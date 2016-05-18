def selectionSort(pInput, pInPlace):
    length = len(pInput)
    infinity = float('inf')

    for i in range(length - 1):
        minVal = infinity

        for j in range(i, length):
            if pInput[j] < minVal:
                minVal = pInput[j]
                minIndex = j

        _swap(pInput, i, minIndex)

    return pInput


def _swap(pArray, a, b):
    temp = pArray[a]
    pArray[a] = pArray[b]
    pArray[b] = temp


import unittest

class TestSelectionSort(unittest.TestCase):
    def _tests(self, pInPlace):
        self.assertEqual(selectionSort([1, 2, 3, 4, 5, 6], pInPlace), [1, 2, 3, 4, 5, 6])
        self.assertEqual(selectionSort([6, 5, 4, 3, 2, 1], pInPlace), [1, 2, 3, 4, 5, 6])
        self.assertEqual(selectionSort([6, 3, 1, 2, 5, 4], pInPlace), [1, 2, 3, 4, 5, 6])
        self.assertEqual(selectionSort([1, 3, 5, 2, 4, 6], pInPlace), [1, 2, 3, 4, 5, 6])
        self.assertEqual(selectionSort([6], pInPlace), [6])
        self.assertEqual(selectionSort([5, 2, 1, 2, 5, 4, 1], pInPlace), [1, 1, 2, 2, 4, 5, 5])

        self.assertEqual(selectionSort([3, 12, 4, 9, 2, 4], pInPlace), [2, 3, 4, 4, 9, 12])
        self.assertEqual(selectionSort([], pInPlace), [])
        self.assertEqual(selectionSort([4, 5], pInPlace), [4, 5])
        self.assertEqual(selectionSort([4, 3], pInPlace), [3, 4])
        self.assertEqual(selectionSort([5, 2, 4, 6, 1, 3], pInPlace), [1, 2, 3, 4, 5, 6])

    def test_inplace(self):
        self._tests(True)


if __name__ == '__main__':
    unittest.main()