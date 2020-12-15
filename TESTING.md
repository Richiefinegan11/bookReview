# Testing

## Testing the code 

### HTML
* I ran all my HTML code through [W3CValidator](https://validator.w3.org/) and found the below:
    * The login and Register page images were missing the alt tags, I have fixed this.
    * The profile page had an ID duplicating on it, this was changed to a class and rectified.
    * The review page images were missing also the alt tags, I have fixed this.
    * All other pages are fine apart from a warning on missing heading in the section for flash messages. The heading is hidden in with a statement.

### CSS 
* I ran all my CSS through [W3CValidator CSS](http://jigsaw.w3.org/css-validator/) and recieved no errors with my CSS file.

### JavaSctipt
* I ran my code through [jshint](https://jshint.com/) and there was no errors

### Python
* I ran my code through [PEP8](http://pep8online.com/checkresult) and there were no errors

## Testing UX Stories

* As a user who enjoys reading, wants a book recommendation, they can review them on the book review page
    * The user can simply log in or register, a profile is automatically created, they can go an view the review from other users on the review page

* As a user who enjoys reading, wants a book recommendation, they can review them on the book review page
    * The user can simply log in or register, a profile is automatically created, the can then go and easily write a review on the write review page, they can also view and edit their review on their profile.

* As a user who needs inspiration on a book to buy, they can go to the book review page and click the link where the book is for sale
    * The user can go to the book review page, where a link is displayed for each book, when the click the link, it will bring them to a books store for them to purchase it 
* As the owner of the site, who also loves reading, I can make money off people clicking the links through my page.
    * The link on each book, has a promo code with the sites name, which will make money for the site owner, every time the book is purchased through this site

## Manual testing of all elements and functionality on every page

### Login/Register page

#### Navbar 
My NavBar has two states changes responsively to all devices. I have tested all of this and it works.

* When the user is logged out, the user should only see the below in the NavBar:
    * Never Judge a book + logo
    * Home
    * Login 
    * Register

* When the user is logged out, all links are working correctly:

Click the never judge a book logo and it brings you to the register page -> click the home button and it brings you to the login page -> click the login button and it brings you to the login page -> click the register page and it brings you to the register page.

* When the user is logged in, the user should only see the below in the NavBar:
    * Never Judge a book + logo
    * Book Review 
    * My Profile
    * Write Review 
    * Logout

* When the user is logged in, all links are working correctly:

Click the never judge a book logo and it brings you to the book review page -> click the book review button and it brings you to the book review page -> click my profile button and it brings you to my profile page -> click the write review button and it brings you to the write review page -> click the logout button and it logs the user out and redirects them to the login page.

#### Footer
My Footer has two state changes responsively to all devices. I have tested all of this and it works.

* When the user is logged out, the user should only see the below in the Footer:
    * Never Judge a book + logo + slogan
    * Register links
    * Login link

* When the user is logged out, all links are working correctly:

Click the birth register links and it directs the user to the top of the register page -> click the login link and it directs the user to the top of the login page.

* When the user is logged in, the user should only see the below in the NavBar:
    * Never Judge a book + logo + slogan
    * Write Review link
    * Check-Out Book Review Link
    * Delete Account link
    * Logout

* When the user is logged in, all links are working correctly:

Click the write review link and it brings the user to the write review page -> click the check out book reviews link and it brings the user to the book reviews page -> click the logout link and it brings the user to the login page -> click the delete account link and it brings the user to a delete account page, where the user is asked to confirm deletion or stay, if they click the "I want to stay" button, they are brought back to their profile. If the click the "Yes, I want to stay" button, their account is deleted and they are directed to the register page, with working flash message "User Deleted"

### Login page

* Login form is displayed
* Typed a username that is less then 5 characters and click off the field - Field and 'Username must be between 5-15 characters using only letters and numbers' field turns red
* Typed a username that contains symbols and click off the field - Field and 'Username must be between 5-15 characters using only letters and numbers' field turns red
* Type a username which is between 5 - 15 characters and contains no symbols and click off the field - Field turns green
* Type a password which is less then 5 characters and click off the field - Field and 'Password must be between 5-15 characters using only letters and numbers' message turn red
* Type a Password which contains symbols and click off the field - Field and 'Password must be between 5-15 characters using only letters and numbers' message turn red
* Type a username which contains symbols and click login - Message appears to say 'Please match the requested format'
* Type a password which contains symbols and click login - Message appears to say 'Please match the requested format'
* Type a Password which is between 5 - 15 characters and contains no symbols and click off the field - Field turns green
* Click Login with one or both fields missing - Message appears to say 'Please fill in this field'
* Login with an invalid username - Flash message appears 'Incorrect Username and/or Password'
* Login with an invalid password - Flash message appears 'Incorrect Username and/or Password'
* Login with a correct username and password - You are taken to your profile page
* Click the 'Register Now' link under form - You are taken to the register page

### Register 
* Register form is displayed
* Typed a username that is less then 5 characters and click off the field - Field and 'Username must be between 5-15 characters using only letters and numbers' field turns red
* Typed a username that contains symbols and click off the field - Field and 'Username must be between 5-15 characters using only letters and numbers' field turns red
* Type a username which is between 5 - 15 characters and contains no symbols and click off the field - Field turns green
* Type a password which is less then 5 characters and click off the field - Field and 'Password must be between 5-15 characters using only letters and numbers' message turn red
* Type a Password which contains symbols and click off the field - Field and 'Password must be between 5-15 characters using only letters and numbers' message turn red
* Type a username which contains symbols and click register - Message appears to say 'Please match the requested format'
* Type a password which contains symbols and click register - Message appears to say 'Please match the requested format'
* Type a Password which is between 5 - 15 characters and contains no symbols and click off the field - Field turns green
* Click register with one or both fields missing - Message appears to say 'Please fill in this field'
* Register with a username which has already been registered - Flash message appears 'Username already exists'
* Register with a correct username and password - you are taken to the profile page
* Click the 'Login Here' link under form - You are taken to the login page

### Profile
* At the top of the image page a welcome <username> appears when first logged in or registered
* Also near the top are messages showing the user in the session how many books they have reviewed out of the total books reviewed
* If the user has reviewed some books they will appear with images and the details of the book.
* If the user has not reviewed any books, a message will appear with a call to action link, when the link is clicked, it will bring the user to the write review page. (I added this feature in on testing)
* On each profile, there is an edit and delete button. If you click on the edit button, it will bring you to the edit review page. If you click the delete button, the book will be deleted from the database and you will be redirected to your profile
* At the bottom of the profile page, a back to the top link will appear, if 3 or more books are reviewed. When clicked, it will bring you to the top of the profile page. 

### Book Reviews 
* At the top of the book review page, a search form is displayed
* If you try to search with an empty field, you will be prompted to "Please fill out this field"
* If less than 3 or more characters are input, you will be prompted by a message to input 3 or more characters
* When the field is filled out and the text doesn't match any of the book's text, a message appears in the middle of the page reading "No books found! Why not write this book's review yourself?" with a call to action for the user to write the review, the link brings the user to the write review page. (This call to action was added while testing)
* When the text input in the field, matches details of a book on the page, the book displays
* When the reset button is clicked, the Book review page refreshes, and all the books appear again
* On this page, books are displayed in card form with an image and a seen review link, which when clicked, reveals the review. Also on the card, is a link that brings you to amazon to buy the book. (This is under the Never judge a book promo code, so the site will make money off the purchase)
* On the card reveal, it shows the book review and which user input the review, and an X icon, when clicked, closes the reveal. 
* At the bottom of the profile page, a back to the top link will appear, if 3 or more books are reviewed. When clicked, it will bring you to the top of the review page

### Write Review
* A form is displayed with a cancel and add review buttons
* All fields in the form must be filled for the user to add a review or "please fill out this field" will appear
* If all the fields are filled in correctly when the add review button is clicked, the review is added to the database and will appear on both the user's profile and book review page. A message will also flash "Review Successfully Added", to confirm
* When the cancel button is clicked, you will be directed back to the review page

### Edit Review
* A form is displayed with cancel and edit review buttons
* All fields are prefilled with the book's details, selected to be edited
* Once the books as been edited and the fields are input correctly when the edit review page is clicked, you will be redirected to the profile page and a message will flash "Your Review Has Been Updated"
* When the cancel button is clicked, you will be directed back to the review page

### Delete Account
* Page displays with options to delete the account or to stay on the site
* Click 'I want to stay!' and you are taken to the profile page
* Click 'Yes I am done' the account is deleted and you are taken to the register page 

## Devices 

* Moto G4 - Google Chrome Dev tools

* iPhone X - Google Chrome Dev tools

* iPhone 6/7/8 - Google Chrome Dev tools

* iPhone 6/7/8 plus - Google Chrome Dev tools

* iPhone 5/se - Google Chrome Dev tools

* iPad - Google Chrome Dev tools

* iPad Pro - Google Chrome Dev tools

* Surface Duo - Google Chrome Dev tools
