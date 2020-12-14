# Never Judge a Book
## Welcome! Please click the below image, I hope you enjoy it.

[![Book Image](static/images/flickedBook.jpg)](https://never-judge-book.herokuapp.com/)

## Table of content
* [Overview](#Overview)
* [UX](#UX)
* [Wireframes](#Wireframes)
* [Features](#Features)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credits)
## Overview

This is a mobile-first site that is designed for users to easily view book reviews from other users and also add a review themselves. It is aesthetically pleasing due to the users ability to easily add an image to their reviews by simply copying a link for their image and pasting it in to the write review form. It is also an easy site to navigate around due to it's simplicity, which should keep the users attention. For book lovers, of all ages, this site is perfect as it is not complicated by unnecessary details and gives the user the essential information.

The goals of this site are:
* Provide a fun site for books lovers to come and find recommendations
* Nice UX to keep the users interested
* Build up a database by getting users to register to the site
* Build brand awareness
* Earn money for each book purchased

The user's goals are:
* To find new books worthy of reading based on recommendations
* Leave recommendations for others for books the user has enjoyed or not enjoyed

## UX
This website has the potential to reach a large market, both young and old people who like to read. It's both simple and aesthetically pleasing, as well as easy to navigate around. The main page has a call to action, for the user to register to the site. If the user is already registered, there is a link under the register form, which will bring the user to the login page. 
Once the user has registered or logged in, they will be directed to their own profile which will be created for them and will show a welcoming message. On their profile page, the user will be shown text with the number of books they have reviewed versus the books actually reviewed, the profile page will also have their review displayed. For users who have only registered, they can navigate easily to the "Write Review" tab which will bring them to a form, where they can write their review.
When the user writes the review, a successful message will flash before them to confirm. The user can then view the nicely laid out book reviews by navigating to the "book review" page.

### Ideal Users
* English Speaking
* People who love to read books
* Opionated people
* Social People

### User Stories
* As a user who enjoys reading, wants a book recommendation, they can review them on the book review page
* As a user who enjoys giving their opions on books they have read, they can create a profile, and review a book on the write review page
* As a user who needs inpsiration on a book to buy, they can go to the book review page and click the link where the book is for sale
* As the owner of the site, who also loves reading, I can make money off people clicking the links through my page.

## Wireframes 
* Home
  * [Desktop](static/images/home_desktop.png)
  * [Tablet](static/images/home_tablet.png)
  * [Mobile](static/images/home_mobile.png)
* Write Review
  * [Desktop](static/images/writeReview_desktop.png)
  * [Tablet](static/images/writeReview_tablet.png)
  * [Mobile](static/images/writeReview_mobile.png)
* Register
  * [Desktop](static/images/register_desktop.png)
  * [Tablet](static/images/register_tablet.png)
  * [Mobile](static/images/register_mobile.png)
* Your Review
  * [Desktop](static/images/yourReview_desktop.png)
  * [Tablet](static/images/yourReview_tablet.png)
  * [Mobile](static/images/yourReview_mobile.png)
* Book Page
  * [Desktop](static/images/bookPage_desktop.png)
  * [Tablet](static/images/bookPage_tablet.png)
  * [Mobile](static/images/bookPage_mobile.png)

## Features
### Existing Features
Each page has a responsive navigation bar with the name of the site (top left) as a clickable button. This button takes the user to the login page, when the user is not logged in, and to the book reviews page, when the user is logged in. 
On larger devices, when the user is not in session, the nav bar will show clickable links "Home", "Login" and "Register" on the top right. When the user is in session on larger devices, the navbar will show clickable links "Book Review", "My Profile", "Write Review" and "Log Out".
On smaller and mobile devices, when the user is not in session, a clickable book icon will show on the nav bar, which, when clicked, displays a side nav to the right of screen, with clickable links "Home", "Login" and "Register". When the user is in session, on smaller and mobile devices, the same thing happens, except the side nav will show clickable links "Book Review", "My Profile", "Write Review" and "Log Out".

Each page also has a responsive footer, with the sites name and logo and also has links for the write review page and the book review page, when the user is in session but will display login and register links, when the user is not in session. At the bottom right of the footer, there is also a log out/login button, depending on whether the user is in session or not. There is also a delete button for the in session user to remove their account from the database. When the user clicks the delete account link, they will be redirected (as part of a defensive design strategy) to a delete account confirmation page, where they will have an option "I want to stay" button, which will bring the user back to their profile or a "Yes, I am done" button, which will delete the account.

### Login/Register 

#### Regiser
On the Register page, there is a form at the top of the page, where the user is prompted to register their username and password. Once filled in and the user clicks the submit/register button, a "POST" method will check if the username is already registered. If the username is not registered, a profile will be created for the user and they will be brought to their profile. However if the username is already in the database, a flash message will show Username already exists, at the top of the page. Under the form button, there is a link to take users that have already registered to the login page.
#### Login
The Login page is very similar to the Register page, there is a form at the top of the page, where the user is prompted to type in their username and password. The form will on except characters from 5 to 15 in lenght and numbers and letters, the user must match this or a prompt will instruct them to match the correct format.
The user can then log in with their details, when the user clicks the submit/login button, a "POST" method checks the database to see if the username is registered. If the username is registered, the user will be logged in. However, if the username is not found in the database, a message will flash "Incorrect Username and/or Password at the top of the page. The message will not indicate specifically, which one is incorrect. Under the form button, there is a link to take users that have not already registered to the register page.
#### Login/Register page content
Under these forms, there is an introdcutory question. This is followed by nice images of books and text explaining the aim of the site to users. On large devices, the text and image position change from left to right down the page, to give a more aesthetically pleasing fell to the page. On smaller and mobile devices, they adapt to what looks more pleasing on the mobile device. 

### Book Review 
At the top of the Book Review page there is a responsive search bar, this allows the user to search for a book review, based on the book title, author or genre. Under the search bar, there is a search button for the user to commence the searc or a reset button, which will reset the page. Next on the page is the the book reviews from all the users. This is laid out on cards with an image and text as card content. The text has a clickable card reveal "See Review" link, which reveals the books review. Under this is the Title of the book, followed by the author and the genre. When a user uploads a review, the books will neatly and responsively fall in to line. The last piece of text on the card is the link that will take the user to an external site to buy the book, the site will then gain commission for directing the user through their site.
At the bottom of the page, under the book review, there is a link marked "back to top", which brings the user back to the top of the page.

### Write Review
The Write review page is a simple page with a form. The user cannot input their review on this by entering the required fields. Once the user clicks the add review button, after filling in the form, the book will be uploaded to the database and will then appear on the "Book Review" page & also the user's profile page. There is also a cancel button, which will bring the user to the "Book Review" page.

### Profile
At the top of the profile page, once user has logged in or registered, they are greeted by a welcome message, indicating to them the amount of books they have reviewed versus the total amount reviewed. Under this message, if the user has wrote a review, it will display in a similar format to the book review page. The books diplayed on this page will only be books the in session user has reviewed. 
On each book reviewed by the user, there is an edit and a delete button. 
When the user clicks the edit button, it will bring the user to a separate page, which has a form. The form will be prefilled with the chosen books info, for ease of editing. When the user is finished editing, they can then click the edit button, once this is done, they will be redirected to their profile and a message will flash "Your Reveiw Has Been Updated". There is a cancel button on the edit review page which brings the user back to their profile.
When the user clicks the delete button, their review will be removed from the database and they will be redirected to their profile with a message displaying "Review Successfully Deleted". 

### Features left to implement
* Store - Once there is a sufficient amount of fans, I will then implement a merchandise page. The fans can then purchase merchandise and boo accessories.
* Blog - Once the site gets some more interest and traffic, I will add a blog page to the site's user can then interact with each other online too.

## Technologies Used
* [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
   * HTML5 was used as the markup language for this project
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
  * CSS was used for this project to style the site 
* [MATERIALIZE](https://materializecss.com/)
  * The project used Materialize to simplify the layout of the website and make it easily responsive
* [GOOGLE FONTS](https://fonts.google.com/)
  * This project used google fonts to style the website fonts
* [MONGODB ](https://www.mongodb.com/)
  * MongoDB was used as the projects database
* [JQUERY](https://jquery.com/)
  * The project uses jQuery to reference Javascript needed for the responsive navbar
* [PYTHON3](https://www.python.org)
  * Python3 was used to help simplify writing the code and reduce time needed for this project
* [FLASK](https://flask.palletsprojects.com/en/1.1.x/)
  * The project used the the Flask frameword for ease
* [FLASK PYMONGO](https://flask-pymongo.readthedocs.io/en/latest/)
  * Used to support the use of Flask with MongoDB
* [WERKZEUG SECURITY](https://werkzeug.palletsprojects.com/en/1.0.x/)
  * Werkzeug is the WSGI that was used for this project
* [BSON](https://www.mongodb.com/json-and-bson)
  * BSON is the binary encoding of JSON-like documents that MongoDB uses when storing documents in collections
* [JINJA](https://jinja.palletsprojects.com/en/2.11.x/)
  * Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates
* [PYMONGO](https://pymongo.readthedocs.io/en/stable/index.html)
  * PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python
* [HEROKU](https://www.heroku.com/home)
  * Heroku is a cloud platform as a service supporting several programming languages
* [GITHUB](https://github.com/)
  * Hosting for software development and version control using Git

## Database Used
MongoDB is a general purpose, document-based, distributed database built for modern application developers and for the cloud era. MongoDB is a NoSQL database programme. I created the following collections for my project:

* books : This was used to store the the users reviews and was displayed on multiple pages such as the "book review" page and their profile.
* users : This was used to store the users login in details when they registed for the site and then was grabed for logging in. It also provived data for the profile page and other links to be used

## Testing
Testing can be accessed [here](TESTING.md)

## Deployment
### Deploying Online 
View live page: https://never-judge-book.herokuapp.com/

To deploy this project online (online IDE - like gitpod) follow the following steps:

1. Clone this repository and initialize your own repository - open the repository
2. Creat an env.py file where you created your variables (IP, PORT, MONGO_URI, MONGO_DBNAME and a secret key for flashed massages)
3. Used the CLI to install all of the frameworks and collect them inside the requirements.txt file
    * You can do this by typing "pip3 install -r requirements.txt" in yout command line interface
4. Create a Procfile for Heroku stating that it should run app.py as a web app and use Python as the language
5.  Create your MongoDB database and collections, populated it with data and connected to it by following the steps in MongoDB
6. Sign up to Heroku and go to https://dashboard.heroku.com/apps and created your new app
7. Connect to your GitHub repository via Heroku
8. Go to settings and in Config Vars, click Reveal Config Vars :
    * IP = 0.0.0.0
    * PORT = 5000
    * MONGO_DBNAME is book_review
    * MONGO_URI is mongodb+srv://<username>:<password>@myfirstclust.tmrem.mongodb.net/<database-name>?retryWrites=true&w=majority
    * SECRET_KEY is a password chosen by you
9. Connect to a branch you want to deploy from and the project will be deployed to the Heroku
10. Click on the 'view' button to view the live deployed project

### Local Deployment
To deploy this project locally I followed the following steps:

You will need to install the following to run this locally:

* An IDE such as Microsoft Visual Studio Code
* Python3 to run the application
* PIP to install all app requirements
* MongoDB to develop your own database either locally or remotely on MongoDB Atlas.
* GIT for cloning and version control

When deplying locally, you will need to follow the below steps:

* Clone this GitHub repository by either clicking the green Clone or download button and downloading the project as a zip-file (remember to unzip it first), or by entering the following into the Git CLI terminal:
    * git clone https://github.com/Richiefinegan11/bookReview.git
* Navigate to the correct file location after unpacking the files
    * cd <path to folder>
* Create a .env file with your credentials. (The same as deploying the project online)
* Install all requirements from the requirements.txt file using this command:
    * sudo -H pip3 -r requirements.txt
* Sign up for a free account on MongoDB and create a new Database called food The Collections in that database should be as stated in the interaction design
* You should now be able to launch your app using the following command in your terminal:
    * flask run
* The app should now be running on localhost on an address similar to http://127.0.0.1:5000. Simply copy/paste this into the browser of your choice!

## Credits 

### Content 
  * The content for this site was taken from the project idea section, suggested by code institue.
  * All text used for this is my own

### Media 
  * The images for the login/register page was obtained from the below:
    * [Visual Hunt](https://visualhunt.com/photos/book/)
    * [Pixabay](https://pixabay.com/images/search/love%20book/)
    * [Freepic](https://www.freepik.com/premium-photo/open-book-with-glasses-wooden-table-against-background-set-books-vintage-toning_5237563.htm)
 * Images for the Book Review page are from [Book Depository](https://www.bookdepository.com/)
 * All other images are uploaded by the users

### Acknowledgements

Jonathan Munz (Code Institute Mentor) - For his advice, helpful feedback, and reassurance towards the end of this project, as always.

The Code Institute Slack Community - which was so helpful, especially for this project. Viewing other student's projects helped me a lot with my own. I would especially like to thank [Lewis](https://code-institute-room.slack.com/team/USRLF3J0M) and [Lige](https://code-institute-room.slack.com/team/UT8PXGLTZ) for their feed back in the peer code review channel

My friends and family, especially Catherine and Jordan for their very helpful feedback for this site.

### Disclaimer
The content of this Website is for educational purposes only