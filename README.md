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

Each page also has a responsive footer, with the sites name and logo and also has links for the write review page and the book review page, when the user is in session but will display login and register links, when the user is not in session. At the bottom right of the footer, there is also a log out/login button, depending on whether the user is in session or not.

### Login/Register 

#### Regiser
On the Register page, there is a form at the top of the page, where the user is prompted to register their username and password. Once filled in and the user clicks the submit/register button, a "POST" method will check if the username is already registered. If the username is not registered, a profile will be created for the user and they will be brought to their profile. However if the username is already in the database, a flash message will show Username already exists, at the top of the page. Under the form button, there is a link to take users that have already registered to the login page.
#### Login
The Login page is very similar to the Register page, there is a form at the top of the page, where the user is prompted to type in their username and password. The form will on except characters from 5 to 15 in lenght and numbers and letters, the user must match this or a prompt will instruct them to match the correct format.
The user can then log in with their details, when the user clicks the submit/login button, a "POST" method checks the database to see if the username is registered. If the username is registered, the user will be logged in. However, if the username is not found in the database, a message will flash "Incorrect Username and/or Password at the top of the page. The message will not indicate specifically, which one is incorrect. Under the form button, there is a link to take users that have not already registered to the register page.
#### Login/Register page content
Under these forms, there is an introdcutory question. This is followed by nice images of books and text explaining the aim of the site to users. On large devices, the text and image position change from left to right down the page, to give a more aesthetically pleasing fell to the page. On smaller and mobile devices, they adapt to what looks more pleasing on the mobile device. 

### Book Review 
On the top of the Book Review page there is a responsive search bar, this allows the user to search for a book review, based on the book title, author or genre. Under the search bar, there is a search button for the user to commence the searc or a reset button, which will reset the page. Next on the page is the the book reviews from all the users. This is laid out on cards with an image and text as card content. The text has a clickable card reveal "See Review" link, which reveals the books review. Under this is the Title of the book, followed by the author and the genre. When a user uploads a review, the books will neatly and responsively fall in to line. The last piece of text on the card is the link that will take the user to an external site to buy the book, the site will then gain commission for directing the user through their site.
At the bottom of the page, under the book review, there is a link marked "back to top", which brings the user back to the top of the page.


### Features left to implement
* Store - Once there is a sufficient amount of fans, I will then implement a merchandise page. The fans can then purchase merchandise from the show upon visiting the website.
* Blog - Once the site gets some more interest and traffic, I will add a blog page to the site so fans can then interact with each other online too.

## Technologies Used
* [Visual Studio Code](https://code.visualstudio.com/)
   * The developer used visual studio code as their IDE while building the website
* [BootstrapCDN](https://getbootstrap.com/)
  * The project used Bootstrap4 to simplify the layout of the website and make it easily responsive
* [Google Fonts](https://fonts.google.com/)
  * This project used google fonts to style the website fonts
* [Popper.js](https://popper.js.org/)
  * This project used Popper.js reference Javascript needed for the responsive navbar
* [jQuery](https://jquery.com/)
  * The project uses jQuery to reference Javascript needed for the responsive navbar
* [EmailJS](https://www.emailjs.com/)
  * The project uses emailJS for the user to join the club and the owner to receive the email
* [Google Maps API](https://developers.google.com/maps/documentation)
  * The project uses the google maps API to show where the meet-up spots are

## Testing
Testing can be accessed [here](TESTING.md)

## Deployment
This project was developed using Visual Studio Code, committed to git, and pushed to Github.

To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:

1. Log into GitHub.
From the list of repositories on the left-hand side of the screen, select [Richiefinegan11/stoic_in_action](https://github.com/Richiefinegan11/rickAndMortyFans).
2. From the menu items near the top of the page, select Settings.
3. Scroll down the page to the GitHub Pages section.
4. Under Source, in the Github Pages section, click the drop-down menu labeled None and select Master Branch.
5. On selecting Master Branch the page is automatically refreshed, the website is now deployed.
6. Scroll back down to the GitHub Pages section where the link to the deployed website will be, at the top of the section.

### How to run the code locally

To clone this project from GitHub:

1. Click on the repository [Richiefinegan11/stoic_in_action](https://github.com/Richiefinegan11/rickAndMortyFans).
2. To the right of the page, click the "Clone or download button.
3. When the Clone with HTTPs section shows, copy the URL of the repository.
4. In your local IDE open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone - then paste the URL copied for as advised in step 3.

## Credits 

### Code 

* CSS
  * Stack Overflow was very helpful in assisting me with questions I needed to be answered to create the style sheet.

* Main page HTML -
  * Some of the HTML5 was copied from BootstrapCDN and modified for layout and responsiveness.

* Main page JS -
  * The javascript used for the quiz was influenced by:
    * [Sitepoint](https://www.sitepoint.com/simple-javascript-quiz/)
    * [VerkkoNet](https://www.youtube.com/channel/UCErON4Z0YyiVHKNtx4BvLfg)
    * [Web Dev Simplified](https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw)
* Club Page JS -
  * The Google maps was achieved by using [Google Maps API](https://developers.google.com/maps/documentation)
  * The form on this page was achieved by using [EmailJS](https://www.emailjs.com/) and implemented with the help of the Code Institue course
  

### Content 
  * The content for this site was influenced by the TV show "Rick and Morty"
  * Some Questions for the quiz were obtained from [thequiz.com](https://www.thequiz.com/can-you-pass-the-hardest-rick-and-morty-quiz-on-the-internet/)

### Media 
  * The main image used in the background was taken from [HD Wallpaper](https://www.hdwallpaper.nu/rick-and-morty-wallpapers/)

### Acknowledgements

Jonathan Munz (Code Institute Mentor) - For his advice, helpful feedback, and reassurance towards the end of this project, as always.

The Code Institute Slack Community - which was so helpful, especially for this project. Viewing other student's projects helped me a lot with my own.

My friends and family, especially Aaron Mcdonnell & Ian P Brady for their very helpful feedback for this site.

### Disclaimer
The content of this Website is for educational purposes only