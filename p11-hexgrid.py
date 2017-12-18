import sys

import shared


TURN_TO_DIRECTION = {
    'n': (0, 1, -1),
    's': (0, -1, 1),
    'ne': (1, 0, -1),
    'nw': (-1, 1, 0),
    'se': (1, -1, 0),
    'sw': (-1, 0, 1)
}


def calc_distance(score):
    return sum(abs(x) for x in score) // 2


def perform_move(score, direction_str):
    current_direction = TURN_TO_DIRECTION[direction_str]
    new_score = score
    for i, _ in enumerate(score):
        new_score[i] += current_direction[i]
    return new_score


if __name__ == '__main__':
    steps_taken = next(shared.get_separated_rows(sys.argv[1], func=lambda x: x.strip()))
    score = [0, 0, 0]
    max_distance = 0
    for st in steps_taken:
        score = perform_move(score, st)
        max_distance = max(max_distance, calc_distance(score))
    print(calc_distance(score))
    print(max_distance)