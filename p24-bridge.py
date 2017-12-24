import sys

import shared


def find_all_components_containing(needle, components):
    return [c for c in components if needle in c]


bad_global_paths = []  # this is terrible
def make_all_paths(so_far, available_components):
    if len(so_far) < 2:
        previous_spot = (0, 0)
    else:
        previous_spot = so_far[-2]
    searching_for = sorted(so_far[-1], key=lambda x: x in previous_spot)[0]
    next_up_candidates = find_all_components_containing(searching_for, available_components)
    if not next_up_candidates:
        bad_global_paths.append(so_far)
    else:
        # TODO: fix this flatmap and kill the global paths. maybe use itertools and chain?
        return [make_all_paths(so_far + [candidate], available_components - {candidate}) for candidate in next_up_candidates]


if __name__ == '__main__':
    all_components = set(tuple(t) for t in shared.get_separated_rows(sys.argv[1], '/', func=int))
    all_paths = make_all_paths([(0,0)], all_components)
    print(max(sum(map(sum, p)) for p in bad_global_paths))
    best_path = max(bad_global_paths, key=lambda x: (len(x), sum(map(sum, x))))
    print(sum(map(sum, best_path)))
