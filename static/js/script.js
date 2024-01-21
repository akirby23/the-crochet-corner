/**
 * Times out the alerts after 3 seconds.
 * Code borrowed from Code Institute's "I Think Therefore I Blog"
 * walkthrough project.
 */
setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);


/**
 * Once called, the user is brought back to the 
 * top of the page.
 */
backToTop = () => {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
};


