import itertools
import sys
from functools import reduce
from operator import xor

import shared


EXTRA_BYTES = [17, 31, 73, 47, 23]

if __name__ == '__main__':
    bytesin = shared.get_string(sys.argv[1]).strip()
    lengths = [ord(b) for b in bytesin] + EXTRA_BYTES
    kt = shared.KnotTwine(256)
    for length in lengths * 64:
        kt.transform(length)
    sixteen_blocks = itertools.groupby(enumerate(kt.twine), lambda t: t[0] // 16)
    sum_answer = ""
    for k, block in sixteen_blocks:
        current_block_xor = 0
        for i, val in block:
            current_block_xor ^= val
        # print(current_block_xor)
        sum_answer += '%02x' % current_block_xor
    print(sum_answer)
    # sum(reduce(lambda a, b: a, b[0]), t) for _, t in sixteen_blocks)


# submitted

# e1edc524b973d8ce80dad9251a2cb918
# 2f8c3d2100fdd57cec130d928b0fd2dd