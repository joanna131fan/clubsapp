//updated javascript
//dropdown sidebar
var dropdown = document.getElementsByClassName("nav-link dropdown-toggle");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

window.addEventListener("load", function () {
  function sendData() {
    var XHR = new XMLHttpRequest();

    // Bind the FormData object and the form element
    var FD = new FormData(form);

    // Define what happens on successful data submission
    XHR.addEventListener("load", function(event) {
      alert(event.target.responseText);
    });

    // Define what happens in case of error
    XHR.addEventListener("error", function(event) {
      alert('Oops! Something went wrong.');
    });

    // Set up our request
    XHR.open("POST", "https://example.com/init.py");

    // The data sent is what the user provided in the form
    XHR.send(FD);
  }
 
  // Access the form element...
  var form = document.getElementById("myForm");

  // ...and take over its submit event.
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    sendData();
  });

});
//form validation
var filledin=true;

function showFormData(oForm) {
  var msg = "FORM IS INCOMPLETE:\n";

  for (i = 1; i < oForm.length, oForm.elements[i].getAttribute("type") !=='submit'; i++) {
    var pat = oForm.elements[i].pattern;

    if(oForm.elements[i].value == null || oForm.elements[i].value == '' || !pat.test(oForm.elements[i].value)) {
      msg += oForm.elements[i].id + "\n";
      filledin=false;
    }
  }
  if(filledin == false){
    alert(msg);
  }
  else {
    location.href="home.html";
    document.onloadend = alert('Thank You For Registering!');
  }
}

function redirecthome(oForm) {
  for (i = 1; i < oForm.length, oForm.elements[i].getAttribute("type") !== "submit"; i++) {
    //var pat = oForm.elements[i].pattern;

    if(oForm.elements[i].value == null || oForm.elements[i].value == '' ) {
      filledin=false;
    }
  }
  if(filledin==true){
    location.href="home.html";
    alert('Thank You For Registering!');
  }
  else {
    alert('Form Not Complete Correctly')
  }
}

//displaying username input: https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_form_elements_item