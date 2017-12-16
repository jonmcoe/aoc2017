# 1


def get_string(filename):
    with open(filename, 'r') as f:
        raw_contents = f.read()
    return raw_contents


def get_circle_sum(sumstring, counterpart_func, debug=False):
    running_sum = 0
    total_length = len(sumstring)
    for i, c in enumerate(sumstring):
        if c == sumstring[counterpart_func(i, total_length)]:
            c_int = int(c)
            running_sum += c_int
        if debug:
            print(running_sum)
            print(sumstring[i:])
    return running_sum


#2


def spin(dancers, step):
    step = int(step)
    return [dancers[i - step] for i, _ in enumerate(dancers)]


def _swap(dancers, first_index, second_index):
    x = list(dancers)
    x[first_index] = dancers[second_index]
    x[second_index] = dancers[first_index]
    return x


def exchange(dancers, first_index, second_index):
    first_index = int(first_index); second_index = int(second_index)
    return _swap(dancers, first_index, second_index)


def partner(dancers, first_name, second_name):
    return _swap(dancers, dancers.index(first_name), dancers.index(second_name))


CHARACTER_TO_FUNCTION = {
    's': spin,
    'x': exchange,
    'p': partner
}


def get_moves(filename):
    with open(filename, 'r') as f:
        raw_contents = f.read()
    return raw_contents.split(',')
