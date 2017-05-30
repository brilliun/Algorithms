import math

# A top-down recursive implementation

def sort(input):
    copy = input[:]
    __sort(copy, input, 0, len(input))


def __sort(source, target, start, end):
    length = end - start
    if length <= 1:
        return

    mid = start + math.ceil(length / 2)

    __sort(target, source, start, mid)
    __sort(target, source, mid, end)
    __merge(source, target, start, mid, end)



def __merge(source, target, start_l, start_r, end):
    target_i = left = start_l
    right = start_r

    while left < start_r and right < end:
        if source[left] <= source[right]:
            target[target_i] = source[left]
            left += 1
        else:
            target[target_i] = source[right]
            right += 1

        target_i += 1

    while left < start_r:
        target[target_i] = source[left]
        left += 1
        target_i += 1
    while right < end:
        target[target_i] = source[right]
        right += 1
        target_i += 1

