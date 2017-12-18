import sys

import shared


if __name__ == '__main__':
    lines = shared.get_exact_rows(sys.argv[1])
    adjacency_dict = dict([shared.p12_parse_line(l) for l in lines])
    zero_connected = shared.get_set_of_connecteds(adjacency_dict, 0)
    print(len(zero_connected))
