'use strict';
/*
This function validates user input fields;
turns the field yellow if the validation is violated
as the user fills it in, displays a warning message next
to the field if the input is invalid, and displays a
status bar heading of 'success' or 'error' once the user
submits the form.
*/


function validator(boxName) {

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

  function createError(boxName) {
    // creates error message if input is not valid
    var errorMsg = $('<div/>', {
      'class': 'error',
      'text': 'Error: input not valid.',
    });
    $('#' + boxName).after(errorMsg);
  }


  function createValid(boxName) {
    // removes error message if textbox is valid
    $('.error').remove();
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
  }
  if (strValid === false) {
    createError(boxName);
  } else {
    createValid(boxName);
  }
}


$(document).ready(function() {
  $('#user-name-box').change(function() {
    validator('user-name-box');
  });
  $('#dob-box').change(function() {
    validator('dob-box');
  });
  $('#phone-box').change(function() {
    validator('phone-box');
  });
});
