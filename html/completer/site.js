'use strict';

function Completer() {
  this.completerArray = [];

  this.addCompletion = function(str) {
    this.completerArray.push(str);
    this.selectCompletion(str);
  };

  this.removeCompletion = function(str) {
    var removeIndex = this.completerArray.indexOf(str);
    if (removeIndex > -1) {
      var removedArray = this.completerArray.splice(removeIndex, 1);
      return this.completerArray;
    }
    if (!(this.itemToWeight === 'undefined')) {
      this.itemToWeight.delete(str);
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

  this.selectCompletion = function(str) {
    if (typeof this.itemToWeight === 'undefined') {
      this.itemToWeight = {}
      this.itemToWeight[str] = 0;
    } else if (!(str in this.itemToWeight)) {
      this.itemToWeight[str] = 0;
    } else {
      this.itemToWeight[str] += 1;
    }
  };
}


var fruitCompleter = new Completer();
fruitCompleter.addCompletion('apple');
fruitCompleter.addCompletion('avocado');
fruitCompleter.addCompletion('apricot');
fruitCompleter.addCompletion('blueberry');

fruitCompleter.complete('a');
fruitCompleter.complete('b');
