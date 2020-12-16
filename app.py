import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# regestering a user to the db
@app.route("/")
@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get('user'):
        return redirect(url_for("review"))

    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# login page for the user
@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('user'):
        return redirect(url_for("review"))

    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


# profile page for the user
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if session["user"]:
        # grab user from the db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # grab the list of books reviewed by user from db
        books_reviewed = mongo.db.books.find(
            {"created_by": session["user"]}
        ).sort("book_title", 1)

        all_books = mongo.db.books.find()

        number = books_reviewed.count()

        book_count = all_books.count()

        return render_template(
            "profile.html",
            username=username,
            number=number,
            books_reviewed=books_reviewed,
            book_count=book_count)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# book review page
@app.route("/review")
def review():
    books = list(mongo.db.books.find())
    return render_template("review.html", books=books)


# search bar for book review page
@app.route("/search", methods=["GET", "POST"])
def search():
    # uses form to get text from the db
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("review.html", books=books)


# write review page
@app.route("/write_review", methods=["GET", "POST"])
def write_review():
    # inserts 'review' details to db
    if request.method == "POST":
        review = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "image": request.form.get("image"),
            "review": request.form.get("review"),
            "created_by": session["user"]
        }
        mongo.db.books.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("write_review"))

    return render_template("write_review.html")


# edit review page
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    # inserts amended info to db
    if request.method == "POST":
        submit = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "image": request.form.get("image"),
            "review": request.form.get("review"),
            "created_by": session["user"]
        }
        mongo.db.books.update({"_id": ObjectId(review_id)}, submit)
        flash("Your Review Has Been Updated")
        return redirect(url_for("profile", username=session["user"]))
    # finds current info for form
    review = mongo.db.books.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", review=review)


# delete review page
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    # removes the review by grabbing the object id
    mongo.db.books.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


# delete account page
@app.route("/delete_account", methods=["GET", "POSTS"])
def delete_account():
    if session.get('user'):
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        return render_template("delete_account.html", username=username)

    return redirect(url_for("login"))


# removes user from the db
@app.route("/delete_account_confirmed", methods=["GET", "POST"])
def delete_account_confirmed():
    mongo.db.users.remove({"username": session["user"]})
    flash("User Deleted")
    session.pop("user")
    return redirect(url_for("register"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
