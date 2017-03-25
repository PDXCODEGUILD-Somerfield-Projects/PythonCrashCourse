'use strict';

function Completer() {
  this.completerArray = [];

  this.addCompletion = function(str) {
    this.completerArray.push(str);
  };

  this.removeCompletion = function(str) {
    var removeIndex = this.completerArray.indexOf(str);
    if (removeIndex > -1) {
      var removedArray = this.completerArray.splice(removeIndex, 1);
      return this.completerArray;
    }
  };

  this.complete = function(prefix) {
    function checkItem(item) {
      return item.startsWith(prefix);
    }
    var checkArray = this.completerArray.filter(checkItem);
    console.log(checkArray);
    return this.checkArray;
  };
}


var fruitCompleter = new Completer();
fruitCompleter.addCompletion('apple');
fruitCompleter.addCompletion('avocado');
fruitCompleter.addCompletion('apricot');
fruitCompleter.addCompletion('blueberry');

fruitCompleter.complete('a');
fruitCompleter.complete('b');
