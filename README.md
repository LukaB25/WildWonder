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
- ***Contact form*** lets users send their own messages and contact the site owner/admin in order to submit general inquiry, to report a bug they have noticed, site feature request, any special requests or other. When the user sends a message, they receive the message confirmation of success if message submitted or an error message that the request failed if that happens. The admin can access all of the messages inside the admin panel, they can view the form, but can not change the content of the message or details, the admin can read and decide to respond to the message, depending on that they can mark the message as read or responded in the checkbox inside each message. User doesn't need to be logged in to send a message to the user and anyone can submit a request/message.
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
- ***Hero section*** displays basic information about the natural wonder of authors choosing. The placeholder image is replaced by the image of the location the article is written about.
- ***About the article center*** displays who wrote the article, article view count, rating status, comment cound and when the article was uploaded.
    * Author is the username of the user that posted the article
    * View count increments and changes each time the site is loaded and opened.
    * Rating status adds all of the votes up and then divides them by the amount of votes(count of votes made on the post). It changes with each vote and is calculated and displayed as a float between 1 and 5(0 on posts that have no active votes)
    * Comment count counts how many published comments are being displayed (flagged comments are not included in the count). It changes with each vote
    * Uploaded on displays the date and time the article was posted on.
- ***Edit and Delete buttons*** only show up if the logged in user is the same as the user that wrote the article or if the user is admin/superuser. The user can choose to edit their article. If user is not logged in or not the user that wrote the article or superuser/admin they will not see the buttons and will not be able to access them.
    * Article edit - If user decides to edit their article, they are taken to the edit site, the data from the existing article are prepopulated and can be changed inside of the edit screen. The error I haven't yet troubleshoot and sorted is the fact that the image needs to be reuploaded every time the article is edited on the live site or it will default back to the placeholder image, if changed from within the admin panel the image will show up same as before edit.
    * Delete article - the user that wrote the article or the superuser can decide to delete an article at any point. Admin has the ability to delete any article as to make sure he has control over them on live site.
- ***Map section*** consists of two parts, a map and the article paragraph
    * Map uses google maps api and js libraries and js to display a map on the screen. I used google maps documentation and couple of video tutorials to implement the javascript code to read and display the map coordinates set as data sets on the map span that display a marker on the map to show the location of the place in article
    * Paragraph is another section to display content about the location user is writing about
- ***Comment and vote section*** is divided onto comments and votes.
    * Comments are displayed on the left (above on smaller screens). They are paginated as three comments per page. I created a flagged words python list that uses better_profanity python package to moderate and flag inappropriate comments posted on the site. If the word or variation of the word is detected inside of the comment body, the comment is flagged and hidden from view. The alert message will show on the screen under the nav bar (red for flagged comment and green for submitted comment). The comment is only visible to the user that made a comment and the admin unless the comment is either updated as not to contain the flagged word or unless it is approved by the admin. In the right corner of the comment user posted they will have two buttons Edit(green button with notepad with pencil icon) and Delete(red button with trashcan icon), admin will see Edit and Delete buttons on their comments and Delete button on other users comments. Admin has full control over the comments and can delete them at any time even if the comment is not their own, the users on the other hand can only delete their own comments, whether they are flagged or not. If user-admin decides to delete a comment a modal will pop up as a confirmation requirement to confirm its deletion. The submit comment form is located on the right(bottom of comment/vote section on small screens)
    * Votes are displayed on the right (beneath the comments on smaller screens) as star icons that will change color on hover and click. User can change their vote by clicking on any other button, when they are ready they can submit their vote by pressing on Vote button. Users can place as many votes on an article as they would like. Each time the vote is sent the votes on the article will be updated and will display new vote total. Votes can only be deleted by a superuser inside the admin panel, if deleted the votes will increment a new total.
- ***Recommended articles section*** displays three random articles that are published on the site. The articles that are displayed are fully random and change with each refresh.
- There is write an article section underneath the recommended articles section.

![First sketch - Contact page](static/images/wildwonder_article_hero.avif)
![First sketch - Contact page](static/images/wildwonder_features_article_section.avif)
![First sketch - Contact page](static/images/wildwonder_features_article_section_smaller_screen.avif)
![First sketch - Contact page](static/images/wildwonder_article_about_section.avif)
![First sketch - Contact page](static/images/wildwonder_delete_article_modal.avif)
![First sketch - Contact page](static/images/wildwonder_map_section.avif)
![First sketch - Contact page](static/images/wildwonder_comment_vote_section.avif)
![First sketch - Contact page](static/images/wildwonder_comment_flagged_msg.avif)
![First sketch - Contact page](static/images/wildwonder_comment_edit.avif)
![First sketch - Contact page](static/images/wildwonder_comment_after_edit.avif)
![First sketch - Contact page](static/images/wildwonder_comment_updated_msg.avif)
![First sketch - Contact page](static/images/wildwonder_delete_comment_modal.avif)
![First sketch - Contact page](static/images/wildwonder_voting_system.avif)
![First sketch - Contact page](static/images/wildwonder_features_article_section_vote_updated.avif)
![First sketch - Contact page](static/images/wildwonder_recommended_articles_section.avif)
![First sketch - Contact page](static/images/wildwonder_write_article_white.avif)

### Write/Edit page
- ***Hero section*** consists of an input field for the location title/name, text field as first paragraph about the location and an image field.
- ***About section*** consists of an input field for a secondary title which is not mandatory and mandatory the main content text field that should include a larger paragraph of text to be displayed on the site.
- ***Map section*** with a partial map of the world on the left, with two input fields for coordinates(latitude and longitude) and a paragraph field on the right for a larger text content.
- ***Submit section*** a massages that informs user they can press the post article button if they are satisfied with their article.

![First sketch - Contact page](static/images/wildwonder_write_article_hero.avif)
![First sketch - Contact page](static/images/wildwonder_write_article_stats.avif)
![First sketch - Contact page](static/images/wildwonder_write_article_about_section.avif)
![First sketch - Contact page](static/images/wildwonder_write_article_maps_section.avif)
![First sketch - Contact page](static/images/wildwonder_write_article_confirm.avif)

### Sign up, Login, Logout pages
- While logged out the user won't be able to interact with the site fully. They won't be able to write or edit post and comments and they won't be able to place a vote. The site has been secured by using login_required django function and if user tries to access the edit/write page they will be redirected to login page.
- ***Sign up*** - The users can sign up and create an account to access the sites full functions.
- ***Login*** - After signing up and creating an account the user can start writing posts, commenting on existing posts or vote for them. on successful log in user will be taken to the home screen or write/edit page if they tried accessing it by url.
- ***Logout*** - While logged in a user can decide to logout at any point, when the logout is clicked, it will redirect user to confirm whether they want to logout or stay signed in. After confirming the user will be sucessfully logged out and taken to the homepage

### Features left to implement
- ***Google maps*** on home page to display the top 10 article locations as pins on the map. Not implemented due to lack of leftover time for the project.

### Possible future features
- ***User profile*** - Each user has their own profile page where they can update their information, add their picture, see their posts, drafts, comments and votes. Users can choose to have their profile picture displayed on the comments and articles.
- ***Drafts*** - Users can write drafts and save unfinished posts to continue later and start where they left off.
- ***Social Media*** - Users can share their favourite posts directly on social media and the article data is compressed to display basic information to be shared on other platforms along side the picture.
- ***Images*** - Users can add and delete their own images to the existing posts to share their favourite images.
- ***Contact section upgrade*** - Admin can change the information on the contact page without accessing the admin panel. Admin can view all of the messages and user requests inside the contact us page and control and reply to users directly from the site.
- ***Messaging*** - Users can message the post author to start the direct conversation about common interests.

## Testing

|           Action            |        Expectation                           | Outcome |
| :-------------------------: |   :-------------------------------------:    | :-----: |
|           Homepage        |   The homepage loads on page start        |  Pass   |
|       Navigation bar      |   The navigation bar responds to screen size change |  Pass   |
|       Navigation bar :not:hover       |   The opacity is turned down to reduce distraction   |  Pass   |
|       Navigation bar:hover       |   The opacity is turned up and the nav bar is fully visible  |  Pass   |
|       Logo       |        When clicked User is taken to homepage          |  Pass   |
|       Nav link - home     |      When clicked User is taken to homepage    |  Pass   |
|   Nav link - contact us   |      When clicked User is taken to contact page  |  Pass   |
|          Contact Us       |   The contact page loads without issues    |  Pass   |
|       Nav link - explore  |      When clicked User is taken to articles page   |  Pass   |
|           Explore        |   The explore/articles page loads without issues        |  Pass   |
|       Nav link - sign up  |      When clicked User is taken to sign up page, when user logged in it switches to write   |  Pass   |
|           Sign Up        |   The sign up page loads without issues        |  Pass   |
|       Nav link - write    |      When clicked User is taken to write an article, when user logges out it switches to sign up   |  Pass   |
|           Write        |   The write page loads without issues        |  Pass   |
|       Nav link - login    |      When clicked User is taken to login page, after user is logged in it changes to logout   |  Pass   |
|           Login        |   The login page loads without issues        |  Pass   |
|       Nav link - logout   |      When clicked User is taken to logout confiramtion page, after logging out it becomes login link   |  Pass   |
|           Logout        |   The logout page loads without issues        |  Pass   |
|       Navigation bar:active link    |   The navigation bar link is darker color when user is on matching page |  Pass   |
|       Navigation bar - small screens     |   The navigation bar links are collapsed into a toggle switch, that when clicked displays list of links |  Pass   |
|       User status message     |   User status message underneath the navbar displays different message whether user is logged in or not  |  Pass   |
|       Hero section        |        Responds with screen size change          |  Pass   |
|       Hero section jumbotron        |        Responds with screen size change. It is slighly transparent to show the picture beneath        |  Pass   |
|       Hero section jumbotron:hover        |         The screen opacity is turned up so the container is fully visible, becomes transparent on hover out         |  Pass   |
|       Hero section jumbotron content       |        Displays the right content depending on the page using templates          |  Pass   |
|       Hero section Explore btn       |        Takes user to the explore/articles page          |  Pass   |
|       Hero section Join Us btn       |       Showed when user is logged out. Takes user to the sign up page, changes to Write btn if user is logged in          |  Pass   |
|       Hero section Write btn       |       Showed when user is logged in. Takes user to the write an article page, changes to Join Us btn if user is logged in          |  Pass   |
|       About section        |       Responds to the screen size change. Different content is displayed on different pages using templates           |  Pass   |
|       Recommended articles         |        Display top three articles depending on the view count to show most popular articles.          |  Pass   |
|       Recommended articles: cards         |        Display the article image, location name and date article was posted. When card is clicked it opens the article.       |  Pass   |
|       Map      |         The map showes on the screen and can be interacted with. Responds with screen size change         |  Pass   |
|       Links around the map        |       Displays top 10 articles on the site. When hovered the text color changes, on click the article is opened          |  Pass   |
|       Write an article section        |       Displays a message promting users to write their own article           |  Pass   |
|       Write an article btn        |         Takes user to write an article, logged out user is redirected to login page to log in before being redirected to write an article         |  Pass   |
|       Footer        |        Fully responsive to screen size change, the layout changes on smaller screens.          |  Pass   |
|       Footer user msg       |        On the left(top on small screen) there is different message depending on if user is logged in or not          |  Pass   |
|       Footer social links       |        Change color on hover. Open the corresponding social links in new tab         |  Pass   |
|       Footer creator msg       |         On the right(top on small screen) a message is displayed what for and by whom the page created for/by         |  Pass   |
|       Contact us jumbotron and about section       |        Display a messages with titles that admin can change from within the admin panel          |  Pass   |
|       Contact form       |        When filled up and submitted displays a success or error message depending on status         |  Pass   |
|       Contact form - not logged in       |        Users can write and send messages without having to be logged in          |  Pass   |
|       Explore - articles       |         Articles are displayed correctly in descending order, from newest to oldest         |  Pass   |
|       Explore pagination       |         Articles are paginated by 6 per page. User can switch between pages freely         |  Pass   |
|       Explore - published       |         Only published articles are displayed on the site.         |  Pass   |
|       Explore - cards       |          The cards display article image, location title and date posted, the complete card is clickable and opens the article        |  Pass   |
|       Article       |        Users can read the article without having to be logged in          |  Pass   |
|       Article - image      |        The regular placeholder image is replaced by the location image published along with the article          |  Pass   |
|       Article - stats      |        Users can view stats of the post, Author username, view count, rating, comments and upload date          |  Pass   |
|       Article - author     |        Author username is displayed with each article posted on the site          |  Pass   |
|       Article - views      |        View count is incremented each time the site is opened and loaded in by 1          |  Pass   |
|       Article - rating     |        Rating is updated each time a vote is placed on an article and recalculated          |  Pass   |
|       Article - comments   |        Comment count displays the number of published and approved comments          |  Pass   |
|       Article - post date  |        Uploaded on displays the date and time the article has been posted, Irish Time        |  Pass   |
|       Article - hero       |        Hero section jumbotron displays the location name and short into into the location          |  Pass   |
|       Article - about      |        About consists of main title(optional) and content text         |  Pass   |
|       Article - location map      |        Above the map the subtitle displays name of the location along side "on the map:"          |  Pass   |
|       Article - map        |        Map section displays the correct location using the coordinates provided inside the article, users can interact with the map, zoom and move the map around as google maps.          |  Pass   |
|       Article - paragraph  |        Paragraph next to the map displays additional content about the location          |  Pass   |
|       Article - comments   |        Users can read the article comments without having to be logged in          |  Pass   |
|       Article - comment pagination      |        Comments are paginated by three          |  Pass   |
|       Article - flagged comment pagination      |        Flagged comments do not effect the pagination process and are not taken into account when not visible on site          |  Fail   |
|       Article - leaving comments      |        User has to be logged in to leave a comment, user comments are posted and approved          |  Pass   |
|       Article - flagged comments      |        In case a comment contains one of the words on the flagged words list they are automatically flagged and not approved, i.e. hidden from user views unless authorised by admin or corrected by user         |  Pass   |
|       Article - votes       |        Users has to be logged in to vote, users can vote as many times they would like          |  Pass   |
|       Article - recommended section      |        There are three random articles inside the recommended section that change each time the site is loaded up          |  Pass   |
|       Article - recommended article       |       When one of the articles is clicked on the article page is opened           |  Pass   |
|       Article - edit btn       |        If user is the article author or an admin they will be able to see edit article btn         |  Pass   |
|       Article - edit page       |        If user is the article author or an admin they will be transfered to the edit article page         |  Pass   |
|       Article - edit page data      |        Input and text fields are populated with the data from the published article        |  Pass   |
|       Article - edit page image      |        Image field is prepopulated with the existing image, if one was posted with the article         |  Fail   |
|       Article - edit page submit      |        After editing the post, when clicked on update post button the user will be redirected to the published post with updated content         |  Pass   |
|       Article - delete btn     |        If user is the article author or an admin they will be able to see delete article btn          |  Pass   |
|       Article - delete btn confirm     |        When clicked, user has to confirm their delete article request inside the modal          |  Pass   |
|       Comment - edit btn       |        If user is the comment author or an admin they will be able to see edit article btn          |  Pass   |
|       Comment - delete btn     |        If user is the comment author or an admin they will be able to see edit article btn          |  Pass   |
|       Comment - delete btn confirm     |        When clicked, user has to confirm their delete comment request inside the modal          |  Pass   |
|       Sign Up page      |         Users can sign up and create an account without problems, when user signes up they are automatically logged in         |  Pass   |
|       Login page      |           Users can log in and start fully interacting with the site, after logging in user is taken to home page       |  Pass   |
|       Logout page      |          Users can decide to log out at any point and get sent to logout confirmation page        |  Pass   |
|       Write       |         Users can write their own post, all of the required input and text fields need to be filled out         |  Pass   |
|       Write - img       |         Image is not mandatory when writing a new article and will display a placeholder if one is not supplied with the article         |  Pass   |
|       Write - submit       |         When the article is posted by clicking on Post article button, the user is redirected to the live article         |  Pass   |
|       Write - approval       |         Article is automatically approved and posted on the site, unless it contains a flagged word, when it will be flagged and won't be posted         |  Pass   |
|      Flagged post        |         Flagged posts will throw a message that the post will need to be reviewed by the moderator to approve the article if the flagged words are triggered         |  Pass   |


## Troubleshooting
- While creating this project I had couple of major issues that I spent a lot of time troubleshooting.
- ***Postgresql*** - The biggest issue I had was my postgresql database was corrupted and I was unable to do a migrations. I was receiving errors that there were duplicate files and the migration couldn't be done. I decided to troubleshoot it myself, as tutor service was finished for the day, I managed to access my postgresql database and I decided to delete the tables that were causing the issues, that ended up causing new errors stating that the database has no table needed, I tried to add/replace the deleted table, but the errors continued and I was unable to repair it myself. I sent a message to the Tutor support and waited until the next morning. One of the tutors, John, reached out to me and tried helping me, before instructing me that it would be better if I just requested a new database from Code Institute and create new migrations inside the new database, which I ended up doing. Luckily I stored most of t he data in my notes, so I was able to restore my content quickly.
- ***Cloudinary images*** - I was having issues with my cloudinary images being updated and edited. At firs I got it to work, but while I was coding my views and rest of the project I must have changed something which created issues with my images on articles not being uploaded and were continuously loading the site without posting the article to the page, when posting the article without an image, everything worked fine. I ended up following Code Institue lessons and tried searching the stackoverflow but it was not working, I watched a tutorial on how to implement Cloudinary Images and I kept changing the code back and forth, restoring it to previous code from github, but no luck. I left for a little while, and when I came back it started to work, so I am unsure in how I fixed it. But it started to work, so I decided to stop working on that part of code and to have it work like this. This is one of the reasons there is an unfixed bug with the images having to be reuploaded when the article is being edited.
- I kept commenting out code and trying to create a new code when the created code did not work, as to try and work out where my errors are. I also left couple of notes for myself as to make sure to come back to the code while coding.
- ***Country model(Deleted)*** - originally I created a Country model that was supposed to be used as a tag as to categorise the articles by country the article is written about. I kept having issues with the code, and I couldn't get it to work as planned, so I decided to scrap the model as my project deadline was coming closer.
- I tried to add the checkbox to confirm whether the admin is writing post, and whether they are writing a plain post or coded article. After the images incident the code in article was not working, so I decided to remove it from the site, but it can still be ticked on inside of the admin page, as to make the article more visually appealing.
- I realised users could still access the write a post page while logged out if they decided to append /write/ to end of explore url, after which I reserched a bit and added the login_required from django. 
- After talking with my mentor and him pointing the login_required I remembered I forgot to check if my /edit/ was secure, it was not. I added the if statement to the edit_article view as to make sure my site is secure.
- I realised I have forgot to add target="_blank" to my social links, so they were opening in the same tab, that has been corrected.
- I tried to write a code and even find online on how to protect my Google Maps API key and nothing worked, so I decided to leave my Google Maps API open, but I have restrictions in place.
- I have been getting the cache errors on my lighthouse reports that are caused by the Cloudinary URLs that were reducing my Best Practises in the report.

### Unfixed bugs
- ***Image loading*** when the article is being edited. As currently the image needs to be reuploaded to work, otherwise it is removed and placeholder is set as current picture
- ***Comment pagination*** when the comments are being paginated, if there are flagged comments not visible by the user, they will be taken into the count of paginated comments, I haven't had time to fix this error, but it could have been resolved with an if statement inside of the template separating the approved comments from the flagged comments.

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
