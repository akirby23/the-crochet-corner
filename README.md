# The Crochet Corner

## About

The Crochet Corner is a crochet pattern sharing platform and community. Whether you're a seasoned crochet artist or just getting started, this is the perfect place you to get inspired and inspire others to create beautiful crochet projects.

[Link to the deployed app](https://the-crochet-corner-ec269bd20745.herokuapp.com/)

## Table of Contents
- [The Crochet Corner](#the-crochet-corner)
  - [About](#about)
  - [Table of Contents](#table-of-contents)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [Design](#design)
      - [Colours](#colours)
      - [Typography](#typography)
      - [Imagery](#imagery)
      - [Wireframes](#wireframes)
      - [Database Design](#database-design)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries \& Programs](#frameworks-libraries--programs)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Local Deployment](#local-deployment)
      - [Forking the repository](#forking-the-repository)
      - [Cloning the repository](#cloning-the-repository)
  - [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

## User Goals

- Ability to browse through the collection of crochet patterns.
- Ability to create, read, edit & delete their own crochet patterns.
- Ability to save/unsave crochet patterns for later.
- Ability to comment on crochet patternsin order to share their thoughts/feedback.

## Site Owner Goals

- To create an appealing, accessible and user friendly platform for crocheters of all skill levels.
- Ability to create, read, update and delete crochet patterns to maintain the collection.
- Ability to approve comments before they are displayed on the crochet patterns.

## User Experience

### User Stories

#### User

1. As a user, I can register for an account so that I can sign in and access member-only features such as reviewing, saving and commenting on crochet patterns.
2. As a user, I can log in so that I can review, save and comment on crochet patterns.
3. As a registered user, I can sign out so that I can ensure the security of my account.
4. As a registered user, I can create crochet patterns so that I can add to the collection.
5. As a user, I can read crochet patterns so that I can follow the instructions to create crochet projects.
6. As a registered user, I can update my own crochet patterns so that I can keep them up to date.
7. As a registered user, I can delete my own crochet patterns so that I can maintain my collection.
8. As a registered user, I can comment on a crochet pattern so that I can share thoughts and/or feedback.
9. As a user, I can view the comments on each individual crochet pattern so that I can read the discussions and feedback left by others.
10. As a registered user, I can edit my comments so that I can correct any errors or share additional thoughts/feedback.
11. As a registered user, I can delete my comments so that I can remove previous comments that I no longer want to be public.
10. As a registered user, I can save or unsave a crochet pattern for later so that I can easily access it in the future, or remove it if I no longer need it.
11. As a registered user, I can view my saved crochet patterns so that I can easily access the patterns that interest me as and when I need to.
12. As a user, I can navigate through multiple pages of patterns so that I can explore the collection of crochet patterns without needing to scroll excessively.
13. As a user, I can scroll back to the top of a page at the click of a button so that I won't have to scroll excessively.
14. As a user, I can navigate back to the pattern list at the click of a button so that I won't need to navigate back using the "back" button in my browser.
15. As a registered user, I can rate a crochet pattern on a scale of 1 to 5 stars so that I can provide feedback on the quality of it based on my own experience.
16. As a user, I can view the average rating of each individual crochet pattern so that I can assess the quality of them based on feedback from others.
17. As a user, I can search for crochet patterns so that I can easily find one that interests me.
18. As a site user, I can refine my search so that I can find crochet patterns that match my specific needs.
19. As a registered user, I can create blog posts so that I can share crochet-related tips and/or showcase my projects.
20. As a user, I can navigate through multiple pages of comments so that I can browse through them without needing to scroll excessively.
21. As a user, I can download crochet patterns in PDF format so that I can access them offline or print them off to use while creating the crochet project.
22. As a user, I can share crochet patterns via text, email or social media so that I can share crochet inspiration with friends, family or other members of the crochet community.

### Site Admin

1. As a site admin, I can access the admin panel so that I can manage my collection of crochet patterns.
2. As a site admin, I can create new crochet patterns so that users can access them.
3. As a site admin, I can read crochet patterns so that I can follow the instructions to create crochet projects.
4. As a site admin, I can update pre-existing crochet patterns so that I can keep them up to date and add new information as necessary.
5. As a site admin, I can delete crochet patterns so that I can remove patterns from the collection as necessary.
6. As a site admin, I can approve or disapprove comments so that I can ensure that the comments on each pattern are appropriate and relevant.
7. As a site admin, I can categorise the crochet patterns so that I can organise them by difficulty/theme.

### Design

#### Colours

![Colour palette](documentation/readme/colour-palette.png)

`#0e0e0e` has been used as the font colour.

`#83B271` has been used as an accent colour.

`#F8F8F8` has been used as the background colour.

The colours above were generated from the hero image to match the theme of the website.

#### Typography

"Spectral" with a fallback font of "Serif" has been used for the main headings.

"Noto Serif JP" with a fallback font of "Serif" has been used for the remaining elements.

Both fonts aim to give the website a modern, elegant feel.

#### Imagery

To match the crochet theme of the project, the image below was used as a hero image on the home page. 

![The Crochet Corner hero image](documentation/readme/imagery/hero-image.png)

The image below was selected as a placeholder image for the patterns. 

![Crochet Pattern Placeholder image](documentation/readme/imagery/pattern-placeholder.jpg)

A yarn icon was selected as the logo for the project, featuring in the navbar and as the favicon. 

![The Crochet Corner Logo](static/img/the-crochet-corner-logo.jpg)

#### Wireframes

<details>
<summary>Home Page</summary>

|  Mobile | Web  | 
|---|---|
| ![Mobile Home Page](documentation/readme/wireframes/homepage-mobile.png)  | ![Web Home Page ](documentation/readme/wireframes/home-page-web.png) |

</details>

<details>
<summary>Pattern List</summary>

|  Mobile | Web  | 
|---|---|
| ![Mobile Pattern List](documentation/readme/wireframes/pattern-list-mobile.png)  |  ![Web Pattern List](documentation/readme/wireframes/pattern-list-web.png) |

</details>

<details>
<summary>Pattern Page</summary>

|  Mobile | Web  | 
|---|---|
| ![Mobile top of the Pattern Page](documentation/readme/wireframes/pattern-page-mobile-1.png) ![Mobile middle of the Pattern Page](documentation/readme/wireframes/pattern-page-mobile-2.png) ![Mobile bottom of the Pattern Page](documentation/readme/wireframes/pattern-page-mobile-3.png)  | ![Web top of the Pattern Page](documentation/readme/wireframes/pattern-page-web-1.png) ![Web middle of the Pattern Page](documentation/readme/wireframes/pattern-page-web-2.png) ![Web bottom of the Pattern Page](documentation/readme/wireframes/pattern-page-web-3.png) |

</details>

<details>
<summary>Create/Edit Pattern</summary>

|  Mobile | Web  | 
|---|---|
| ![Mobile Create/Edit Pattern ](documentation/readme/wireframes/create-edit-pattern-mobile.png) | ![Web Create Pattern top of the page](documentation/readme/wireframes/create-pattern-web-1.png) ![Web Create Pattern bottom of the page](documentation/readme/wireframes/create-pattern-web-2.png) ![Web Edit Pattern top of the page](documentation/readme/wireframes/edit-pattern-web-1.png) ![Web Edit Pattern bottom of the page](documentation/readme/wireframes/edit-pattern-web-2.png) |

</details>

<details>
<summary>Delete Pattern</summary>

|  Mobile | Web  | 
|---|---|
| ![Mobile Delete Pattern](documentation/readme/wireframes/delete-pattern-mobile.png) | ![Web Delete Pattern](documentation/readme/wireframes/delete-pattern-web.png) |

</details>

**Deviation from the Wireframes**

- Due to time constraints, the following features have not been implemented:
    - Blog
    - Pattern rating system
    - Pattern search functionality
- To make the home page more visually appealing, the website description was split into 3 cards instead of being displayed as a block of text below the hero image. 
- A TikTok social media link has been added to the footer alongside the Instagram and YouTube nav links. 
- For better navigation, a "Back to All Patterns" button has been added to the pattern page. 
- A "Cancel" button has been added to the Create & Edit Pages. 


#### Database Design

<details>
<summary>Original Design</summary>

During the planning phase of this project, the models were designed as follows: 

**Pattern Model**

| Key |  Name | Field Type  |  Validation |   
|---|---|---|---|
| PrimaryKey | pattern_id | AutoField |  | 
|   | title  | CharField  | max_length=200, unique=True  |
|   |  featured_image |  CloudinaryField | 'image', default='placeholder'  |
|   |  description | TextField  |   |
|   |  created_on | DateTimeField  | auto_now_add=True  |
|   |  difficulty level | CharField  | choices=DIFFICULTY_LEVEL_CHOICES, max_length=20 |
|   | yarn_type  | CharField  | max_length=50  |
|   |  hook_size | CharField  |  max_length=10 |
|   |  gauge | CharField  | max_length=50  |
|   | instructions  | TextField  |   |
|   |  status |  IntegerField |  choices=STATUS, default=0 |


**Comment Model**

| Key |  Name | Field Type  |  Validation |    
|---|---|---|---|
|PrimaryKey | comment_id | AutoField |  | 
| ForeignKey  |  pattern | ForeignKey  |   |
| ForeignKey  |  author | ForeignKey  | User, on_delete=models.CASCADE  |
|   | text  | TextField  |   |
|   | created_on  | DateTimeField  | auto_now_add=True  |
|   | approved  | BooleanField  | default=False  |

</details>

<details>
<summary>Current Design</summary>

As the needs of the project evolved during the development phase, the models were later updated. 

Below is the current design of the models:

**Pattern Model**

| Key |  Name | Field Type  |  Validation | 
|---|---|---|---|
| PrimaryKey | pattern_id | AutoField |  | 
|   | title  | CharField  | max_length=200, unique=True  |
|  | slug  | SlugField | max_length=200, unique=True |
|   |  featured_image |  CloudinaryField | 'image', default='placeholder'  |
|   |  description | TextField  |   |
|   |  created_on | DateTimeField  | auto_now_add=True  |
| ForeignKey | created_by | ForeignKey | User, on_delete=models.CASCADE, default='1' |
|   |  difficulty level | CharField  | choices=DIFFICULTY_LEVEL_CHOICES, max_length=20 |
|   | yarn_type  | CharField  | max_length=50  |
|   |  hook_size | CharField  |  max_length=10 |
|   |  gauge | CharField  | max_length=50  |
|   | instructions  | TextField  |   |
|   |  status |  IntegerField |  choices=STATUS, default=0 |
|  | saved  | ManyToManyField | User, related_name='saved_pattern', blank=True |

**Comment Model**

| Key |  Name | Field Type  |  Validation |    
|---|---|---|---|
|PrimaryKey | comment_id | AutoField |  | 
| ForeignKey  |  pattern | ForeignKey  |   |
| ForeignKey  |  author | ForeignKey  | User, on_delete=models.CASCADE  |
|   | text  | TextField  |   |
|   | created_on  | DateTimeField  | auto_now_add=True  |
|   | approved  | BooleanField  | default=False  |
|  |  |  |  |

</details>

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python

### Frameworks, Libraries & Programs 

- [Django](): to design the project features in the backend.
- [Django-allauth](https://docs.allauth.org/en/latest/): for user authentication.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): for rendering the Django forms.
- [django-summernote](https://summernote.org/): to add WYSIWYG editors to the pattern's text fields. 
- [Bootstrap v5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/): to style the project and to make it responsive.
- [PostgreSQL](https://www.postgresql.org/): as the object-relational database. 
- [ElephantSQL](https://customer.elephantsql.com/): used as the database.
- [Heroku](https://dashboard.heroku.com/): to deploy the project.
- [CodeAnywhere](https://app.codeanywhere.com/): to write the code.
- [GitPod](https://gitpod.io/): to write the code.
- [Git](https://git-scm.com/): to commit & push the code to GitHub for version control.
- [GitHub](https://github.com/): to store the code in its repository and to manage the KanBan board.
- [ChromeDevTools](https://developer.chrome.com/docs/devtools) for debugging and manual testing.
- [Cloudinary](https://cloudinary.com/): to store static files online.
- [Balsamiq](https://balsamiq.com/): to create the wireframes.
- [Whitenoise](https://whitenoise.readthedocs.io/en/latest/): for hosting static files for deployment.
- [Google Fonts](https://fonts.google.com/): to import the "Spectral" & "Noto Serif JP" fonts.
- [FontAwesome](https://fontawesome.com/): to import the icons used throughout the project.
- [coolors](https://coolors.co/): to generate the colour palette.

## Testing

The testing details are documented within the [TESTING.md](TESTING.md) file.

## Agile Development Process

This project was developed using an Agile approach.

- User stories were prioritised using the MoSCoW method:

|   |   |
|---|---|
| Must Have  | Essential features  |
| Should Have  | Important but not absolutely essential features  |
| Could Have  | Nice to have but not essential features  |
| Won't Have  | Non essential features, may be implemented in the future  |

GitHub Issues was used to prioritise each user story and to define acceptance criteria & tasks.

![Completed User Stories](documentation/readme/github-issues-completed-1.PNG)
![Completed User Stories](documentation/readme/github-issues-completed-2.PNG)
![Won't Have User Stories](documentation/readme/github-issues-wont-have.PNG)


- User stories were then refined into Epics using Milestones in GitHub:

|   |   |
|---|---|
| Iteration 1  | ![Iteration 1](documentation/readme/epics/epic-1.PNG) |
| Iteration 2  | ![Iteration 2](documentation/readme/epics/epic-2.PNG) |
| Iteration 3  | ![Iteration 3](documentation/readme/epics/epic-3.PNG) |
| Iteration 4  | ![Iteration 4, issue closed](documentation/readme/epics/epic-4.1.PNG) ![Iteration 4, issue deprioritised](documentation/readme/epics/epic-4.2.PNG) |
| Iteration 5  | ![Iteration 5](documentation/readme/epics/epic-5.PNG) |
| Iteration 6  | ![Iteration 6](documentation/readme/epics/epic-6.PNG) |


A GitHub Project was used to manage and track the progress of the project:

![The Crochet Corner GitHub Project](documentation/readme/the-crochet-corner-project.PNG)


## Deployment

### Heroku Deployment

This application has been deployed to Heroku using the following steps:

#### Create the app
1. Create a Heroku account on [heroku.com](https://heroku.com/)
2. From the top right hand corner of the dashboard, click "New", then click "Create new app".
3. Give the app a unique name and select the relevant region.
4. Click "Create app".

#### Create the database | ElephantSQL

This app requires the use of a PostgreSQL database. 

To obtain your own database:

1. Navigate to [elephantSQL.com](https://customer.elephantsql.com/) and register for an account using your GitHub account. 
2. Click on "Create New Instance".
3. Name your database and select the "Tiny Turtle (Free)" plan. 
4. Click "Select Region", and on the next page, select your preferred region. 
5. Once you've created your instance, click on the name of the instance to access the database URL & password.

#### Cloudinary

This app uses Cloudinary to store images online. 

To obtain your Cloudinary key:

1. Navigate to [cloudinary.com](https://cloudinary.com/) and create an account. 
2. Navigate to the dashboard to obtain your API Environment Variable.
3. When copying the API Environment Variable, be sure to remove the "CLOUDINARY_URL=" from the start of the URL.

#### Set the Config Vars

From the settings tab on the app dashboard, navigate to "Config Vars and click "Reveal Config Vars".

Set them as follows:

| Key | Value | 
| --- | --- |
| CLOUDINARY_URL| Your Cloudinary URL |
| DATABASE_URL| Your own database URL |
| DISABLE_COLLECTSTATIC | 1 (temporary step, to be removed before deployment)
| SECRET_KEY | Your own secret key |


#### Prepare required files
- In your preferred IDE, install the project's requirements by running the following command:
  `pip3 install -r requirements.txt`
- Create a Procfile within the root directory.
- In the procfile, add the following code: web: `gunicorn PROJ_NAME.wsgi`
   - Replace the PROJ_NAME with your own main Django app name.
- Push the changes to GitHub. 


#### Deploy to Heroku

- Navigate to the "Deploy" tab. 
- Link the GitHub repository in the Deployment Method sectionn. 
- Deploy manually or enable automatic deploys if you would prefer. 
- If any errors occur during deployment, the build logs can be used to troubleshoot them.

The app will now be live.

### Local Deployment

- Create an env.py file in the root directory if there isn't one already. 
- Ensure to add the env.py file to your .gitignore file <u>before</u> commiting or pushing to GitHub to prevent credentials from being exposed. 
- Add `import.os` to the top of the env.py file. 
- Add your secret key, Cloudinary URL & database URL in this format: 
<br>
`os.environ.["SECRET_KEY] = "YOUR_SECRET_KEY"`
<br>
`os.environ.["CLOUDINARY_URL"] = "YOUR_URL"`
<br>
`os.environ.["DATABASE_URL] = "YOUR_URL"`
- Add your environment variables to the settings.py file. 

Note: Ensure to set "DEBUG" to "False" in production or during deployment.


#### Forking the repository

1. Navigate to [The Crochet Corner  GitHub repository](https://github.com/akirby23/the-crochet-corner).
2. At the top right-hand corner of the page, click on "Fork".
3. Rename or change the description if you wish.
4. Click "Create Fork".
5. A copy of the original repository should now appear on your GitHub account.

#### Cloning the repository

1. Navigate to [The Crochet Corner GitHub repository](https://github.com/akirby23/the-crochet-corner).
2. Navigate to the "<> Code" button and click on it.
3. Choose your preferred cloning option (HTTPS, SSH or GitHub CLI).
4. Open Git Bash or Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. In your terminal, enter the following command to clone The Crochet Corner repository:
     ``git clone https://github.com/akirby23/the-crochet-corner.git``
7. Press enter to create a local clone in your preferred IDE.

## Credits

### Code

- [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/) was consulted during the development of the backend features of this project.
- [Bootstrap 5.3 documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) was consulted during the development of the frontend features of this project.
- [stackoverflow](https://stackoverflow.com/) was used for troubleshooting throughout the development of the project. It also helped with [ rendering Bootstrap card images in the same height](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width), with [redirecting to the previous page after completing an action](https://stackoverflow.com/questions/806835/django-redirect-to-previous-page-after-login), [preventing users from editing/deleting content that they have not posted](https://stackoverflow.com/questions/43209606/django-writing-generic-update-view-restricted-to-certain-user) and [with displaying success messages on a DeleteView](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown).
- [django-summernote](https://github.com/summernote/django-summernote) for support with rendering Summernote fields on the frontend.
- Code Institute's "I Think Therefore I Blog" walkthrough project. 

### Media

- All of the images associated with the patterns were sourced from [Ravelry](https://www.ravelry.com/).
- The hero image was sourced from [istockphoto](https://www.istockphoto.com/photo/craft-hobby-background-with-yarn-in-natural-colors-gm1346636854-424352442?phrase=crochet&searchscope=image%2Cfilm).
- The pattern placeholder image was sourced from [pexels.com](https://www.pexels.com/photo/person-holding-crochet-hook-2897128/).
- The vector image for the logo was sourced from [vecteezy.com](https://www.vecteezy.com/vector-art/8326074-wool-yarn-logo-icon-design-vector).

### Content

All of the pattern content was sourced from [Ravelry](https://www.ravelry.com/).

### Acknowledgements

- I would like to thank my Code Institute mentor, Mo Shami, for guiding me with this project and for sharing his expertise.
- I would also like to thank Jason from the tutor support team at Code Institute for helping me to troubleshoot an issue that I was having with template rendering.

[Back to the top](#the-crochet-corner)
