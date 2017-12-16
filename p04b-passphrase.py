import sys

import shared


if __name__ == '__main__':
    lines = shared.get_separated_rows(sys.argv[1], ' ', lambda x: ''.join(sorted(x.replace('\n', ''))))
    print(shared.count_with_all_unique_elements(lines))
