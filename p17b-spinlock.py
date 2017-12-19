import sys

import shared


if __name__ == '__main__':
    step_size = int(shared.get_string(sys.argv[1]).strip())
    l = [0]  # this is probably not the best data structure
    cursor = 0
    for current_val in range(1, 50000000):
        cursor = (cursor + step_size) % len(l) + 1
        l.insert(cursor, current_val)
    print(l[l.index(0) + 1])
