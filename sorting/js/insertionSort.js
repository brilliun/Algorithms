function insertionSort(pArray, pInPlace) {
	if (pInPlace === true) {
		return _insertionInPlace(pArray);
	} else {
  	return _insertionNew(pArray);
	}
}

function _insertionInPlace(pArray) {
	var tCurrent, tCompare;
	var j;

	for (var i = 0, il = pArray.length; i < il; i++) {
		tCurrent = pArray[i];

		for (j = i - 1; j >= 0; j--) {
			tCompare = pArray[j];

			if (tCurrent < pArray[j]) {
				pArray[j + 1] = tCompare;
			} else {
				break;
			}
		}

		if (i !== j + 1) {
			pArray[j + 1] = tCurrent;
		}
	}

	return pArray;
}

function _insertionNew(pArray) {
	var tResult = [];
	var tCurrent;
	var tPosition;
	var j;

	for (var i = 0, il = pArray.length; i < il; i++) {
		tCurrent = pArray[i];
		tPosition = 0;

		for (j = i - 1; j >= 0; j--) {
			if (tCurrent >= tResult[j]) {
				tPosition = j + 1;
				break;
			}
		}

		tResult.splice(tPosition, 0, tCurrent);

	}

	return tResult;
}


function test(pInPlace) {
	var assert = require('assert');
	assert.deepStrictEqual(insertionSort([1, 2, 3, 4, 5, 6], pInPlace), [1, 2, 3, 4, 5, 6]);
	assert.deepStrictEqual(insertionSort([6, 5, 4, 3, 2, 1], pInPlace), [1, 2, 3, 4, 5, 6]);
	assert.deepStrictEqual(insertionSort([6, 3, 1, 2, 5, 4], pInPlace), [1, 2, 3, 4, 5, 6]);
	assert.deepStrictEqual(insertionSort([1, 3, 5, 2, 4, 6], pInPlace), [1, 2, 3, 4, 5, 6]);
	assert.deepStrictEqual(insertionSort([6], pInPlace), [6]);
	assert.deepStrictEqual(insertionSort([5, 2, 1, 2, 5, 4, 1], pInPlace), [1, 1, 2, 2, 4, 5, 5]);

	assert.deepStrictEqual(insertionSort([3, 12, 4, 9, 2, 4], pInPlace), [2, 3, 4, 4, 9, 12]);
	assert.deepStrictEqual(insertionSort([], pInPlace), []);
	assert.deepStrictEqual(insertionSort([4, 5], pInPlace), [4, 5]);
	assert.deepStrictEqual(insertionSort([4, 3], pInPlace), [3, 4]);
	assert.deepStrictEqual(insertionSort([5, 2, 4, 6, 1, 3], pInPlace), [1, 2, 3, 4, 5, 6]);

	console.log('Tests passed for InPlace: ' + pInPlace);
}

test(true);
test(false);

