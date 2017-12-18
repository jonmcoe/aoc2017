import sys

import shared


if __name__ == '__main__':
    range_dict = shared.build_range_dict(sys.argv[1])
    caught = True
    starting_time = -1
    while caught:
        starting_time += 1
        caught = shared.gets_caught(starting_time, range_dict)
    print(starting_time)

# 303870 failing not sure why