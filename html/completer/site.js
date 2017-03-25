'use strict';

/*
Completer functions like an auto-complete.
It creates a list of input items and the more
times an item is selected from the list, the higher
that item is weighted in the selection list.
*/
function Completer() {
  this.completerArray = [];
  // adds an item to the Completer list
  this.addCompletion = function(str) {
    this.completerArray.push(str);
    this.selectCompletion(str);
  };
  // locates item in the list and removes it
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
  // creates a suggestion list based on users' first letter(s)
  this.complete = function(prefix) {
    function checkItem(item) {
      return item.startsWith(prefix);
    }
    var checkArray = this.itemsSortedByWeight.filter(checkItem);
    console.log(checkArray);
    return this.checkArray;
  };
  /* adds weight to items at each selection in a dict object,
  creates a dynamic array that returns items in a sorted order
  from most to least weighted
  */
  this.selectCompletion = function(str) {
    if (typeof this.itemToWeight === 'undefined') {
      this.itemToWeight = {};
      this.itemToWeight[str] = 0;
    } else if (!(str in this.itemToWeight)) {
      this.itemToWeight[str] = 0;
    } else {
      this.itemToWeight[str] += 1;
    }
    this.itemsSortedByWeight = [];
    var itemToWeight = this.itemToWeight;
    // re-shuffles the array based on item weight
    this.itemsSortedByWeight =
      Object.keys(itemToWeight).sort(function(a, b) {
        return itemToWeight[b] - itemToWeight[a];
      }
    );
    return this.itemsSortedByWeight;
  };
}


var fruitCompleter = new Completer();
fruitCompleter.addCompletion('apple');
fruitCompleter.addCompletion('anise');
fruitCompleter.addCompletion('avocado');
fruitCompleter.addCompletion('apricot');
fruitCompleter.addCompletion('blueberry');

fruitCompleter.complete('a');
fruitCompleter.complete('b');

fruitCompleter.selectCompletion('avocado');
fruitCompleter.selectCompletion('avocado');

fruitCompleter.complete('a')
