
def sort(input):
    if not input or len(input) == 1:
        return

    length = len(input)
    unit_size = 1

    while unit_size < length:
        merged_size = unit_size * 2
        for start in range(0, length - unit_size, merged_size):
            __merge(input, start, start + unit_size, start + merged_size)

        unit_size = merged_size


def __merge(input, left, right, end):
    real_end = min(end, len(input))
    sorted = []
    l, r = left, right

    while l < right and r < real_end:
        if input[l] <= input[r]:
            sorted.append(input[l])
            l += 1
        else:
            sorted.append(input[r])
            r += 1

    while l < right:
        sorted.append(input[l])
        l += 1

    while r < real_end:
        sorted.append(input[r])
        r += 1

    input[left:real_end] = sorted[:]

