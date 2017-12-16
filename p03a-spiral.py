import math
import sys


if __name__ == '__main__':
    target = int(sys.argv[1])
    block = int(math.ceil(math.sqrt(target)))
    if block % 2 == 0:
        block += 1
    width = (block - 1) / 2
    steps = width + width
    closest_square = block ** 2
    for loc in range(closest_square, target, -1):
        # TODO: conditional for whether in growing or shrinking section. deal with corners
        # right now we are only correct for those "slightly" less (within `block / 2` than the odd integer's square (bottom edge)
        # we'll see if this is worth fixing when we see part two
        # NOTE: probably not worth fixing. I see no way around a true constructive approach in p03b
        steps -= 1
        loc -= 1
    print(steps)
