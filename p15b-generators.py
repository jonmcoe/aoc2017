import sys

from shared import (
    GENERATOR_COMPARISON_BOUNDARY,
    GENERATOR_DIVISOR,
    GENERATOR_MULTIPLICANDS,
    get_generator_seeds
)


BOUND = 5 * 10 ** 6
CONFIRMATION_DIVISORS = [4, 8]


def make_generator(val, multiplicand, confirmation_divisor):
    while True:
        val = val * multiplicand % GENERATOR_DIVISOR
        if val % confirmation_divisor == 0:
            yield val


if __name__ == '__main__':
    values = get_generator_seeds(sys.argv[1])
    matches = 0
    generators = [make_generator(t[0], t[1], t[2]) for t in zip(values, GENERATOR_MULTIPLICANDS, CONFIRMATION_DIVISORS)]
    for _ in range(BOUND):
        # if _ % 10 ** 5 == 0:
        #     print("{}: {}".format(_, matches))
        if next(generators[0]) % GENERATOR_COMPARISON_BOUNDARY == next(generators[1]) % GENERATOR_COMPARISON_BOUNDARY:
            matches += 1
    print(matches)
