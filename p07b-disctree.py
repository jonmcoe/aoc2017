import sys

import shared


if __name__ == '__main__':
    x = shared.get_exact_rows(sys.argv[1])
    parsed_args = [shared.parse_disctree_row(l) for l in x]
    bottom = shared.find_bottom(parsed_args)
    d = shared.build_disctree_arguments_dict(parsed_args)
    tree = shared.DiscNode(bottom, d)
    different_child, expected_weight = tree.find_different_child()
    different_child_candidate = different_child
    while different_child_candidate:
        different_child_candidate, different_child_candidate_weight = different_child.find_different_child()
        if different_child_candidate:
            different_child, expected_weight = different_child_candidate, different_child_candidate_weight
    print(expected_weight - (different_child.combined_weight() - different_child.weight))
