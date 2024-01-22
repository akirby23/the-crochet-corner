# Testing | The Crochet Corner

[Return to README.md](README.md)

## Table of Contents

- [User Stories](#user-stories)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
- [Validator Testing](#validator-testing)

## User Stories

| User Story  | Acceptance Criteria   |  Status |
|---|---|---|
| As a user, I can register for an account so that I can sign in and access member-only features such as reviewing, saving and commenting on crochet patterns.  |The user should be able to register for an account by clicking on the Sign Up button on the navigation bar. <br> Once the user clicks on the Sign Up button, they should see a form that will guide them through how to register for an account.  |  Pass |
| As a user, I can log in so that I can review, save and comment on crochet patterns.  | A "Log In" button should display in the navigation to users who are not already logged in. <br>The user should be required to provide a valid username & password.<br>Feedback should be given to the user to confirm whether or not they have signed in successfully.  | Pass  |
| As a registered user, I can sign out so that I can ensure the security of my account.  | A "Log Out" button should be visible in the navigation bar to users who are signed in. <br> Feedback should be provided to the user to confirm that they have successfully signed out.  |  Pass |
| As a registered user, I can create crochet patterns so that I can add to the collection.  | Only users who are logged in should be able to create crochet patterns. <br> A "Create Pattern" button should display to users who are logged in on the Pattern List page. | Pass  |
| As a user, I can read crochet patterns so that I can follow the instructions to create crochet projects.  | Once published, the title, description and image associated with the crochet pattern should display in a listed format on the patterns page. <br> Users should be able to click on each pattern to display them in full. <br> The title, description, image, difficulty level, recommended yarn type, recommended hook size, gauge & instructions should display in a clear format. <br>Site admins should be able to view the patterns in the admin panel in order to be able to edit/delete them as necessary. |  Pass |
| As a registered user, I can update my own crochet patterns so that I can keep them up to date.  | Only users who are logged in should be able to edit patterns. <br> Users should only be able to edit their own patterns.  | Pass  |
| As a registered user, I can delete my own crochet patterns so that I can maintain my collection.  | Only users who are logged in should be able to delete patterns. <br> Users should only be able to delete their own patterns.   | Pass |
| As a registered user, I can comment on a crochet pattern so that I can share thoughts and/or feedback.  | Only users that have logged in should be able to leave a comment. <br> Users who are not logged in should be prompted to log in/sign up before adding a comment.  | Pass  |
| As a user, I can view the comments on each individual crochet pattern so that I can read the discussions and feedback left by others.  | The comments should display in a clear format below the pattern. <br> Only approved comments should be displayed.  | Pass  |
| As a registered user, I can edit my comments so that I can correct any errors or share additional thoughts/feedback.  | Users who are logged in should only be able to edit their own comments. <br> Edited comments should be set back to pending admin approval. <br> The user should be informed of this. | Pass  |
| As a registered user, I can delete my comments so that I can remove previous comments that I no longer want to be public.  | Users who are logged in should only be able to delete their own comments. <br> Users should be prompted to confirm whether or not they want to delete the comment before the action is finalised.  |  Pass |
| As a registered user, I can save or unsave a crochet pattern for later so that I can easily access it in the future, or remove it if I no longer need it.  | A bookmark icon labelled "Save for later" should display on each crochet pattern. <br> Users should be able to click on the icon to save the pattern for later. <br> Users who are not signed in should be prompted to log in or sign up if they attempt to save the pattern. <br> Users who are signed in should be given feedback to confirm whether or not the pattern was successfully saved. <br> Users who are logged in should be able to unsave patterns. | Pass  |
| As a registered user, I can view my saved crochet patterns so that I can easily access the patterns that interest me as and when I need to.  | Only users who have logged in should be able to view their saved patterns. <br> Only patterns that the user has saved should be accessible on the My Saved Patterns page. <br> The patterns saved by the user should be displayed in a clear format on the My Saved Patterns page.|  Pass  |
| As a user, I can navigate through multiple pages of patterns so that I can explore the collection of crochet patterns without needing to scroll excessively.  | No more than 9 patterns should display on the page. <br> Where there are multiple pages, the user should be able to navigate to the next or previous page. <br> The correct page count should display at the bottom of the page.   | Pass  |
| As a user, I can scroll back to the top of a page at the click of a button so that I won't have to scroll excessively.  | A "Back to the Top" button should be fixed to the Pattern page. <br> User should be taken to the top of the page once the button is clicked. | Pass  |
| As a user, I can navigate back to the pattern list at the click of a button so that I won't need to navigate back using the "back" button in my browser.  | A button should appear on the pattern page that will allow the user to navigate back to all patterns.   | Pass  |
| As a site admin, I can access the admin panel so that I can manage my collection of crochet patterns.  | Access should be resricted to site admins only.  | Pass  |
| As a site admin, I can create new crochet patterns so that users can access them.  | Crochet patterns should be created via a form that is accessible via the admin panel only. <br> The form should be intuitive, prompting the site admin to provide important information such as the title, description, difficulty level, recommended yarn type, recommended hook size, gauge & instructions. <br> The site admin should be able to upload an image of the completed crochet project to accompany the pattern. | Pass  |
| As a site admin, I can read crochet patterns so that I can follow the instructions to create crochet projects.  | Once published, the title, description and image associated with the crochet pattern should display in a listed format on the patterns page. <br> Users should be able to click on each pattern to display them in full. <br> The title, description, image, difficulty level, recommended yarn type, recommended hook size, gauge & instructions should display in a clear format. <br> Site admins should be able to view the patterns in the admin panel in order to be able to edit/delete them as necessary. | Pass  |
| As a site admin, I can update pre-existing crochet patterns so that I can keep them up to date and add new information as necessary.  | The option to edit crochet patterns should be accessible via the admin panel only. <br> The form should have the same fields as the form used to create the pattern. The fields should pre-populate the data that the site admin submitted when the form was created. <br> Feedback should be given to the site admin on whether or not the changes saved successfully. | Pass <br> Note: Pattern editing functionality is available on the admin panel, however the scope of the project has changed and editing functionality is now available on the frontend to authenticated users.  |
| As a site admin, I can delete crochet patterns so that I can remove patterns from the collection as necessary.  | The option to delete a pattern should be available on the admin panel only. <br> The site admin should be prompted to confirm that they want to delete the pattern before the action is finalised.  | Pass <br> Note: Pattern deleting functionality is available on the admin panel, however the scope of the project has changed and deleting functionality is now available on the frontend to authenticated users.  |
|As a site admin, I can approve or disapprove comments so that I can ensure that the comments on each pattern are appropriate and relevant.   | Only site admins should be able to approve or disappove comments.  |  Pass |



## Manual Testing

<details>
<summary>Nav bar</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Logo  | The Crochet Corner logo is displayed on the left hand side of the nav bar. <br> Once clicked, the user is redirected to the home page.  | Pass  |   |
| Home nav link  | Once clicked, user is redirected to the home page.  | Pass  |   |
| Patterns nav link   | Once clicked, user is directed to the All Patterns page if they are not authenticated. <br> If they are authenticated, a dropdown menu appears containing the “All Patterns” and “My Saved Patterns” nav links.   | Pass  |   |
| All Patterns nav link  | Visible to authenticated users only. <br> Once clicked, the user is directed to the All Patterns page.  | Pass  |   |
| My Saved Patterns nav link  | Visible to authenticated users only. <br> Once clicked, the user is brought to the My Saved Patterns page.  | Pass  |   |
| Log In nav link  | Visible to authenticated users only. <br> Once clicked, the user is brought to the My Saved Patterns page.   | Pass  |   |
| Log Out nav link  | Visible only to users who are authenticated. <br> Once clicked, the user is redirected to a page that will prompt them to confirm whether or not they want to log out.    | Pass  |   |
| Sign Up nav link  | Visible only to users who are not authenticated. <br> Once clicked, the user is directed to a form that allows them to sign up.   | Pass  |   |

</details>

<details>
<summary>Footer</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Instagram footer link  | Once clicked, Instagram opens in a new tab.    | Pass  |   |
| TikTok footer link  | Once clicked, TikTok opens in a new tab. | Pass  |   |
|YouTube footer link   | Once clicked, YouTube opens in a new tab. | Pass  |   |
| Disclaimer  | A disclaimer is visible in the footer advising the user that the website has been created for educational purposes only.   | Pass  |   |


</details>

<details>
<summary>Home Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Hero Section  | Hero image is displayed with a welcome message for the user.  | Pass  |   |
| Calls to Action  | Browse, Save & Share calls to action are displayed on the homepage  | Pass  |   |

</details>

<details>
<summary>All Patterns Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Create New Pattern button  |  Visible to authenticated users only. <br>  Once clicked, the user is redirected to a form that will allow them to create a new pattern. <br>Users who attempt to access the Create Pattern Page are prompted to log in or sign up.  | Pass  |   |
|  Pattern Cards | A pattern card is displayed for each crochet pattern. <br> Only approved patterns are displayed on this page. Once clicked, the user is brought to the full pattern page.  | Pass  |   |
| Pattern Image  | The pattern’s image is displayed on the pattern card.   | Pass   |   |
| Pattern title  | The pattern’s title is displayed on the pattern card.   | Pass  |   |
| Pattern difficulty level  | The pattern’s difficulty level is displayed on the pattern card.   |  Pass  |   |
| Pagination  | The correct page number displays at the bottom of the page. <br> When there are more than 9 crochet patterns, the user can navigate easily to the next/previous/first/last pages.   | Pass  |   |

</details>

<details>
<summary>My Saved Patterns Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|  Pattern Cards | A pattern card is displayed for each crochet pattern. <br> Only patterns that have been saved by the authenticated user are displayed on this page. Once clicked, the user is brought to the full pattern page.  | Pass  |   |
| Pattern Image  | The pattern’s image is displayed on the pattern card.   | Pass   |   |
| Pattern title  | The pattern’s title is displayed on the pattern card.   | Pass  |   |
| Pattern difficulty level  | The pattern’s difficulty level is displayed on the pattern card.   |  Pass  |   |
| Pagination  | The correct page number displays at the bottom of the page. <br> When there are more than 9 crochet patterns, the user can navigate easily to the next/previous/first/last pages.   | Pass  |   |

</details>

<details>
<summary>Pattern Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
Pattern Title  |  The pattern’s title is displayed. | Pass   |   |
| Pattern Image  | The pattern’s image is displayed.  | Pass  |   |
| Pattern Description  | The pattern’s description is displayed.  | Pass  |   |
| Edit Button  | Visible to the authenticated user who created the pattern only. <br> Once clicked, the user is redirected to a form that allows them to edit the pattern. <br> The form’s fields are pre-populated with the data from the pattern.   | Pass  |   |
| Delete Button  |Visible to the authenticated user who created the pattern only.<br> Once clicked, the user is brought to a form that will prompt them to confirm whether or not they want to delete the pattern.    | Pass  |   |
| Save for Later - Log In/Sign Up buttons  | Unauthenticated users are prompted to log in/sign up in order to save the pattern for later. <br> If the unauthenticated user logs in or signs up via the log in/sign up buttons, they are redirected back to the pattern page they were on.   | Pass  |   |
| Save for Later button  | Visible to authenticated users only. <br> Once clicked, the pattern is saved for later and the user is alerted. The button’s text changes to “Saved for Later”.  | Pass  |   |
| Saved for Later button  | Visible to authenticated users who have saved the pattern only. <br> Once clicked, the pattern is removed from the user’s saved pattern and the user is alerted. <br> The button’s text changes back to “Save for Later”.  |  Pass |   |
| Difficulty Level  |  The pattern’s difficulty level is displayed. | Pass  |   |
|  Yarn Type | The pattern’s yarn type is displayed.  | Pass  |   |
| Hook Size  | The pattern’s hook size is displayed.  | Pass  |   |
| Gauge  | The pattern’s gauge type is displayed.  | Pass  |   |
| Abbreviations  | The pattern’s abbreviations are displayed.  | Pass  |   |
| Instructions  | The pattern’s instructions are displayed.  |   |   |
| Comment Section - Log In / Sign Up buttons  | Unauthenticated users are prompted to log in/sign up in order to leave a comment. <br> If the unauthenticated user logs in or signs up via the log in/sign up buttons, they are redirected back to the pattern page they were on.   |   |   |
|Comment box   | Authenticated users can input text into the text field and click “Submit” to add a comment. Upon successful completion of the action, the user is alerted that their comment is pending approval.   | Pass   |   |
| Comments  | Approved comments are displayed in a clear format. <br> The date on which the comment was created is displayed alongside the name of the user who created the comment.   | Pass  |   |
| Comment Section - Edit Button  | Visible to the authenticated user who created the comment only. <br> Once clicked, the user is directed to a form that will allow them to edit their comment. <br> The data in the form is prepopulated with the user’s comment.   |   |   |
| Comment Section - Delete Button  | Visible to the authenticated user who created the comment only. <br> Once clicked, the user is prompted to confirm whether or not they want to delete the comment.   |   |   |
| Back to the Top button  | Once clicked, the user is redirected to the top of the page.   |  Pass |   |
| Back to All Patterns button  | Once clicked, the user is redirected to the All Patterns page.   | Pass  |   |


</details>

<details>
<summary>Create Pattern Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Create Pattern Page Access  | Accessible to authenticated users only. | Pass  | Testing on a url with the structure of `/create_pattern/` while logged out, was redirected to the log in page. |
| Title Input  | Authenticated user can input the title via a charfield.  | Pass  |   |
| Image Input  |  Authenticated user can upload an image. | Fail  |  User can upload an image however it is not saved to the database, and therefore defaults to the placeholder. |
| Placeholder image  | Placeholder image is in place.  | Fail  | No placeholder image is in place in the form. However, featured_image default is set to "placeholder" in the backend so the placeholder image should still be rendered.  |
|Description Input   | Authenticated user can input the title via a textfield/WYSIWYG editor.  |  Pass |   |
| Difficulty Level Input   | Authenticated user can select the difficulty level from the dropdown.  | Pass  |   |
| Yarn Type Input  | Authenticated user can input the yarn type via a charfield.  | Pass  |   |
| Hook Size Input   | Authenticated user can input the hook size via a charfield.  |  Pass |   |
| Gauge  | Authenticated user can input the gauge via a charfield.  | Pass  |   |
|  Abbreviations Input | Authenticated user can input the abbreviations via a textfield/WYSIWYG editor.  | Pass  |   |
| Instructions Input  | Authenticated user can input the instructions via a textfield/WYSIWYG editor.  | Pass   |   |
| Status Input  | Authenticated user can set the status to “Draft” or “Published”  | Pass  | While the user has the option to save their pattern as a draft, drafts can only currently be edited on the admin panel. Time constraints have prevented draft editing/saving/publishing on the frontend, however this is expected to be implemented in the future.  |
|Submit Button   | Once clicked, the pattern is created and the user is alerted. <br> If the form is not valid, the user is prompted to correct any errors.   | Pass  |   |
| Cancel Button   | Once clicked, the action is aborted and the user is redirected back to the pattern list.  |  Pass | Alerts for cancelling actions are expected to be implemented in the future.  |


</details>

<details>
<summary>Edit Pattern Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|  Edit Pattern Page Access | Page is accessible to the user who created the pattern only.   | Pass  | Tested on a url with the structure of `patterns/<slug>/edit_pattern` while logged in as a user who did not create the pattern, 404 error thrown.<br> 403 error would be preferred, however marking as a pass as the user is still being prevented from completing an unauthorised request. |
| Pre-populated fields  | All fields from the Create Pattern Page are prepopulated with the data that the authenticated user who created the pattern previously entered.  | Pass  |  |
| Edit pre-populated fields  | All pre-populated fields can be edited.  | Fail  |  All fields can be edited and all changes are reflected on the frontend & backend with the exception of the featured image, which defaults to the placeholder image.   |
| Save Button  | Once clicked, the changed are saved and the user is alerted. <br> If the form is not valid, the user is prompted to correct any errors.   | Pass  | User is redirected to the home page after successfully editing the pattern. Redirecting to the pattern that has just been edited would be the preferred behaviour for better UX, however due to time constraints, this has not yet been implemented.  |
|Cancel Button  | Once clicked, the action is aborted and the user is redirected back to the pattern list.  |  Pass | Alerts for cancelling actions are expected to be implemented in the future.  |


</details>

<details>
<summary>Delete Pattern Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Delete Pattern Access  | Accessible to the user who created the pattern only.   | Pass  | Tested on a url with the structure of `patterns/<slug>/delete_pattern` while logged in as a user who did not create the pattern, 404 error thrown.<br> 403 error would be preferred, however marking as a pass as the user is still being prevented from completing an unauthorised request.  |
| Delete Pattern Prompt  | Authenticated user who created the patter is prompted to confirm whether or not they want to delete the pattern.   | Pass  |   |
| Delete Button  | Once clicked, the pattern is deleted and the user is alerted.  | Pass  |   |
| Cancel Button  |  Once clicked, the action is aborted and the user is redirected back to the pattern. | Pass  | Action is cancelled however the user is redirected to the pattern list instead of to the pattern page, which was intentional due to time constraints. While it is not the desired behaviour, marking as a pass as the action is cancelled successfully.  |


</details>

<details>
<summary>Edit Comment Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Edit Comment Access  | Accessible to the comment author only.| Pass | Tested on a url with the structure of `patterns/<pk>/edit_comment` while logged in as a user who did not create the comment, 404 error thrown.<br> 403 error would be preferred, however marking as a pass as the user is still being prevented from completing an unauthorised request.   |
| Pre-populated field  | The comment text box is pre-populated with the comment author’s comment.  | Pass  |   |
| Edit pre-populated fields  | The comment text box can be edited.  | Pass  |   |
| Save Button  | Once clicked, the changed are saved and the user is alerted that their comment is pending approval. <br> If the form is not valid, the user is prompted to correct any errors.   |  Pass |   |
| Cancel Button  |  Once clicked, the action is aborted and the user is redirected back to the pattern. | Pass  |   |
| Pending Approval Status  | Once edited, the approved comment is set to not approved so that it can be reviewed by the admin prior to making it public again.  | Pass  |   |

</details>

<details>
<summary>Delete Comment Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Delete Comment Access  | Accessible to the comment author only.  |  Pass | Tested on a url with the structure of `patterns/<pk>/delete_comment` while logged in as a user who did not create the comment, 404 error thrown.<br> 403 error would be preferred, however marking as a pass as the user is still being prevented from completing an unauthorised request.   |
| Delete Button  | Once clicked, the comment is deleted and the user is alerted.  |   |   |
| Cancel Button   | Once clicked, the action is aborted and the user is redirected back to the pattern. | Pass  |   |


</details>

<details>
<summary>Log In Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|  Log In Page Access | Accessible to unauthenticated users only.  | Pass  | Tested with a URL with the structure of `/accounts/login/` while logged out, was redirected to the home page.  |
| Username input  | Username can be added to the text field  | Pass  |   |
| Password Input  | Password can be added to the text field  |  Pass |   |
| Forgot Password Input | Once clicked, the user is redirected to a form that will allow them to reset their password.  | Pass  | The link works as expected, however due to time constraints it has not been configured nor was I able to remove the link from the UI.  |
| Remember Me   | User can click the check box to remember them.   | Pass  |   |
| Log In Button  | If the login credentials are valid, the user is logged in and alerted of the same. <br> If the login credentials are not valid, the user is prompted to correct any errors before proceeding.   | Pass  |   |

</details>

<details>
<summary>Log Out Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Log Out Page Access  | Accessible to authenticated users only.   | Pass  | Tested with a URL with the structure of `/accounts/logout/` while logged in, was redirected to the home page.  |
| Log Out Prompt  | User is prompted to confirm that they want to log out  | Pass  |   |
| Log Out Button   | Once clicked, the user is logged out and alerted of the same.  | Pass  |   |


</details>

<details>
<summary>Sign Up Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Sign Up Page Access  | Accessible to unauthenticated users only.   | Pass  | Tested with a URL with the structure of `/accounts/signup/` while logged in, was redirected to the home page.   |
| Sign Up Benefits  |  Benefits of signing up are displayed to the user. |  Pass |   |
| Log In Prompt  | User is prompted to log in if they already have an account. <br> By clicking the “Log In” link, the user is redirected to the login page.   | Pass  |   |
| Username Input  | Username can be added to the text field  | Pass  |   |
| Password Input  | Password can be added to the text field  |  Pass |   |
| Email Address  | User can provide an optional email address in the text field.  |  Pass |   |
|Password Requirements   | Password requirements are displayed to the user.   | Pass  |   |
| Password Confirm  | User is prompted to confirm their password. <br> This can be added to another textfield.  | Pass  |   |
| Sign Up Button   | If the credentials are valid/password requirements are met, the account is created. The user is logged in and alerted of this. <br> Otherwise, the user is prompted to correct any errors before proceeding. |  Pass | As expected, the user can sign up with or without an email address.  |

</details>

<details>
<summary>Admin Panel</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Admin Panel Access  | Accessible to admins only.  | Pass  | Tested with a URL with the structure of `/admin/` while logged out and while logged in as a normal user, was redirected to the admin sign in page.  |
| Patterns   | Admin can access all patterns from the admin panel.  | Pass  |   |
| Comments  | Admin can access all comments from the admin panel.  | Pass  |   |
|Approve/disapprove comments   | Admin can approve/disapprove comments from the admin panel.  | Pass  |   |
| Delete Comments  | Admin can delete comments from the admin panel.  | Pass  |   |
| Filter comments  | Admin can filter comments by approved status, created date and author.  | Pass  |   |
| Create Crochet Patterns  |  Admin can create crochet patterns from the admin panel. | Pass  |   |
| Update Crochet Patterns  | Admin can update crochet patterns from the admin panel.  | Pass  |   |
| Delete Crochet Patterns  | Admin can update delete patterns from the admin panel.  | Pass  |   |


</details>

<details>
<summary>Error Pages</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| 400.html  | Display template when a 400 error is thrown.  | Pass  |   |
| 403.html  | Display template when a 403 error is thrown.  |  Pass |   |
| 404.html | Display template when a 404 error is thrown.   | Pass  |   |
| 500.html  | Display template when a 500 error is thrown.   | Pass  |   |
| Return to Home links  | When the user clicks “here” to return to the home page, they are redirected to the home page.  | Pass  |   |


</details>

## Bugs

| Feature  |  Issue | Status  | Notes  |
|---|---|---|---|
| Save for Later button  | If the user attempts to unsave a crochet pattern for later, they are brought down to the comment section and prompted to submit their comment. Once a comment is entered and the submit button is clicked, the pattern is unsaved. No comment is registered in the backend. ![Save for Later button bug](documentation/testing/bugs/save-for-later-bug.gif)  | Resolved  | **Root cause:** The if statement was eding outside of the form element. ![Save for Later bug root cause](documentation/testing/bugs/save-for-later-bug-root-cause.PNG) **Fix:** Placed the "endif" statement inside the form element. ![Save for Later button fix](documentation/testing/bugs/save-for-later-bug-fix.PNG) |
| Footer  | Footer was floating in the middle of the page on certain pages  | Resolved  | Expanded the viewport height of the main element on affected pages which resolved the issue  |


## Validator Testing

### HTML

The HTML pages were validated using the [W3 HTML Validation Service](https://validator.w3.org/)

| Screenshot  | Status  |
|---|---|
| ![Home page](documentation/testing/validator-testing/html/html-validated-1.PNG)  |  Passed with no errors |
| ![All Patterns Page](documentation/testing/validator-testing/html/html-validated-11.PNG) | Trailing slashes, since resolved |
| ![Pattern Page](documentation/testing/validator-testing/html/html-validated-12.PNG) | Errors deriving from the summernotes fields, currently unresolved |
| ![Create Pattern Page](documentation/testing/validator-testing/html/html-validated-2.PNG)   | Trailing slash, unresolved as this derives from the summernote field  |
| ![Log In Page](documentation/testing/validator-testing/html/html-validated-3.PNG)  | Passed, no errors  |
| ![Log Out Page](documentation/testing/validator-testing/html/html-validated-4.PNG)  | Passed, no errors  |
| ![Sign Up Page](documentation/testing/validator-testing/html/html-validated-5.PNG)  | Errors deriving from django allauth form, therefore unresolved  |


The pages below were tested via text input due to login being required to access them. 
Django related error messages have been filtered out. 

| Screenshot  | Status  |
|---|---|
| ![My Saved Patterns](documentation/testing/validator-testing/html/html-validated-6.PNG) | Passed with no errors  |
| ![Delete Comment Page](documentation/testing/validator-testing/html/html-validated-7.PNG) | Passed with no errors  |
|![Delete Pattern Page](documentation/testing/validator-testing/html/html-validated-8.PNG) | Passed with no errors  |
|![Edit Comment Page](documentation/testing/validator-testing/html/html-validated-9.PNG) | Passed with no errors  |
|![Edit Pattern Page](documentation/testing/validator-testing/html/html-validated-10.PNG) | Passed with no errors  |



### CSS

The CSS was validated using the [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator) and passed with no errors. 

![CSS validated](documentation/testing/validator-testing/css/css-validated.PNG)

### JavaScript

Both JavaScript functions that were used were validated  using [JSHint](https://jshint.com/). 

|  Function | Screenshot  | Notes  |
|---|---|---|
|  setTimeout() | ![setTimeout() function validated](documentation/testing/validator-testing/javascript/jshint-set-timeout.PNG)  | Passed with no errors  |
| backToTop()  | ![backToTop() function validated](documentation/testing/validator-testing/javascript/jshint-back-to-top.PNG)  | Passed with no errors |

### Python

All Python files were validated via the [CI PEP8 Python Linter](https://pep8ci.herokuapp.com/).

|  File | Screenshot  | Notes  |
|---|---|---|
|  crochetcorner settings.py | ![crochetcorner settings.py file validated](documentation/testing/validator-testing/python/pep8-crochetcorner-settings.PNG)  | Passed with no errors  |
|  crochetcorner urls.py | ![crochetcorner urls.py file validated](documentation/testing/validator-testing/python/pep8-crochetcorner-urls.PNG)  | Passed with no errors  |
| home apps.py  | ![home apps.py file validated](documentation/testing/validator-testing/python/pep8-home-apps.PNG)  | Passed with no errors  |
| home urls.py  | ![home urls.py file validated](documentation/testing/validator-testing/python/pep8-home-urls.PNG)  | Passed with no errors  |
|  home views.py  | ![home views.py file validated](documentation/testing/validator-testing/python/pep8-home-views.PNG)  | Passed with no errors  |
|  patterns admin.py | ![patterns admin.py file validated](documentation/testing/validator-testing/python/pep8-patterns-admin.PNG)  | Passed with no errors  |
|  patterns apps.py  |  ![patterns apps.py file validated](documentation/testing/validator-testing/python/pep8-patterns-apps.PNG) | Passed with no errors  |
|  patterns forms.py | ![patterns forms.py file validated](documentation/testing/validator-testing/python/pep8-patterns-forms.PNG)  |  Passed with no errors |
|  patterns models.py | ![patterns models.py file validated](documentation/testing/validator-testing/python/pep8-patterns-models.PNG)  | Passed with no errors  |
| patterns urls.py   | ![patterns urls.py file validated](documentation/testing/validator-testing/python/pep8-patterns-urls.PNG)  | Passed with no errors  |
| patterns views.py   | ![patterns views.py file validated](documentation/testing/validator-testing/python/pep8-patterns-views.PNG) | Passed with no errors  |




[Back to the top](#testing--the-crochet-corner)
<br>
[Return to README.md](README.md)
