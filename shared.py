import string


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

def get_separated_rows(filename, sep=',', func=None):
    def identity(x):
        return x
    if not func:
        func = identity
    with open(filename, 'r') as f:
        return ([func(item) for item in (l.split(sep))] for l in f.readlines())


# 3

def generate_spiral_until(n, next_value_func):
    # generate overly big list so we don't have to deal with "infinite" issues
    size = 10000
    grid = []
    for i in range(size):
        grid.append([None] * size)

    # initial stuff
    COUNTER_CLOCKWISE_DIRECTIONS_LIST = [
        (1, 0),
        (0, -1),
        (-1, 0),
        (0, 1)
    ]
    direction_index = 0
    cur = size // 2, size // 2
    last_placed = 1
    grid[cur[0]][cur[1]] = last_placed
    direction = COUNTER_CLOCKWISE_DIRECTIONS_LIST[direction_index]

    while last_placed < n:
        cur = (cur[0] + direction[0], cur[1] + direction[1])
        last_placed = next_value_func(grid, cur, last_placed)
        grid[cur[0]][cur[1]] = last_placed
        all_neighbors = [
            grid[cur[0] - 1][cur[1]],
            grid[cur[0] + 1][cur[1]],
            grid[cur[0]][cur[1] - 1],
            grid[cur[0]][cur[1] + 1]
        ]
        if len([neighbor for neighbor in all_neighbors if neighbor is not None]) == 1:
            direction_index += 1
            direction_index %= len(COUNTER_CLOCKWISE_DIRECTIONS_LIST)
            direction = COUNTER_CLOCKWISE_DIRECTIONS_LIST[direction_index]

    grid = [line for line in grid if any(cell is not None for cell in line)]  # filter out some of the crap. why not
    return grid, (cur[0] - size // 2, cur[1] - size // 2), last_placed


# 4

def count_with_all_unique_elements(lines):
    return sum((1 if len(list(l)) == len(set(list(l))) else 0) for l in lines)


# 5


def run_instructions(instructions, alteration_function):
    steps = 0
    num_instructions = len(instructions)
    cur_index = 0
    while 0 <= cur_index < num_instructions:
        cur_val = instructions[cur_index]
        instructions[cur_index] = alteration_function(cur_val)
        cur_index += cur_val
        steps += 1
    return steps


# 6

def reallocate_banks(banks):
    redistribution_amount = max(banks)
    new_banks = list(banks)
    current_index = new_banks.index(redistribution_amount)
    new_banks[current_index] = 0
    while redistribution_amount > 0:
        current_index += 1
        current_index %= len(new_banks)
        new_banks[current_index] += 1
        redistribution_amount -= 1
    return tuple(new_banks)

# 7


def get_exact_rows(filename):
    with open(filename, 'r') as f:
        return (l.strip() for l in f.readlines())

class DiscNode(object):

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children


def parse_disctree_row(line):
    try:
        name = line.split(' ')[0]
        weight = line.split('(')[1].split(')')[0]
        children_names = line.split('->')[1].strip().split(', ') if '->' in line else []
    except:
        raise
    return name, weight, children_names


#16


class DancerLineup(object):

    def __init__(self, n):
        self._offset = 0
        self._number_of_dancers = n
        self._dancers = list(string.ascii_lowercase[:n])
        # self._name_to_index = {  # need this if n gets big
        #     k: v for v, k in enumerate(self._dancers)
        # }

    def __str__(self):
        return ''.join(self._dancers[i - self._offset] for i in range(self._number_of_dancers))

    def spin(self, step):
        self._offset += step
        self._offset %= self._number_of_dancers

    def exchange(self, first_index, second_index):
        internal_first_index = first_index - self._offset
        internal_second_index = second_index - self._offset
        self._dumb_swap(internal_first_index , internal_second_index)

    def partner(self, first_name, second_name):
        internal_first_index = self._dancers.index(first_name)   # problem if n gets big
        internal_second_index = self._dancers.index(second_name)
        self._dumb_swap(internal_first_index, internal_second_index)

    def _dumb_swap(self, first_index, second_index):
        self._dancers[first_index], self._dancers[second_index] = self._dancers[second_index], self._dancers[first_index]

    def process_move(self, movestring):
        move_func = {
            's': self.spin,
            'x': self.exchange,
            'p': self.partner
        }[movestring[0]]
        args = movestring[1:].split('/')
        args = [(int(a) if a.isdigit() else a) for a in args]
        move_func(*args)


def get_moves(filename):
    with open(filename, 'r') as f:
        raw_contents = f.read()
    return raw_contents.split(',')
