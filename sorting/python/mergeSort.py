def mergeSort(pInput):
    duplicate = pInput[:]

    return _sort(pInput, duplicate, 0, len(pInput) - 1)


def _sort(pOrigin, pDuplicate, pStart, pEnd):
    if pEnd <= pStart:
        return pDuplicate

    tMid = (pStart + pEnd) // 2
    _sort(pDuplicate, pOrigin, pStart, tMid)
    _sort(pDuplicate, pOrigin, tMid + 1, pEnd)

    _merge(pOrigin, pDuplicate, pStart, tMid, pEnd)

    return pDuplicate


def _merge(pBefore, pAfter, pLow, pMid, pHigh):
    l, r, p = pLow, pMid + 1, pLow

    while p <= pHigh:
        if l > pMid:
            pAfter[p] = pBefore[r]
            r = r + 1
        elif r > pHigh:
            pAfter[p] = pBefore[l]
            l = l + 1
        elif pBefore[l] > pBefore[r]:
            pAfter[p] = pBefore[r]
            r = r + 1
        else:
            pAfter[p] = pBefore[l]
            l = l + 1

        p = p + 1

    return pAfter


import unittest
import random

class TestSort(unittest.TestCase):
    def _tests(self):
        self.assertEqual(mergeSort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(mergeSort([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(mergeSort([6, 3, 1, 2, 5, 4]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(mergeSort([1, 3, 5, 2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(mergeSort([6]), [6])
        self.assertEqual(mergeSort([5, 2, 1, 2, 5, 4, 1]), [1, 1, 2, 2, 4, 5, 5])

        self.assertEqual(mergeSort([3, 12, 4, 9, 2, 4]), [2, 3, 4, 4, 9, 12])
        self.assertEqual(mergeSort([]), [])
        self.assertEqual(mergeSort([4, 5]), [4, 5])
        self.assertEqual(mergeSort([4, 3]), [3, 4])
        self.assertEqual(mergeSort([5, 2, 4, 6, 1, 3]), [1, 2, 3, 4, 5, 6])

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
            a = mergeSort(randomInput[:])
            randomInput.sort()
            b = randomInput
            print(*a)
            print(*b)
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()