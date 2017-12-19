import sys

import shared


if __name__ == '__main__':
    hashprefix = shared.get_string(sys.argv[1]).strip()
    all_hashes_hexstring = (shared.knot_hash("{0}-{1}".format(hashprefix, i)) for i in range(128))
    as_bytes = (shared.convert_hex_to_bytes(h) for h in all_hashes_hexstring)
    print(sum(shared.sum_individual_characters(x) for x in as_bytes))
