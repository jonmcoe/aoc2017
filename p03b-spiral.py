import sys

import shared


if __name__ == '__main__':
    target = int(sys.argv[1])

    def summing_neighbors_function(grid, cur, last_value):
        return sum([
            grid[cur[0] - 1][cur[1] - 1] or 0,
            grid[cur[0] - 1][cur[1]] or 0,
            grid[cur[0] - 1][cur[1] + 1] or 0,
            grid[cur[0]][cur[1] - 1] or 0,
            grid[cur[0]][cur[1] + 1] or 0,
            grid[cur[0] + 1][cur[1] - 1] or 0,
            grid[cur[0] + 1][cur[1]] or 0,
            grid[cur[0] + 1][cur[1] + 1] or 0,
        ])

    _, __, last_value = shared.generate_spiral_until(target, summing_neighbors_function)
    print(last_value)
