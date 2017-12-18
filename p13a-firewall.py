import sys

import shared


if __name__ == '__main__':
    range_dict = shared.build_range_dict(sys.argv[1])
    penalty = shared.penalty_when_starting_at(0, range_dict)
    print(penalty)
