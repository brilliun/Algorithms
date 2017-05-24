function isPalindrome (pString) {
	if (typeof pString !== 'string') {
		return null;
	}

	var tLength = pString.length;

	if (tLength === 0) {
		return false;
	}

	for (var i = 0, il = Math.floor(tLength / 2); i < il; i++) {
		if (pString[i] !== pString[tLength - 1 - i]) {
			return false;
		}
	}

	return true;
}