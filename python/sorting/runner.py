import sys

sys.path.append('/Users/Brilliun/Workspace/Algorithms/python')

import importlib
import random

test_cases = [
    [],
    [1],
    [1, 2],
    [2, 1],
    [1, 2, 3],
    [3, 2, 1],
    [2, 1, 3],
    [3, 1, 2],
]

def __generate_random_test_cases(size, hi, lo = 0):
    test_case = []
    for i in range(size):
        test_case.append(random.randint(lo, hi))

    return test_case


def __array_equal(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def run():
    for i in range(5):
        test_cases.append(__generate_random_test_cases(6, 10))
    for i in range(5):
        test_cases.append(__generate_random_test_cases(11, 20))
    for i in range(10):
        test_cases.append(__generate_random_test_cases(20, 30))

    algorithm = importlib.import_module(sys.argv[1])

    for test in test_cases:
        origin = test[:]
        sorted_origin = sorted(origin)
        algorithm.sort(test)
        if not __array_equal(test, sorted_origin):
            print('Sort failed!')
        print('Origin: {0}'.format(origin))
        print('Sorted: {0}'.format(sorted_origin))
        print('Result: {0}'.format(test))


run()
