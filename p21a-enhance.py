import sys
from functools import lru_cache

import shared


def parse_rule(l):
    left, right = (t.strip() for t in l.split('=>'))
    return tuple(left.split('/')), tuple(right.split('/'))


def parse_rules(lines_in):
    return {
        k: v for k, v in (parse_rule(l) for l in lines_in)
    }


# TODO: we can get away with a lot cheaper bc there are only two elements and therefore symmetries.
# then again cache makes less unimportant
@lru_cache()
def make_transformations(x):

    def horizontal_mirror(x):
        return x[::-1]

    def vertical_mirror(x):
        return tuple(x[i][::-1] for i, _ in enumerate(x))

    def counterclockwise_turn(x):
        return tuple("".join(x[i][-j-1] for i, _ in enumerate(x)) for j, __ in enumerate(x))

    return [
        x,
        horizontal_mirror(x),
        vertical_mirror(x),
        counterclockwise_turn(x),
        counterclockwise_turn(counterclockwise_turn(x)),
        counterclockwise_turn(counterclockwise_turn(counterclockwise_turn(x))),
        counterclockwise_turn(horizontal_mirror(x)),
        counterclockwise_turn(vertical_mirror(x))
    ]


def convert_blocks_to_picture(blocks_grid):
    block_size = len(blocks_grid[0][0])
    return tuple(
        ''.join(blocks_grid[i // block_size][j][i % block_size] for j, _ in enumerate(blocks_grid))
        for i in range(len(blocks_grid) * block_size)
    )


def perform_iteration(p):

    chop_by = next(i for i in (2, 3) if len(p) % i == 0)
    num_blocks = len(p) // chop_by
    blocks_grid = shared.initialize_2d_array(num_blocks, num_blocks, '.')

    for i in range(num_blocks):
        for j in range(num_blocks):
            cur_block_in = tuple(r[chop_by * i: chop_by * i + chop_by] for r in p[j * chop_by:chop_by * j + chop_by])
            transformation = next(t for t in make_transformations(cur_block_in) if t in ruleset)
            cur_block_out = ruleset[transformation]
            # print("apply for: {0} == {1} --> {2}  ({3}, {4})".format(cur_block_in, transformation, cur_block_out, i, j))
            blocks_grid[i][j] = cur_block_out
    return convert_blocks_to_picture(blocks_grid)


if __name__ == '__main__':
    lines_in = shared.get_exact_rows(sys.argv[1])
    ruleset = parse_rules(lines_in)
    picture = ('.#.', '..#', '###')

    cap = 6
    for iteration in range(cap):
        print("{0}: {1}".format(iteration, len([c for c in str(picture) if c == '#'])))
        picture = perform_iteration(picture)
    print("{0}: {1}".format(cap, len([c for c in str(picture) if c == '#'])))
