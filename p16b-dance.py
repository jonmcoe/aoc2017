import sys

from shared import DancerLineup, get_moves


DEFAULT_NUMBER_OF_DANCERS = 16
NUMBER_OF_CYCLES = 10 ** 9


if __name__ == '__main__':
    move_set = get_moves(sys.argv[1])
    number_of_dancers = (len(sys.argv) > 2 and int(sys.argv[2])) or DEFAULT_NUMBER_OF_DANCERS
    debug = len(sys.argv) > 3 and bool(sys.argv[3])
    current_dancers = DancerLineup(number_of_dancers)
    initial_string = str(current_dancers)

    # find cycle
    cycle_point = None
    for dance_routine_iteration in range(NUMBER_OF_CYCLES):
        if dance_routine_iteration > 0 and str(current_dancers) == initial_string:
            cycle_point = dance_routine_iteration
            print(cycle_point)
            break

        for move in move_set:
            if debug:
                print(current_dancers)
                print("MOVE: {0}".format(move))
            current_dancers.process_move(move)

    # perform difference
    for dance_routine_iteration in range(NUMBER_OF_CYCLES % cycle_point):
        for move in move_set:
            if debug:
                print(current_dancers)
                print("MOVE: {0}".format(move))
            current_dancers.process_move(move)

    print(current_dancers)
