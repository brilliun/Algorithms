
def search(input, target):
    if not input or len(input) == 0:
        return -1

    return __binary_search(input, target, 0, len(input))



def __binary_search(input, target, start, end):
    if end <= start:
        return -1

    mid = start + (end - start) // 2
    mid_value = input[mid]

    if mid_value == target:
        return mid
    elif mid_value > target:
        return __binary_search(input, target, start, mid)
    else:
        return __binary_search(input, target, mid + 1, end)