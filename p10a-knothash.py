import sys

import shared


if __name__ == '__main__':
    lengths = next(shared.get_separated_rows(sys.argv[1], func=int))
    kt = shared.KnotTwine(256)
    for length in lengths:
        kt.transform(length)
    print(kt.twine[0] * kt.twine[1])