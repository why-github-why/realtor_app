/* When updating js or css files, remember to run PYTHON MANAGE.PY COLLECTSTATIC */

/* Update year in footer */
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

/* Fade out error message after 5000 milliseconds */ 
setTimeout(function() {
   $('#message').fadeOut('slow');
}, 5000);
