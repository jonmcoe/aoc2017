import sys

import shared


if __name__ == '__main__':
    x = shared.get_exact_rows(sys.argv[1])
    parsed_args = [shared.parse_disctree_row(l) for l in x]
    print(shared.find_bottom(parsed_args))
