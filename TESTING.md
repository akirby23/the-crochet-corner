# Testing | The Crochet Corner

[Return to README.md](README.md)

## Table of Contents

- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
- [Validator Testing](#validator-testing)

## Manual Testing

<details>
<summary>Home Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>All Patterns Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
| Create New Pattern button  |  This button should only be visible to users who are logged in. Once clicked, the user should be redirected to a form that will allow them to create a new crochet pattern. |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>My Saved Patterns Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>Pattern Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>Create Pattern Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>Edit Pattern Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>Delete Pattern Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>Edit Comment Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>Delete Comment Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>Log In Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>Log Out Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

<details>
<summary>Sign Up Page</summary>

| Feature  | Expected Behaviour  | Status  |  Notes |  
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |

</details>

## Bugs

| Feature  |  Issue | Status  | Notes  |
|---|---|---|---|
| Save for Later button  | If the user attempts to unsave a crochet pattern for later, they are brought down to the comment section and prompted to submit their comment. Once a comment is entered and the submit button is clicked, the pattern is unsaved. No comment is registered in the backend. ![Save for Later button bug](documentation/testing/bugs/save-for-later-bug.gif)  | Resolved  | **Root cause:** The if statement was eding outside of the form element. ![Save for Later bug root cause](documentation/testing/bugs/save-for-later-bug-root-cause.PNG) **Fix:** Placed the "endif" statement inside the form element. ![Save for Later button fix](documentation/testing/bugs/save-for-later-bug-fix.PNG)
 |
|   |   |   |   |
|   |   |   |   |

## Validator Testing


[Back to the top](#testing--the-crochet-corner)
<br>
[Return to README.md](README.md)
