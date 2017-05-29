import math

def sort(input):
    copy = []
    half_size = math.ceil(len(input) / 2)
    unit_size = 1

    while unit_size <= half_size:
        __unit_merge(input, copy, unit_size)
        temp = input
        input = copy
        copy = temp
        unit_size = unit_size * 2

    copy[:] = input[:]


def __unit_merge(source, target, unit_size):
    merged_size = unit_size * 2
    for left in range(0, len(source), merged_size):
        __merge_sort(source, target, left, left + unit_size, left + merged_size)


def __merge_sort(source, target, start_l, start_r, end):
    real_end = min(len(target), end)
    target_i = left = start_l
    right = start_r


    while target_i < real_end and left < start_r and right < real_end:
        if source[left] <= source[right]:
            target[target_i] = source[left]
            left += 1
        else:
            target[target_i] = source[right]
            right += 1

        target_i += 1

    while left < start_r and target_i < real_end:
        target[target_i] = source[left]
        left += 1
        target_i += 1
    while right < real_end and target_i < real_end:
        target[target_i] = source[right]
        right += 1
        target_i += 1

