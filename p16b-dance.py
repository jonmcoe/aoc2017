import string
import sys

from shared import get_moves, CHARACTER_TO_FUNCTION


DEFAULT_NUMBER_OF_DANCERS = 16
NUMBER_OF_DANCE_CYCLES = 10 ** 9


if __name__ == '__main__':
    move_set = get_moves(sys.argv[1])
    number_of_dancers = (len(sys.argv) > 2 and int(sys.argv[2])) or DEFAULT_NUMBER_OF_DANCERS
    debug = len(sys.argv) > 3 and bool(sys.argv[3])
    current_dancers = list(string.ascii_lowercase[:number_of_dancers])
    for _ in range(NUMBER_OF_DANCE_CYCLES):
        for move in move_set:
            move_func = CHARACTER_TO_FUNCTION[move[0]]
            move_args = move[1:].split('/')
            if debug:
                print(''.join(current_dancers))
                print("MOVE: {0}".format(move))
            current_dancers = move_func(current_dancers, *move_args)
    print(''.join(current_dancers))
