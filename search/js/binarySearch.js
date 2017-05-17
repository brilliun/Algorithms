function binarySearch (pArray, pTarget) {
	if (pArray.length <= 0 || pArray[0] > pTarget || pArray[pArray.length - 1] < pTarget) {
		return -1;
	}

	return _subSearch(pArray, pTarget, 0, pArray.length - 1);
}

function _subSearch (pArray, pTarget, pFrom, pTo) {
	if (pFrom > pTo) {
		return -1;
	}

	var tMid = pFrom + Math.floor((pTo - pFrom) / 2);

	if (pArray[tMid] > pTarget) {
		return _subSearch(pArray, pTarget, pFrom, tMid - 1);
	} else if (pArray[tMid] < pTarget) {
		return _subSearch(pArray, pTarget, tMid + 1, pTo);
	} else {
		return tMid;
	}
}


console.log(binarySearch([1, 2, 3, 4, 5], 3));
console.log(binarySearch([1, 2, 3, 4, 5], 1));
console.log(binarySearch([1, 2, 3, 4, 5], 5));
console.log(binarySearch([1, 2, 3, 4, 5, 6], 2));