import sys

from shared import (
    GENERATOR_COMPARISON_BOUNDARY,
    GENERATOR_DIVISOR,
    GENERATOR_MULTIPLICANDS,
    get_generator_seeds
)


BOUND = 40 * 10 ** 6


if __name__ == '__main__':
    values = get_generator_seeds(sys.argv[1])
    matches = 0
    for _ in range(BOUND):
        # if _ % 10 ** 6 == 0:
        #     print("{}: {}".format(_, matches))
        values[0] = (values[0] * GENERATOR_MULTIPLICANDS[0]) % GENERATOR_DIVISOR
        values[1] = (values[1] * GENERATOR_MULTIPLICANDS[1]) % GENERATOR_DIVISOR
        if values[0] % GENERATOR_COMPARISON_BOUNDARY == values[1] % GENERATOR_COMPARISON_BOUNDARY:
            matches += 1
    print(matches)
