import sys

import shared


if __name__ == '__main__':
    lines = shared.get_separated_rows(sys.argv[1], ' ', lambda x: x.replace('\n', ''))
    print(sum((1 if len(list(l)) == len(set(list(l))) else 0) for l in lines))