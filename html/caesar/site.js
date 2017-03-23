'use strict';

var letterToNumber = {
  'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
  'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
  'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
  'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
  'Y': 24, 'Z': 25, ' ': null
};



/* This function 'encrypts' a string
into Caesar cipher. It takes in plainStr,
transforms it to a numeric represention of
the alphabet, adds the input cipher key to
the numbers and transforms the translated
numbers back into a string --returning an
'encrypted' string.*/
function caesarEncrypt(plainStr, key) {
  var plainStrUpper = plainStr.toUpperCase();
  var numberArray = [];
  for (var i = 0; i < plainStrUpper.length; i += 1) {
    var letter = plainStrUpper.charAt(i);
    numberArray.push(letterToNumber[letter]);
  }
  var encryptedNumberArray = [];
  var newNum = null;
  for (var i = 0; i < numberArray.length; i += 1) {
    var number = numberArray[i];
    if (number === null) {
      newNum = null;
    } else {
      newNum = number + key;
    }
    if (newNum > 25) {
      newNum = newNum - 25;
    } else {
      newNum = newNum;
    }
    encryptedNumberArray.push(newNum);
  }
  var encryptedStr = '';
  for (var i = 0; i < encryptedNumberArray.length; i += 1) {
    var encryptedNumber = encryptedNumberArray[i];
    var encryptedLetter = _.findKey(letterToNumber,
      _.partial(_.isEqual, encryptedNumber));
    encryptedStr += encryptedLetter;
  }
  return encryptedStr;
}
