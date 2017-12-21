import sys

import shared


def parse_rule(l):
    left, right = (t.strip() for t in l.split('=>'))
    return tuple(left.split('/')), tuple(right.split('/'))


def parse_rules(lines_in):
    return {
        k:v for k,v in (parse_rule(l) for l in lines_in)
    }


# TODO: we can get away with a lot cheaper bc there are only two elements
# or generate all of these once in the beginning
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
        counterclockwise_turn(vertical_mirror(x)),
    ]


def convert_blocks_to_picture(blocks_grid, block_size):
    return tuple(''.join(blocks_grid[i // block_size][j][i % block_size] for j, _ in enumerate(blocks_grid)) for i in range(len(blocks_grid) * block_size))


def perform_iteration(p):
    if len(p) % 2 == 0:

        three_by_three_blocks = []
        for i in range(len(p) // 2):
            this_row = [None] * (len(p) // 2)
            three_by_three_blocks.append(this_row)
        for i in range(len(p) // 2):
            for j in range(len(p) // 2):
                cur_block = tuple(r[2 * i: 2 * i + 2] for r in p[j * 2:2 * j + 2])
                transformations = make_transformations(cur_block)
                for t in transformations:
                    if t in ruleset:
                        cur_three_block = ruleset[t]
                        # print("apply for: {0} == {1} --> {2}  ({3}, {4})".format(cur_block, t, ruleset[t], i, j))

                        break
                else:
                    raise Exception   # TODO: StopIteration
                three_by_three_blocks[i][j] = cur_three_block
        return convert_blocks_to_picture(three_by_three_blocks, 3)

    if len(p) % 3 == 0:

        four_by_four_blocks = []
        for i in range(len(p) // 3):
            this_row = [None] * (len(p) // 3)
            four_by_four_blocks.append(this_row)


        for i in range(len(p) // 3):
            for j in range(len(p) // 3):
                cur_block = tuple(r[3 * i: 3 * i + 3] for r in p[j * 3:3 * j + 3])
                transformations = make_transformations(cur_block)
                for t in transformations:
                    if t in ruleset:
                        cur_four_block = ruleset[t]
                        # print("apply for: {0} == {1} --> {2}  ({3}, {4})".format(cur_block, t, ruleset[t], i, j))
                        break
                else:
                    raise Exception  # TODO: StopIteration
                four_by_four_blocks[i][j] = cur_four_block

        return convert_blocks_to_picture(four_by_four_blocks, 4)

if __name__ == '__main__':
    lines_in = shared.get_exact_rows(sys.argv[1])
    ruleset = parse_rules(lines_in)
    picture = ('.#.', '..#', '###')

    cap = 19
    for i in range(cap):
        print("{0}: {1}".format(i, len([c for c in str(picture) if c == '#'])))
        picture = perform_iteration(picture)
    print("{0}: {1}".format(cap, len([c for c in str(picture) if c == '#'])))
