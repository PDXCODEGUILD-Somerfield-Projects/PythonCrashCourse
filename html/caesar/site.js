'use strict';

var letterToNumber = {
  'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
  'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
  'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
  'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
  'Y': 24, 'Z': 25, ' ': null
};

var NumberToLetter = {
  0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F',
  6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
  12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
  18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
  24: 'Y', 25: 'Z', null: ' '
};

var letterToFrequency = {
  'A': 73, 'B': 9, 'C': 30, 'D': 44, 'E': 130, 'F': 28,
  'G': 16, 'H': 35, 'I': 74, 'J': 2, 'K': 3, 'L': 35,
  'M': 25, 'N': 78, 'O': 74, 'P': 27, 'Q': 3, 'R': 77,
  'S': 63, 'T': 93, 'U': 27, 'V': 13, 'W': 16, 'X': 5,
  'Y': 19, 'Z': 1
};

/* This function 'encrypts' a string
into Caesar cipher. It takes in plainStr,
transforms it to a numeric represention
(A = 0, B = 1, etc), adds the cipher key to
each number and transforms the translated
numbers back into a string --returning an
'encrypted' string.

Input string can only contain letters and spaces;
the input key is an integer*/
function caesarEncrypt(plainStr, key) {
  // changes string to uppercase letters
  var plainStrUpper = plainStr.toUpperCase();
  var numberArray = [];
  // loops through the string and creates an array of
  // corresponding numbers
  for (var i = 0; i < plainStrUpper.length; i += 1) {
    var letter = plainStrUpper.charAt(i);
    numberArray.push(letterToNumber[letter]);
  }
  var encryptedNumberArray = [];
  var newNum = null;
  // loops through the array of numbers and adds key to
  // each number, creating an encryption set
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
  // loops through the 'encryption' numbers and creates a
  // new encrypted string for output
  for (var i = 0; i < encryptedNumberArray.length; i += 1) {
    var encryptedNumber = encryptedNumberArray[i];
    var encryptedLetter = NumberToLetter[encryptedNumber];
    /*
    ** alternative way to pull key with one dict object:
    var encryptedLetter = _.findKey(letterToNumber,
      _.partial(_.isEqual, encryptedNumber));
    */
    encryptedStr += encryptedLetter;
  }
  return encryptedStr;
}

/* This function 'decrypts' a string
into Caesar cipher. It takes in an encoded string,
transforms it to its numeric represention
(A = 0, B = 1, etc.), subtracts the cipher key from
each number and transforms the translated
numbers back into a string --returning a
'decrypted' string.

Takes in string as letters, spaces only;
takes in key as an integer */
function caesarDecrypt(encStr, key) {
  // changes string to upper case letters
  var encStrUpper = encStr.toUpperCase();
  var numberArray = [];
  /*
  loops through the string, changing each letter
  to its numeric represention and creates a
  number array
  */
  for (var i = 0; i < encStrUpper.length; i += 1) {
    var letter = encStrUpper.charAt(i);
    numberArray.push(letterToNumber[letter]);
  }
  var decryptedNumberArray = [];
  var newNum = null;
  /*
  loops through the number array and subtracts the key
  from each number, creating a new 'decrypted' number array
  */
  for (var i = 0; i < numberArray.length; i += 1) {
    var number = numberArray[i];
    if (number === null) {
      newNum = null;
    } else {
      newNum = number - key;
    }
    if (newNum < 0) {
      newNum = newNum + 25;
    } else {
      newNum = newNum;
    }
    decryptedNumberArray.push(newNum);
  }
  var decryptedStr = '';
  // transforms the number array into the decrypted string
  for (var i = 0; i < decryptedNumberArray.length; i += 1) {
    var decryptedNumber = decryptedNumberArray[i];
    var decryptedLetter = _.findKey(letterToNumber,
      _.partial(_.isEqual, decryptedNumber));
    decryptedStr += decryptedLetter;
  }
  return decryptedStr;
}

function decryptSansKey(encStr) {
  // a dict object to save the frequency of each letter in the string
  var strletterToFrequency = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
    'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
    'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
    'Y': 0, 'Z': 0
  };

    /*
    function to calculate chi squared based on instructions from
    http://www.statisticshowto.com/what-is-a-chi-square-statistic/
    runs through all of the letters of the alphabet and finds the
    corresponding letter with the lowest chi square statistic,
    returning the 'shift' number to that letter
    */
  function chiCalc(encStrUpper) {
    // gets the observed frequency of the current letter
    var observed = strletterToFrequency[encStrUpper];
    // resets the values to track chi and shift
    var leastChi = 0;
    var chiShift = null;
    // calculates the corresponding chi squared statistic for each
    // letter of the alphabet
    for (var alpha = 0; alpha < 26; alpha += 1) {
      var shiftLetter = NumberToLetter[alpha];
      var expected = letterToFrequency[shiftLetter] / 1000 * encLength;
      var residualSquared = Math.pow(observed - expected, 2);
      var component = residualSquared / expected;
        // saves the lowest chi score and corresponding shift
      if (alpha === 0) {
        leastChi = component;
        if (alpha < letterToNumber[encStrUpper]) {
          chiShift = letterToNumber[encStrUpper] - alpha;
        } else {
          chiShift = letterToNumber[encStrUpper] + 26 - alpha;
        }
      } else if (component < leastChi) {
        leastChi = component;
        if (alpha < letterToNumber[encStrUpper]) {
          chiShift = letterToNumber[encStrUpper] - alpha;
        } else {
          chiShift = letterToNumber[encStrUpper] + 26 - alpha;
        }
      }

    }
    // returns the shift number for the letter with the lowest chi score
    return chiShift;
  }

  var encStrUpper = encStr.toUpperCase();
  var strSpaces = 0;
  // runs through the string to calculate frequency of each letter
  for (var i = 0; i < encStrUpper.length; i += 1) {
    var letter = encStrUpper.charAt(i);
    if (!(letter === ' ')) {
      strletterToFrequency[letter] = strletterToFrequency[letter] + 1;
    } else {
      // also counts the number of spaces in the string
      strSpaces += 1;
    }
  }
  //length of string without spaces
  var encLength = encStrUpper.length - strSpaces;
  var bestShift = [];
  // runs through each letter in the string
  for (var i = 0; i < encStrUpper.length; i += 1) {
    var strLetter = encStrUpper[i];
    // runs the chiCalc function on anything that's not a space in the string
    if (!(strLetter === ' ')) {
      var chiShift = chiCalc(strLetter);
      /*
      saves an array of the lowest chi shift result for each
      letter in the string
      */
      bestShift.push(chiShift);
    }
  }
  // sorts the array to consolidate values
  bestShift.sort();
  /*
  runs through the array to find the shift with the highest
  frequency in the array
  */
  var bestShiftFreq = 0;
  var bestOfBest = 0;
  for (var i = 0; i < bestShift.length; i += 1) {
    if (i === 0) {
      var val = bestShift[i];
      var freq = 1;
      bestShiftFreq = 1;
      bestOfBest = val;
    } else if (bestShift[i] === val) {
      freq += 1;
    } else {
      if (freq > bestShiftFreq) {
        bestShiftFreq = freq;
        bestOfBest = val;
        val = bestShift[i];
        freq = 1;
      } else {
        val = bestShift[i];
        freq = 1;
      }
    }
  }
  console.log('Most frequent shift = ' + bestOfBest);
  console.log('Frequency = ' + bestShiftFreq);
  var decryptedStr = caesarDecrypt(encStr, bestOfBest);
  console.log(decryptedStr);
}
