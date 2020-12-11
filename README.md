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
Each page has a responsive navigation bar with the name of the site (top left) as a clickable home button. When viewed on a mobile site the navbar presents 

### Home    
Under the navbar, the heading appears in the form of a welcoming message to the user. Under the heading, the introduction begins and is designed to resemble the Star Wars opening crawl, with an attempt at humor. The introduction is short and sweet, it lets the user know there is a quiz available on the page and also has a clickable prompt to let the user know about the club page. 

At the bottom of the introduction, there is a button labeled 'Start Quiz', when clicked, the introduction disappears and the quiz questions appear one by one with four clickable multiple-choice options with a yellow background. Once an option is picked, the 3 incorrect options turn red and the correct option turns green, then a clickable next button appears for the user to go to the next question. This repeats through 10 questions and then the quiz is complete. At the end of the quiz, the user will receive a score accompanied by a GIF reaction to the score. Under this, there is an option to re-attempt the quiz or to quit back to the main page using buttons and hyperlinks.

### Club Page
Under the navbar on the club page, there is a map showing the locations, where the fan club meets all over the country. Under the map, there is a button with the name of each city where the meet-ups take place. When clicked, these buttons will zoom in on the city and show cycling routes all around that city. Directly under this, there is a form for the user to fill out if they are interested in joining the club. Once filled out correctly, the user will then receive an email to the address they have given, indicating if they have been accepted or not.

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