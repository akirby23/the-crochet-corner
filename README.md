# The Crochet Corner

## About

The Crochet Corner is a crochet pattern sharing platform and community. Whether you're a seasoned crochet artist or just getting started, this is the perfect place you to get inspired and inspire others to create beautiful crochet projects.

## Table of Contents
- [The Crochet Corner](#the-crochet-corner)
  - [About](#about)
  - [Table of Contents](#table-of-contents)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Features](#features)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries \& Programs](#frameworks-libraries--programs)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
      - [Create the app](#create-the-app)
      - [Create the database | ElephantSQL](#create-the-database--elephantsql)
      - [Cloudinary](#cloudinary)
      - [Set the Config Vars](#set-the-config-vars)
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

## User Stories

## Design

### Colours

### Typography

"Spectral" with a fallback font of "Serif" has been used for the main headings.

"Noto Serif JP" with a fallback font of "Serif" has been used for the remaining elements.

Both fonts aim to give the website a modern, elegant feel.

### Imagery

To match the crochet theme of the project, the image below was used as a hero image on the home page. 

![The Crochet Corner hero image](#)

The image below was selected as a placeholder image for the patterns. 

![Crochet Pattern Placeholder image](#)

A yarn icon was selected as the logo for the project, featuring in the navbar and as the favicon. 

![The Crochet Corner Logo](static/img/the-crochet-corner-logo.jpg)

### Features

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python

### Frameworks, Libraries & Programs

- Django
- Django-allauth
- ElephantSQL
- Heroku
- CodeAnywhere
- Git
- GitHub
- Bootstrap v5.3
- Cloudinary
- Balsamiq
- Summernote
- Am I Responsive
- Google Fonts
- coolors

## Testing

The testing details are documented within the [TESTING.md](TESTING.md) file.

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


### Forking the repository

1. Navigate to [The Crochet Corner  GitHub repository](https://github.com/akirby23/the-crochet-corner).
2. At the top right-hand corner of the page, click on "Fork".
3. Rename or change the description if you wish.
4. Click "Create Fork".
5. A copy of the original repository should now appear on your GitHub account.

### Cloning the repository

1. Navigate to [The Crochet Corner GitHub repository](https://github.com/akirby23/the-crochet-corner).
2. Navigate to the "<> Code" button and click on it.
3. Choose your preferred cloning option (HTTPS, SSH or GitHub CLI).
4. Open Git Bash or Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. In your terminal, enter the following command to clone The Crochet Corner repository:
     - ``git clone https://github.com/akirby23/the-crochet-corner.git``
7. Press enter to create a local clone in your preferred IDE.

## Credits

### Code

- [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/) was consulted during the development of the backend features of this project.
- [Bootstrap 5.3 documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) was consulted during the development of the frontend features of this project.
- [stackoverflow](https://stackoverflow.com/) was used for troubleshooting throughout the development of the project, namely for support with [Bootstrap card images to render in the same height](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width) and with [redirecting to the previous page after completing an action](https://stackoverflow.com/questions/806835/django-redirect-to-previous-page-after-login).
- [django-summernote](https://github.com/summernote/django-summernote) for support with rendering Summernote fields on the frontend.

### Media

- All of the images associated with the patterns were sourced from [Ravelry](https://www.ravelry.com/).
- The hero image was sourced from [istockphoto](https://www.istockphoto.com/photo/craft-hobby-background-with-yarn-in-natural-colors-gm1346636854-424352442?phrase=crochet&searchscope=image%2Cfilm).
- The pattern placeholder image was sourced from [pexels.com](https://www.pexels.com/photo/person-holding-crochet-hook-2897128/).
- The vector image for the logo was sourced from [vecteezy.com](https://www.vecteezy.com/vector-art/8326074-wool-yarn-logo-icon-design-vector).

### Content

All of the pattern content was sourced from [Ravelry](https://www.ravelry.com/).

### Acknowledgements

[Back to the top](#the-crochet-corner)
