import sys

import shared


if __name__ == '__main__':
    x = shared.get_exact_rows(sys.argv[1])
    parsed_args = [shared.parse_disctree_row(l) for l in x]

    root_names = set()
    leaf_names = set()
    for arg_set in parsed_args:
        root_names.add(arg_set[0])
        for leaf_name in arg_set[2]:
            leaf_names.add(leaf_name)
    print(root_names - leaf_names)
