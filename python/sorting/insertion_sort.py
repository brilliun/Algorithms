import utils


def sort(input):
    if input is None or len(input) <= 1:
        return input

    for nxt in range(1, len(input)):
        nxt_val = input[nxt]
        
        for cpr in range(nxt - 1, -1, -1):
            if nxt_val < input[cpr]:
                input[cpr + 1] = input[cpr]
            else:
                if cpr + 1 < nxt:
                    input[cpr + 1] = nxt_val
                break
        else:
            input[0] = nxt_val


