import sys

from shared import get_exact_rows


if __name__ == '__main__':
    grid = list(get_exact_rows(sys.argv[1], strip=False))
    current_position = [0, grid[0].index('|')]
    direction = 1, 0
    letters_encountered = []
    current_character = None
    steps = 0
    while current_character != ' ':
        steps += 1
        current_position[0] += direction[0]
        current_position[1] += direction[1]
        current_character = grid[current_position[0]][current_position[1]]
        if current_character.isalpha():
            letters_encountered += current_character
        elif current_character == '+':
            left_turn = direction[1], direction[0]  # this is not correct how did this work
            right_turn = direction[1] * -1, direction[0] * -1
            peek_left_character = None
            peek_right_character = None

            if 0 <= current_position[0] + left_turn[0] < len(grid) and 0 <= current_position[1] + left_turn[1] < len(grid[1]):
                peek_left_character = grid[current_position[0] + left_turn[0]][current_position[1] + left_turn[1]]
            if 0 <= current_position[0] + right_turn[0] < len(grid) and 0 <= current_position[1] + right_turn[1] < len(grid[1]):
                peek_right_character = grid[current_position[0] + right_turn[0]][current_position[1] + right_turn[1]]

            if peek_left_character in {'-', '|'}:
                direction = left_turn
            elif peek_right_character in {'-', '|'}:
                direction = right_turn
            else:
                raise Exception("bad")
    print(''.join(letters_encountered))
    print(steps)