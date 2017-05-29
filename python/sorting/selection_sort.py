import utils

def sort(input):
    input_len = len(input)
    for i in range(input_len):
        min_index = __find_min(input, i, input_len)
        utils.swap(input, i, min_index)


def __find_min(input, start, end):
    min_val = float('inf')
    min_index = -1;

    for i in range(start, end):
        if input[i] < min_val:
            min_val = input[i]
            min_index = i

    return min_index

