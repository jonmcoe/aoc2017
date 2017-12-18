import sys

import shared


if __name__ == '__main__':
    lines = shared.get_exact_rows(sys.argv[1])
    adjacency_dict = dict([shared.p12_parse_line(l) for l in lines])
    number_of_groups = 0
    while adjacency_dict:
        number_of_groups += 1
        first = next(iter(adjacency_dict.keys()))
        connected = shared.get_set_of_connecteds(adjacency_dict, first)
        for k in connected:
            del adjacency_dict[k]
    print(number_of_groups)
