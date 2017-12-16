import sys

from shared import get_separated_rows


if __name__ == '__main__':
    print(sum(max(map(int, l)) - min(map(int, l)) for l in get_separated_rows(sys.argv[1], sep='\t')))