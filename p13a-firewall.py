import sys

import shared


def position_at_time(r, t):
    states = list(range(r)) + list(range(r - 2, 0, -1))
    return states[t % len(states)]


if __name__ == '__main__':
    lines = shared.get_exact_rows(sys.argv[1])
    range_dict = {
        int(t[0]): int(t[1]) for t in [l.split(':') for l in lines]
    }
    penalty = 0
    for d in range(max(range_dict.keys())):
        if d in range_dict and position_at_time(range_dict[d], d) == 0:
            print(d)
            penalty += d * range_dict[d]
    print(penalty)
