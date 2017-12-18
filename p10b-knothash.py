import sys
from functools import reduce
from operator import add, xor

import shared


EXTRA_BYTES = [17, 31, 73, 47, 23]


if __name__ == '__main__':
    bytesin = shared.get_string(sys.argv[1]).strip()
    lengths = [ord(b) for b in bytesin] + EXTRA_BYTES
    kt = shared.KnotTwine(256)
    for length in lengths * 64:
        kt.transform(length)
    blocks_of_sixteen = (kt.twine[block_num * 16:block_num * 16 + 16] for block_num in range(16))
    xor_results_hex_pairs = ('%02x' % reduce(xor, l) for l in blocks_of_sixteen)
    sum_result = reduce(add, xor_results_hex_pairs)
    print(sum_result)
