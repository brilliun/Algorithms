function shellSort(pArray) {
  var N = pArray.length;
  var tRound = 1;
  var tShell = 1;
  var tCurrent;
  var j;

  while (tShell < N/3) tShell = 3 * tShell + 1;

  while (tShell >= 1) {

    for (var i = tShell; i < N; i++) {
      tCurrent = pArray[i];

      for (j = i - tShell; j >= 0; j -= tShell) {
        if (tCurrent < pArray[j]) {
          pArray[j + tShell] = pArray[j];
        } else {
          break;
        }
      }

      if (j + tShell !== i) {
        pArray[j + tShell] = tCurrent;
      }
    }

    tShell = Math.floor(tShell / 3);
  }

  return pArray;
}

function test() {
  var assert = require('assert');
  assert.deepStrictEqual(shellSort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6]);
  assert.deepStrictEqual(shellSort([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6]);
  assert.deepStrictEqual(shellSort([6, 3, 1, 2, 5, 4]), [1, 2, 3, 4, 5, 6]);
  assert.deepStrictEqual(shellSort([1, 3, 5, 2, 4, 6]), [1, 2, 3, 4, 5, 6]);
  assert.deepStrictEqual(shellSort([6]), [6]);
  assert.deepStrictEqual(shellSort([5, 2, 1, 2, 5, 4, 1]), [1, 1, 2, 2, 4, 5, 5]);

  assert.deepStrictEqual(shellSort([3, 12, 4, 9, 2, 4]), [2, 3, 4, 4, 9, 12]);
  assert.deepStrictEqual(shellSort([]), []);
  assert.deepStrictEqual(shellSort([4, 5]), [4, 5]);
  assert.deepStrictEqual(shellSort([4, 3]), [3, 4]);
  assert.deepStrictEqual(shellSort([5, 2, 4, 6, 1, 3]), [1, 2, 3, 4, 5, 6]);

  var random;

  for (var size = 5; size <= 20; size = size * 2) {
    random = generateRandomArray(size, size);
    console.log('Random array: ' + JSON.stringify(random));
    assert.deepStrictEqual(shellSort(random.slice()), random.sort(function(a, b) {
      return a - b;
    }));    
  }

  console.log('All tests passed');
}

function generateRandomArray(pSize, pMax) {
  var tResult = new Array(pSize);

  for (var i = 0; i < pSize; i++) {
    tResult[i] = Math.floor(pMax * Math.random());
  }

  return tResult;
}

test();