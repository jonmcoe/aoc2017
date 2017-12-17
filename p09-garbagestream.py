import sys

import shared


if __name__ == '__main__':
    raw_string = shared.get_string(sys.argv[1])
    garbageless, discarded_count = shared.remove_garbage(raw_string)
    print(discarded_count)
    print(shared.count_depth_score(garbageless))
