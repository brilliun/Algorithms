import unittest

def insertionSort(pInput, pInplace):
    return _insertionInPlace(pInput) if pInplace else _insertionNew(pInput)


def _insertionInPlace(pInput):
    length = len(pInput)
    j = 0

    for i in range(length):
        curr = pInput[i]
        for j in reversed(range(i)):
            compare = pInput[j]
            if curr < compare:
                pInput[j + 1] = compare
            else:
                if j + 1 != i:
                    pInput[j + 1] = curr
                break
        else:
            if i != 0:
                pInput[0] = curr

    return pInput


def _insertionNew(pInput):
    result = []
    length = len(pInput)

    for i in range(length):
        curr = pInput[i]
        pos = 0

        for j in reversed(range(i)):
            if curr >= result[j]:
                pos = j + 1
                break

        result.insert(pos, curr)

    return result


class TestInsertionSort(unittest.TestCase):
    def _tests(self, pInPlace):
        self.assertEqual(insertionSort([1, 2, 3, 4, 5, 6], pInPlace), [1, 2, 3, 4, 5, 6])
        self.assertEqual(insertionSort([6, 5, 4, 3, 2, 1], pInPlace), [1, 2, 3, 4, 5, 6])
        self.assertEqual(insertionSort([6, 3, 1, 2, 5, 4], pInPlace), [1, 2, 3, 4, 5, 6])
        self.assertEqual(insertionSort([1, 3, 5, 2, 4, 6], pInPlace), [1, 2, 3, 4, 5, 6])
        self.assertEqual(insertionSort([6], pInPlace), [6])
        self.assertEqual(insertionSort([5, 2, 1, 2, 5, 4, 1], pInPlace), [1, 1, 2, 2, 4, 5, 5])

        self.assertEqual(insertionSort([3, 12, 4, 9, 2, 4], pInPlace), [2, 3, 4, 4, 9, 12])
        self.assertEqual(insertionSort([], pInPlace), [])
        self.assertEqual(insertionSort([4, 5], pInPlace), [4, 5])
        self.assertEqual(insertionSort([4, 3], pInPlace), [3, 4])
        self.assertEqual(insertionSort([5, 2, 4, 6, 1, 3], pInPlace), [1, 2, 3, 4, 5, 6])

    def test_inplace(self):
        self._tests(True)

    def test_not_inplace(self):
        self._tests(False)

if __name__ == '__main__':
    unittest.main()
