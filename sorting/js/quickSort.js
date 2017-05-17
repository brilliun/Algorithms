function quickSort(pInput) {
  _subsort(pInput, 0, pInput.length - 1);

  return pInput;
}

function _subsort(pInput, pLow, pHigh) {
  if (pHigh <= pLow) {
    return;
  }

  var tPivot = _partition(pInput, pLow, pHigh);

  _subsort(pInput, pLow, tPivot - 1);
  _subsort(pInput, tPivot + 1, pHigh);
}


function _partition(pInput, pLow, pHigh) {
  var tDivision = pInput[pLow];
  var l = pLow + 1, r = pHigh;

  while (true) {
    while (l <= pHigh && pInput[l] <= tDivision) {
      l++;
    }

    while (r > pLow && pInput[r] >= tDivision) {
      r--;
    }

    if (l < r) {
      _swap(pInput, l, r);
    } else {
      break;
    }
  }

  if (r !== pLow) {
    _swap(pInput, r, pLow);    
  }

  return r;

}

function _swap(pInput, a, b) {
  var temp = pInput[a];

  pInput[a] = pInput[b];
  pInput[b] = temp;
}


function test() {
  arrayEqual(quickSort([5, 3, 3, 8, 4]), [3, 3, 4, 5, 8]);
  arrayEqual(quickSort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6]);
  arrayEqual(quickSort([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6]);
  arrayEqual(quickSort([1, 3, 5, 2, 4, 6]), [1, 2, 3, 4, 5, 6]);
  arrayEqual(quickSort([6]), [6]);
  arrayEqual(quickSort([]), []);
  arrayEqual(quickSort([4, 5]), [4, 5]);
  arrayEqual(quickSort([4, 3]), [3, 4]);

  var random;

  for (var size = 5; size <= 20; size = size * 2) {
    random = generateRandomArray(size, size + 5);
    console.log('Random array: ' + JSON.stringify(random));
    arrayEqual(quickSort(random.slice()), random.sort(function(a, b) {
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