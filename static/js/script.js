/**
 * Times out the alerts after 3 seconds.
 * Code borrowed from Code Institute's "I Think Therefore I Blog"
 * walkthrough tutorial.
 */
setTimeout(function () {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();
}, 3000);
