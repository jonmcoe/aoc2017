import sys

from shared import get_string, get_circle_sum


if __name__ == '__main__':
    sumstring = get_string(sys.argv[1])
    debug = len(sys.argv) > 2 and bool(sys.argv[2])
    print(get_circle_sum(sumstring, lambda i, l: ((i + int(l / 2)) % l), debug=debug))
