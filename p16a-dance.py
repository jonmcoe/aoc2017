import sys

from shared import DancerLineup, get_moves


DEFAULT_NUMBER_OF_DANCERS = 16


if __name__ == '__main__':
    move_set = get_moves(sys.argv[1])
    number_of_dancers = (len(sys.argv) > 2 and int(sys.argv[2])) or DEFAULT_NUMBER_OF_DANCERS
    debug = len(sys.argv) > 3 and bool(sys.argv[3])
    current_dancers = DancerLineup(number_of_dancers)
    for move in move_set:
        if debug:
            print(current_dancers)
            print("MOVE: {0}".format(move))
        current_dancers.process_move(move)
    print(current_dancers)
