import utils
import math

step_records = []


def sort(input):
    global step_records
    step_records = []
    __sort(input, 0, len(input))
    return step_records


def __sort(input, start, end):
    global step_records

    length = end - start
    if length <= 1:
        return

    mid = __quick_sort(input, start, end)
    step_records.append("{} ~ {} [{}]".format(start, end, ', '.join(str(x) for x in input)))

    __sort(input, start, mid)
    __sort(input, mid + 1, end)


def __quick_sort(input, start, end):
    l, r = start + 1, end - 1

    pivot = input[start]

    while True:
        while l < end and input[l] <= pivot:
            l += 1
        while r > start and input[r] >= pivot:
            r -= 1
        if l < r:
            utils.swap(input, l, r)
            l += 1
            r -= 1
        else:
            utils.swap(input, start, r)
            return r
