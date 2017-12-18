import sys

import shared


def parse_line(line):
    left, right = line.split('<->')
    return int(left.strip()), [int(x.strip()) for x in right.split(', ')]


def get_set_of_connecteds(adjacency_dict, subject, seen=set()):
    if (subject not in adjacency_dict) or (subject in seen):
        return set()
    else:
        neighbors = adjacency_dict[subject]
        sets_to_union = (get_set_of_connecteds(adjacency_dict, s, seen.union([subject])) for s in neighbors)
        return {subject}.union(*sets_to_union)


if __name__ == '__main__':
    lines = shared.get_exact_rows(sys.argv[1])
    adjacency_dict = dict([parse_line(l) for l in lines])
    zero_connected = get_set_of_connecteds(adjacency_dict, 0)
    print(len(zero_connected))
