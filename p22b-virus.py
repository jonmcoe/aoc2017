import sys

import shared


class CellStates:

    CLEAN = '.'
    WEAKENED = 'W'
    INFECTED = '#'
    FLAGGED = 'F'

    from_string = {
        '.': CLEAN,
        'W': WEAKENED,
        'F': FLAGGED,
        '#': INFECTED
    }

    next_state = {
        CLEAN: WEAKENED,
        WEAKENED: INFECTED,
        INFECTED: FLAGGED,
        FLAGGED: CLEAN
    }

if __name__ == '__main__':
    ITERATIONS = 10000000
    rows = list(shared.get_exact_rows(sys.argv[1]))
    grid_size = len(rows) + 1000
    notreallyinfinite_grid = shared.initialize_2d_array(grid_size, grid_size, '.')
    starting_bound = (grid_size - len(rows)) // 2
    for i, r in enumerate(rows):
        notreallyinfinite_grid[starting_bound + i][starting_bound:starting_bound + len(rows)] = list(r)

    position = grid_size // 2, grid_size // 2
    center = position
    direction = (-1, 0)
    infection_events = 0
    clean_streak = 0
    for _ in range(ITERATIONS):
        # if _ % 10000 == 0:
        #     print(_)
        current_state = shared.get_value_at_tuple(notreallyinfinite_grid, position)
        if current_state == CellStates.INFECTED:
            direction = direction[1], -1 * direction[0]  # right turn
            clean_streak = 0
        elif current_state == CellStates.CLEAN:
            direction = (-1 * direction[1], direction[0])  # left turn
            clean_streak += 1
        elif current_state == CellStates.FLAGGED:
            direction = (-1 * direction[0], -1 * direction[1])  # about face
        else:
            clean_streak = 0
        new_state = CellStates.next_state[current_state]
        if new_state == CellStates.INFECTED:
            infection_events += 1
        if clean_streak > 10:
            break
        shared.set_value_at_tuple(notreallyinfinite_grid, position, new_state)
        position = position[0] + direction[0], position[1] + direction[1]

    print(infection_events)
