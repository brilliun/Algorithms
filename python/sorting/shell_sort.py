import utils


def sort(input):
    if input is None or len(input) <= 1:
        return input

    shell_size = max(len(input) // 3, 1)
    while shell_size > 0:
        __sort_by_shell(input, shell_size)
        if shell_size == 1:
            break
        shell_size = max(shell_size // 3, 1)



def __sort_by_shell(input, shell_size):
    if input is None or len(input) <= shell_size:
        return input

    for nxt in range(shell_size, len(input), shell_size):
        nxt_val = input[nxt]
        
        for cpr in range(nxt - shell_size, -1, -shell_size):
            if nxt_val < input[cpr]:
                input[cpr + shell_size] = input[cpr]
            else:
                if cpr + shell_size < nxt:
                    input[cpr + shell_size] = nxt_val
                break
        else:
            input[0] = nxt_val


