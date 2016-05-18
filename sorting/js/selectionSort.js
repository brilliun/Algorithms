function selectionSort(pArray) {
  var tMin, tMinIndex;
  var tLength = pArray.length;
  var j;

  for (var i = 0; i < tLength - 1; i++) {
    tMin = Infinity;

    for (j = i; j < tLength; j++) {
      if (pArray[j] < tMin) {
        tMin = pArray[j];
        tMinIndex = j;
      }
    }

    _swap(pArray, i, tMinIndex);
  }

  return pArray;
}


function _swap(pArray, a, b) {
  if (a !== b) {
    var tTemp = pArray[a];
    pArray[a] = pArray[b];
    pArray[b] = tTemp;
  }
}

function test(pInPlace) {
  var assert = require('assert');
  assert.deepStrictEqual(selectionSort([1, 2, 3, 4, 5, 6], pInPlace), [1, 2, 3, 4, 5, 6]);
  assert.deepStrictEqual(selectionSort([6, 5, 4, 3, 2, 1], pInPlace), [1, 2, 3, 4, 5, 6]);
  assert.deepStrictEqual(selectionSort([6, 3, 1, 2, 5, 4], pInPlace), [1, 2, 3, 4, 5, 6]);
  assert.deepStrictEqual(selectionSort([1, 3, 5, 2, 4, 6], pInPlace), [1, 2, 3, 4, 5, 6]);
  assert.deepStrictEqual(selectionSort([6], pInPlace), [6]);
  assert.deepStrictEqual(selectionSort([5, 2, 1, 2, 5, 4, 1], pInPlace), [1, 1, 2, 2, 4, 5, 5]);

  assert.deepStrictEqual(selectionSort([3, 12, 4, 9, 2, 4], pInPlace), [2, 3, 4, 4, 9, 12]);
  assert.deepStrictEqual(selectionSort([], pInPlace), []);
  assert.deepStrictEqual(selectionSort([4, 5], pInPlace), [4, 5]);
  assert.deepStrictEqual(selectionSort([4, 3], pInPlace), [3, 4]);
  assert.deepStrictEqual(selectionSort([5, 2, 4, 6, 1, 3], pInPlace), [1, 2, 3, 4, 5, 6]);

  console.log('Tests passed for InPlace: ' + pInPlace);
}

test(true);
