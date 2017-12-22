import sys

import shared


INFECTED = '#'
CLEAN = '.'

if __name__ == '__main__':
    ITERATIONS = 10000
    rows = list(shared.get_exact_rows(sys.argv[1]))
    grid_size = len(rows) + ITERATIONS
    notreallyinfinite_grid = shared.initialize_2d_array(grid_size, grid_size, '.')
    starting_bound = (grid_size - len(rows)) // 2
    for i, r in enumerate(rows):
        notreallyinfinite_grid[starting_bound + i][starting_bound:starting_bound + len(rows)] = list(r)

    position = grid_size // 2, grid_size // 2
    direction = (-1, 0)
    infection_events = 0
    # confirm centering
    # notreallyinfinite_grid[center[0]][center[1]] = 'X'
    # for r in notreallyinfinite_grid[center[0]-15:center[0]+15]:
    #     print(r[center[0]-15:center[0]+15])
    for _ in range(ITERATIONS):
        if shared.get_value_at_tuple(notreallyinfinite_grid, position) == INFECTED:
            direction = direction[1], -1 * direction[0]  # right turn
            shared.set_value_at_tuple(notreallyinfinite_grid, position, CLEAN)
        elif shared.get_value_at_tuple(notreallyinfinite_grid, position) == CLEAN:
            direction = (-1 * direction[1], direction[0])  # left turn
            shared.set_value_at_tuple(notreallyinfinite_grid, position, INFECTED)
            infection_events += 1
        position = position[0] + direction[0], position[1] + direction[1]
    print(infection_events)
    # notreallyinfinite_grid[position[0]][position[1]] = 'X'
    # for r in notreallyinfinite_grid[position[0] - 15:position[0] + 15]:
    #     print(r[position[0] - 15:position[0] + 15])
