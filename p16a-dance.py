import string
import sys


DEFAULT_NUMBER_OF_DANCERS = 16


def spin(dancers, step):
    step = int(step)
    return [dancers[i - step] for i, _ in enumerate(dancers)]


def swap(dancers, first_index, second_index):
    x = list(dancers)
    x[first_index] = dancers[second_index]
    x[second_index] = dancers[first_index]
    return x


def exchange(dancers, first_index, second_index):
    first_index = int(first_index); second_index = int(second_index)
    return swap(dancers, first_index, second_index)


def partner(dancers, first_name, second_name):
    return swap(dancers, dancers.index(first_name), dancers.index(second_name))


CHARACTER_TO_FUNCTION = {
    's': spin,
    'x': exchange,
    'p': partner
}


def get_moves(filename):
    with open(filename, 'r') as f:
        raw_contents = f.read()
    return raw_contents.split(',')


if __name__ == '__main__':
    move_set = get_moves(sys.argv[1])
    number_of_dancers = (len(sys.argv) > 2 and int(sys.argv[2])) or DEFAULT_NUMBER_OF_DANCERS
    debug = len(sys.argv) > 3 and bool(sys.argv[3])
    current_dancers = list(string.ascii_lowercase[:number_of_dancers])
    for move in move_set:
        move_func = CHARACTER_TO_FUNCTION[move[0]]
        move_args = move[1:].split('/')
        if debug:
            print(''.join(current_dancers))
            print("MOVE: {0}".format(move))
        current_dancers = move_func(current_dancers, *move_args)
    print(''.join(current_dancers))
