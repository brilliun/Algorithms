import sys

sys.path.append('/Users/Brilliun/Workspace/Algorithms/python')

import importlib
import random

test_cases = [
    [1],
    [1, 2],
    [1, 2, 3],
]

def __generate_random_test_cases(size, hi, lo = 0):
    test_case = []
    for i in range(size):
        test_case.append(random.randint(lo, hi))

    return sorted(test_case)



def run():
    for i in range(5):
        test_cases.append(__generate_random_test_cases(6, 10))
    for i in range(5):
        test_cases.append(__generate_random_test_cases(11, 20))
    for i in range(10):
        test_cases.append(__generate_random_test_cases(20, 30))

    algorithm = importlib.import_module(sys.argv[1])

    for test in test_cases:
        target = test[random.randint(0, len(test) - 1)]
        search_result = algorithm.search(test, target)

        if test[search_result] != target:
            print('Search {} failed! {}'.format(target, search_result))
            print('Input: {}'.format(test))
            break


run()
