import sys

from shared import get_generator_seeds


BOUND = 40 * 10 ** 6
COMPARISON_BOUNDARY = 2 ** 16


# 7 ** 5 and a prime. so certainly relatively prime
MULTIPLICANDS = [16807, 48271]

DIVISOR = 2147483647


if __name__ == '__main__':
    values = get_generator_seeds(sys.argv[1])
    matches = 0
    for _ in range(BOUND):
        # if _ % 10 ** 6 == 0:
        #     print("{}: {}".format(_, matches))
        values[0] = (values[0] * MULTIPLICANDS[0]) % DIVISOR
        values[1] = (values[1] * MULTIPLICANDS[1]) % DIVISOR
        if (values[0] % COMPARISON_BOUNDARY == values[1] % COMPARISON_BOUNDARY):
            matches += 1
    print(matches)