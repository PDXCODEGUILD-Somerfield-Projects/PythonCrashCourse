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
  24: 'Y', 25: 'Z', ' ': null
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

/* This function 'decrypts' a string
into Caesar cipher. It takes in encStr,
transforms it to its numeric represention of
the alphabet, subtracts the input cipher key to
the numbers and transforms the translated
numbers back into a string --returning a
'decrypted' string.*/
function caesarDecrypt(encStr, key) {
  var encStrUpper = encStr.toUpperCase();
  var numberArray = [];
  for (var i = 0; i < encStrUpper.length; i += 1) {
    var letter = encStrUpper.charAt(i);
    numberArray.push(letterToNumber[letter]);
  }
  var decryptedNumberArray = [];
  var newNum = null;
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
  for (var i = 0; i < decryptedNumberArray.length; i += 1) {
    var decryptedNumber = decryptedNumberArray[i];
    var decryptedLetter = _.findKey(letterToNumber,
      _.partial(_.isEqual, decryptedNumber));
    decryptedStr += decryptedLetter;
  }
  return decryptedStr;
}

function DecryptSansKey(encStr) {
  var strletterToFrequency = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
    'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
    'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
    'Y': 0, 'Z': 0
  };
  var encStrUpper = encStr.toUpperCase();
  var strSpaces = 0;
  for (var i = 0; i < encStrUpper.length; i += 1) {
    var letter = encStrUpper.charAt(i);
    if (!(letter === ' ')) {
      strletterToFrequency[letter] = strletterToFrequency[letter] + 1;
    } else {
      strSpaces += 1;
    }
  }
  var bestShift = [];
  for (var lf = 0; lf < encStrUpper.length; lf += 1) {
    var strLetter = encStrUpper[lf];
    var ltrLength = encStrUpper.length - strSpaces;
    var leastChi = 0;
    var chiShift = null;
    var observed = strletterToFrequency[strLetter];
    if (!(strLetter === ' ')) {
      for (var s = 0; s < 26; s += 1) {
        var shiftLetter = NumberToLetter[s];
        var expected = letterToFrequency[shiftLetter] / 1000 * ltrLength;
        var residual = observed - expected;
        var squaredResidual = Math.pow(residual, 2);
        var component = squaredResidual / expected;
        if (s === 0) {
          leastChi = component;
          if (s > letterToNumber[strLetter]) {
            chiShift = s - letterToNumber[strLetter];
          } else {
            chiShift = s + 26 - letterToNumber[strLetter];
          }
        } else if (component < leastChi) {
          leastChi = component;
          if (s > letterToNumber[strLetter]) {
            chiShift = s - letterToNumber[strLetter];
          } else {
            chiShift = s + 26 - letterToNumber[strLetter];
          }
        }
      }
      bestShift.push(chiShift);
    }
  }
  bestShift.sort();
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
