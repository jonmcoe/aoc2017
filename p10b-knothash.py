import sys

import shared


if __name__ == '__main__':
    bytesin = shared.get_string(sys.argv[1]).strip()
    print(shared.knot_hash(bytesin))
