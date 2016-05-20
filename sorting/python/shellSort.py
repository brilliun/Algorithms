def shellSort(pInput):
    N = len(pInput)
    h = 1
    j = 0

    while h < N/3:
        h = h * 3 + 1

    while h >= 1:
        for i in range(h, N):
            curr = pInput[i]

            for j in range(i - h, -1, -h):
                if curr < pInput[j]:
                    pInput[j + h] = pInput[j]
                else:
                    if j + h != i:
                        pInput[j + h] = curr
                    break
            else:
                if i != j:
                    pInput[j] = curr

        h = h // 3;

    return pInput


import unittest
import random

class TestshellSort(unittest.TestCase):
    def _tests(self):
        self.assertEqual(shellSort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(shellSort([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(shellSort([6, 3, 1, 2, 5, 4]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(shellSort([1, 3, 5, 2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(shellSort([6]), [6])
        self.assertEqual(shellSort([5, 2, 1, 2, 5, 4, 1]), [1, 1, 2, 2, 4, 5, 5])

        self.assertEqual(shellSort([3, 12, 4, 9, 2, 4]), [2, 3, 4, 4, 9, 12])
        self.assertEqual(shellSort([]), [])
        self.assertEqual(shellSort([4, 5]), [4, 5])
        self.assertEqual(shellSort([4, 3]), [3, 4])
        self.assertEqual(shellSort([5, 2, 4, 6, 1, 3]), [1, 2, 3, 4, 5, 6])

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
            a = shellSort(randomInput[:])
            randomInput.sort()
            b = randomInput
            print(*a)
            print(*b)
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()