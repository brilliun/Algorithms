def quickSort(pInput):
    _sort(pInput, 0, len(pInput) - 1)

    return pInput


def _sort(pInput, pLow, pHigh):
    if pHigh <= pLow:
        return

    tPivot = _partition(pInput, pLow, pHigh)
    _sort(pInput, pLow, tPivot - 1)
    _sort(pInput, tPivot + 1, pHigh)

    return


def _partition(pInput, pLow, pHigh):
    tDivision = pInput[pLow]
    l, r = pLow + 1, pHigh

    while True:
        while l <= pHigh and pInput[l] <= tDivision:
            l = l + 1
        while r > pLow and pInput[r] >= tDivision:
            r = r - 1

        if l < r:
            pInput[l], pInput[r] = pInput[r], pInput[l]
        else:
            break

    if r != pLow:
        pInput[r], pInput[pLow] = pInput[pLow], pInput[r]

    return r


import unittest
import random


class TestSort(unittest.TestCase):
    def _tests(self):
        self.assertEqual(quickSort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(quickSort([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(quickSort([6, 3, 1, 2, 5, 4]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(quickSort([1, 3, 5, 2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(quickSort([6]), [6])
        self.assertEqual(quickSort([5, 2, 1, 2, 5, 4, 1]), [1, 1, 2, 2, 4, 5, 5])

        self.assertEqual(quickSort([3, 12, 4, 9, 2, 4]), [2, 3, 4, 4, 9, 12])
        self.assertEqual(quickSort([]), [])
        self.assertEqual(quickSort([4, 5]), [4, 5])
        self.assertEqual(quickSort([4, 3]), [3, 4])
        self.assertEqual(quickSort([5, 2, 4, 6, 1, 3]), [1, 2, 3, 4, 5, 6])

    def test_simple(self):
        self._tests()

    def _genRandomInput(self, pSize, pMax):
        result = []

        for i in range(pSize):
            result.append(random.randint(0, pMax))

        return result

    def test_random(self):
        for i in range(5, 25, 5):
            randomInput = self._genRandomInput(i, i + 5)
            a = quickSort(randomInput[:])
            randomInput.sort()
            b = randomInput
            print(*a)
            print(*b)
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()