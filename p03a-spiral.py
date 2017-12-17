import sys

import shared


if __name__ == '__main__':
    target = int(sys.argv[1])

    def incrementing_function(grid, cur, last_value):
        return last_value + 1

    _, last_location, __ = shared.generate_spiral_until(target, incrementing_function)
    steps = last_location[0] + last_location[1]
    print(steps)
