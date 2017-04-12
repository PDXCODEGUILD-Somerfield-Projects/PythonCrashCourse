'use strict';

/*
This function validates user input fields;
turns the field yellow if the validation is violated
as the user fills it in, displays a warning message next
to the field if the input is invalid, and displays a
status bar heading of 'success' or 'error' once the user
submits the form.
*/
function validator(boxName, check) {

  // uses Reg Ex to check user input for 'word'(space)'word' format
  function checkName(str) {
    var valid = /[A-Za-z]* [A-Za-z]*/.test(str);
    return valid;
  }

  // uses Reg Ex to check user input for YYYY-MM-DD format
  function checkDob(str) {
    var valid = /\d{4}-\d\d-\d\d/.test(str);
    return valid;
  }

  // uses Reg Ex to check user input for 555-555-5555 format
  function checkPhone(str) {
    var valid = /\d{3}-\d{3}-\d{4}/.test(str);
    return valid;
  }

  function createWarningMsg(boxName) {
    // creates error message if input is not valid
    var errorMsg = $('<div/>', {
      'class': 'warning-text',
      'text': 'Error: input not valid.',
    });
    $('#' + boxName).after(errorMsg);
  }

  function createValid(boxName) {
    // removes error message if textbox is valid
    $('.warning-text').remove();
  }

  function createWarningField(boxName) {
    // adds warning class to the text box element
    $('#' + boxName).addClass('warning');
  }

  function removeWarningField(boxName) {
    $('#' + boxName).removeClass('warning');
  }

  //picks the validation function to run based on the textbox ID
  if (boxName === 'user-name-box') {
    var nameStr = $('#user-name-box').val();
    var strValid = checkName(nameStr);
  } else if (boxName === 'dob-box') {
    var dobStr = $('#dob-box').val();
    var strValid = checkDob(dobStr);
  } else if (boxName === 'phone-box') {
    var phoneStr = $('#phone-box').val();
    var strValid = checkPhone(phoneStr);
    /*
    To decide whether the status bar should show success or
    error, all of the field boxes are validated. If they all
    return 'true', the status bar updates a 'success' message; if
    any return 'false', the status bar updates an 'error' message.
    */
  } else if (boxName === 'status-bar') {
    var nameStr = $('#user-name-box').val();
    var nameStrValid = checkName(nameStr);
    var dobStr = $('#dob-box').val();
    var dobStrValid = checkDob(dobStr);
    var phoneStr = $('#phone-box').val();
    var phoneStrValid = checkPhone(phoneStr);
    if (nameStrValid === true &&
      dobStrValid === true &&
      phoneStrValid === true) {
      $('#status-bar').removeClass('error');
      $('#status-bar').addClass('valid');
      $('#status-bar').html('<h3>SUCCESS: Input is valid!</h3>');
    } else {
      $('#status-bar').removeClass('valid');
      $('#status-bar').addClass('error');
      $('#status-bar').html('<h3>ERROR: Input not valid!</h3>');
    }
  }

  /* Identifies whether the user input matches the valid format
  and runs the appropriate 'warning' function to change the field
  color, create an error message warning, or remove a warning */
  if (strValid === false && check === 'box-change') {
    createWarningMsg(boxName);
  } else if (strValid === true && check === 'box-change') {
    createValid(boxName);
  } else if (strValid === false && check === 'key-change') {
    createWarningField(boxName);
  } else {
    removeWarningField(boxName);
  }
}

/*
Looks for updates or changes in the text fields
and button click to run validator function
*/
$(document).ready(function() {
  $('#user-name-box').keyup(function() {
    validator('user-name-box', 'key-change');
  });
  $('#user-name-box').change(function() {
    validator('user-name-box', 'box-change');
  });
  $('#dob-box').keyup(function() {
    validator('dob-box', 'key-change');
  });
  $('#dob-box').change(function() {
    validator('dob-box', 'box-change');
  });
  $('#phone-box').keyup(function() {
    validator('phone-box', 'key-change');
  });
  $('#phone-box').change(function() {
    validator('phone-box', 'box-change');
  });
  // on submit button click, the status bar is added to html
  $(':button').on('click', function(event) {
    event.preventDefault();
    var statusBar = $('<header id="status-bar"></header>');
    $('.form').before(statusBar);
    validator('status-bar', 'submit');
  });
});
