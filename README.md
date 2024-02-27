# [WildWonder](https://wildwonder-d6e191626f44.herokuapp.com/)

## Introduction

- WildWonder is a blog style website that focuses on natural parks and all natural wonders.

- WildWonder is targeted towards all of the nature lovers and adventurers. It offers it's users a place to share their experiences, favourite natural wonders, to vote for articles they like or places they like, or just engage in discussions inside comments on each post.

- I got the idea for this project as I was building a project along side the learning materials as I wanted to expand on the idea of a blog style website and create my take on it. I believe that natural wonders and beauty is all around us, so I decided to create a project about some of the natural wonders, and offer a chance for other users to expand on my idea by being able to create posts of their own on the same topic.

## Wireframes

### WildWonder Homepage

![First sketch - Homepage](static/images/wildwonder_wireframe_homepage.avif)

### WildWonder Contact page

![First sketch - Contact page](static/images/wildwonder_wireframe_contact_page.avif)

### WildWonder Explore page - all articles page

![First sketch - Explore page](static/images/wildwonder_wireframe_explore_page.avif)

### WildWonder article page

![First sketch - Article page](static/images/wildwonder_wireframe_article_page.avif)

### WildWonder login/signup page

![First sketch - Contact page](static/images/wildwonder_wireframe_contact_page.avif)

### WildWonder write page

![First sketch - Write page](static/images/wildwonder_wireframe_write_page.avif)

### WildWonder tablet wireframes

![First sketch - Contact page](static/images/wildwonder_wireframe_tablet1.avif)
![First sketch - Contact page](static/images/wildwonder_wireframe_tablet2.avif)

### WildWonder phone wireframe

![First sketch - Contact page](static/images/wildwonder_wireframe_phone.avif)

### WildWonder Figma design

![First sketch - Contact page](static/images/wildwonder_figma_designs1.avif)
![First sketch - Contact page](static/images/wildwonder_figma_designs2.avif)

### WildWonder ERD

![First sketch - Contact page](static/images/wildwonder_erd.avif)

## About the build

- As I started working on this project I created my ERD using [Lucidchart](https://www.lucidchart.com/) to map out the models I would need and to help with the planning and designing process. After creating them I sketched out my wireframes using [Balsamiq](https://balsamiq.com/). Even before starting to design the project, I had an image in my head as to what I wanted it to look like, so I decided to work out my complete desing, I used [Figma](https://www.figma.com/) to create my second wireframes with colors, images and styles. And then I moved to creating the repository, adding the user stories with labels and iteration milestone, preparing the workspace and starting to code the project.

- To prepare better for the project i went through the older learning material and watched couple of videos and tutorials in order to refresh and expand my knowledge on the topics and languages like javascript and python.

### Preparing the workspace

- After creating the repository and opening my workspace in VS Code through gitpod, I installed Django and created my project file in the top directory, created my first app called blog. I started setting up all of the starting requirements, PostgreSQL database to store my data, connecting with Heroku for deploying the project.

- I created my Post, Comment, Country and Vote Models using the ERD's I have drawn out using Lucidchart to the blog app that were necessary for the project. After which I worked on generic post view that would display posts to the site.

- I added a django summernote package to the requirements to improve the admin panel.

### Templates -Top level directory
#### base.html (template)

- Using the Code Institute project lessons I created the starter base.html file that will be used as a template for the other html files to keep consistency throughout the site.

- I started by creating the basic structure using bootstrap and went with the responsive design that will, for the most part, respond to most screen sizes with the viewwidth and viewheight sizing in place, as to avoid extensive use of media queries, as I did on my first project.

- base.html consists of navigation bar that is consistent through all of the pages and collapses to be interacted by the toggle button on smaller screen sizes; hero section that has a default image set as background and the hero content changes with each page; main section that displays different content depending on the page user is on; and the footer that is consistent through all site pages.

- base.html has five block elements that are used to display different content depending on the page. Hero block is located inside hero section, and main section constains three different block elements:  article_info, about_section and main, and a block extras that loads necessary javascript files.

- base.html is located inside the top level directory file called templates

### Homepage - App
#### index.html (home)

- index.html extends base.html template file to display the website homepage. It uses the predefined block elements to add content to the base.html.

- Hero block element inside the hero section it is displaying the welcome message with couple of paragraphs of user benefits and what the site is for when using the site. Additionally it is checking if the user is logged in or not, and depending on which is the answer it changes the buttons and their use.

- About_section block element inside the main section is displaying an about us message, to give more insite to the user about the page itself.

- Main block element inside main section is displaying recommended articles that is using a code to display top three articles and a map section that will show some of the WildWonder locations on map.

- The site homepage or index.html was originally located inside of the blog file directory, but due to additional changes that were made and added, I decided to separate the homepage into its own app, as it didn't require the data from Models and views inside the blog directory.

### Contact - App

- One Model is in charge of the contact about section, creating required fields for the  titles and messages. Admin can change and update the content in the database that will be displayed to the user from the Admin panel.

- Separate Model is controlling the fields of the contact form and sets all of the requirements for the fields and data for the contact form itself.

- The views are controlling how to handle the user message post request and displaying of contact about section

- The form controlls which fields from the model will be displayed from the Model

- The admin file controlls all of the data displayed to the admin. All of the fields are set to read only so Admin can't change it's content and can only control the checkboxes to mark whether the message was read or responded. Admin can also delete any messages inside the admin panel. 

#### contact.html (Contact Us)

- contact.html extends base.html template to display the website contact page. It uses the predefined block elements to add content to the base.html.

- Hero block element is displaying a title and message that admin wrote and can change inside the admin panel. Additionally it is checking if the user is logged in or not, and depending on which is the answer it changes the buttons and their use.

- About_section block element is displaying a title and message that admin wrote and can also change inside the admin pagel.

- Main block element is displaying the form that is used to contact the website owner/admin. 

- contact.html is located inside of it's own app called contact. The contact app has it's own Models, Views, Form and Admin files that are used to generate and change data displayed to the user on site. 



### Blog - App
#### articles_page.html (Explore)

- articles_page.html extends base.html template to display the Explore page that contains all of the articles. It uses the predefined block elements to add content to the base.html.

-  Hero block element is showing a message that offers insight and to attract the user to continue reading and that they can read the articles that follow.

- About_section block element invites the user to continue exploring the site and to embark on a captivating journey that follows.

- Main block element is used to display all of the articles in a paginated section that displays 6 articles at the time on each page.

- articles_page.html is a template inside of the blog app that displays articles saved inside the database

#### article.html (Article post)

- article.html extends base.html template to display each article when selected. It uses the predefined block elements to add content to the base.html.

- Hero block element displays natural wonder name and the small description of the location. The buttons are changed depending on whether the user is logged in or not.

- About_section block element displays the article content that let's users know what can be seen at the location they are reading about as the main content to attract the users.

- Main block element is showing couple of sections, the first section is split in two, one of which is displaying a map with the location of the WildWonder and the second is populated by another text content about the location. It is followed by a comment and vote section, after which we have related articles section, that will be conditional, and will display the articles that are about the same country or will display random articles as recommendations and write your own article section.

- article.html is a template inside of the blog app that displays each article saved inside the database

## Features

### Base features on all pages
#### Navigation bar and hero section
- The navigation bar is fully responsive, it shrinks and expands with the screen change. 
- When hovered on, the nav bar is fully visible, but when it is not in focus, the opacity is lowered as to show the image beneath it.
- The navigation links respond with size and collapse into a toggle switch that when clicked on displays all of the links as a list in the right hand corner of the screen. The navigation link is darker color when the page is active for each page user is on.
- The logo is fully interactive and when clicked will take user to the homepage.
- Under the navigation links is a user status message, that either showes the "For the full experience please signup/login" message when user is not logged in, and "You are logged in as: ***Username***"
- The page alerts show up on the left hand side underneath the logo. And display either success(green) or error(red) messages, depending on the alert style.
- The hero image is displayed underneath the whole hero section and the navbar. The image adjusts with the screen size and is fully responsive.
- The hero section has a jumbotron displaying the content which changes depending on the page user is on.
- The jumbotron has a hover effect that makes the content fully visible when hovered on, but sets the opacity when it is not in focus, as to reduce the distraction from other content and to make the image underneath visible.
- The jumbotron has two buttons that either prompt and take user to the articles page called "Explore" and the "Join Us" button that takes user to the sign up page, which changes to "Write" button when user is logged in to prompt user to write an article.
- The jumbotron is fully responsive and responds to the screen size change

![First sketch - Contact page](static/images/wildwonder_navbar_and_hero_section.avif)

![First sketch - Contact page](static/images/wildwonder_login_confirmation.avif)

#### About
- The about section contains a couple of paragraphs of content that change depending on the page user is on.
- The about section is fully responsive and changes with screen size.

![First sketch - Contact page](static/images/wildwonder_about_section.avif)
#### Footer
- The footer is fully responsive and changes with screen size.
- The footer consists of the "Join us to post and discuss about WildWonders" message and "Sign Up/Log In" links on the left when the user is not logged in. The meessage and links change to "Thank you for being a part of WildWonder" and "Explore/Write" after the user is logged into the site. On small screens the message moves above. Followed by social link icons in the middle that respond and take users to the corresponding site to the logo on the "button". And on the right there is a message with a link "This site is created as a project for [Code Institute](https://codeinstitute.net/ie/) By: [Luka Black](https://github.com/LukaB25)", which moves to the bottom, underneath the links, on small screens.
- The footer links and social media icons change colors on hover and all open in new tab when clicked.

![First sketch - Contact page](static/images/wildwonder_footer.avif)

![First sketch - Contact page](static/images/wildwonder_footer_after_login.avif)

### Homepage
- ***Hero section*** gives users some idea what the WildWonder is about and what they could gain from joining the community.
- ***About us section*** explains a little about the WildWonder and it is promting users to join the community.
- ***Recommended articles section*** displayes the top three articles by views. The articles strictly depend on which article has the most views. All of the displayed articles show as a card that increses in size on hover, the card contains the article image, name of the location and the date it was posted on. The article card can be clicked anywhere to be taken to the corresponding article it contains.
- ***Map section*** displays a world map and the names/article links of top 10 articles, 5 on either side on medium and larger screens, and 5 above and underneath the map on smaller screens. The homepage map at the moment doesn't display the locations, but could be part of future features. The links are displayed in the order by the view count.
- ***Write an article section*** is there as to prompt users to write their own article about their own favourite place.

![First sketch - Contact page](static/images/wildwonder_navbar_and_hero_section.avif)
![First sketch - Contact page](static/images/wildwonder_about_section.avif)
![First sketch - Contact page](static/images/wildwonder_recommended_articles.avif)
![First sketch - Contact page](static/images/wildwonder_maps_section.avif)
![First sketch - Contact page](static/images/wildwonder_write_article.avif)

### Contact Us
- ***Page hero*** and ***about section*** are used to display a messages about the site and contact options, Admin has full control and can change the hero title and message, but also the about title and message from the admin panel. The messages are there to nudge the user to send a message to the admin.
- ***Contact form*** lets users send their own messages and contact the site owner/admin in order to submit general inquiry, to report a bug they have noticed, site feature request, any special requests or other. When the user sends a message, they receive the message confirmation of success if message submitted or an error message that the request failed if that happens. The admin can access all of the messages inside the admin panel, they can view the form, but can not change the content of the message or details, the admin can read and decide to respond to the message, depending on that they can mark the message as read or responded in the checkbox inside each message.
- Underneath the contact form there is another ***Write an article section*** as to prompt users to write their own article

![First sketch - Contact page](static/images/wildwonder_contact_hero.avif)
![First sketch - Contact page](static/images/wildwonder_contact_about.avif)
![First sketch - Contact page](static/images/wildwonder_contact_form.avif)
![First sketch - Contact page](static/images/wildwonder_write_article_white.avif)

### Explore/Articles page
- ***Hero section*** and ***about section*** give users the insite of what they can find on the explore page, it paints a picture for users to feel invited and welcome to explore the wonders that await within the articles.
- ***Articles section*** displays six articles per page as two rows of three article cards on medium or larger screens, and one at the time on small screens. The article cards are responsive and enlarge on hover and shrink back on hover out. The card consists of the image at the top followed by the location name and the date article was posted. When the card is clicked it opens the article in the same tab.
- There is another write an article section on the bottom of the screen underneath the articles section.

![First sketch - Contact page](static/images/wildwonder_explore_hero.avif)
![First sketch - Contact page](static/images/wildwonder_explore_about.avif)
![First sketch - Contact page](static/images/wildwonder_explore_articles_section.avif)
![First sketch - Contact page](static/images/wildwonder_write_article_white.avif)
### Article
### Write

### Features left to implement

### Possible future features

## Testing
## Troubleshooting
### Unfixed bugs

## Validator testing
### Performance
#### Lighthouse
### HTML, CSS and JavaScript
#### HTML
#### CSS
#### JavaScript
### Python

## Deployment

## Credits
### Media
### Content