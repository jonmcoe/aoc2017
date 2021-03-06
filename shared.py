import re
import string
from collections import defaultdict, deque, namedtuple
from functools import reduce
from operator import add, mod, mul, sub, xor

from typing import Dict, List, Sequence

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


def get_exact_rows(filename, strip=True):
    with open(filename, 'r') as f:
        return (l.strip() if strip else l for l in f.readlines())


class DiscNode(object):

    def __init__(self, name, arguments_dict):
        self.name = name
        current_node_arguments = arguments_dict[name]
        self.weight = current_node_arguments[1]
        self.children = [
            DiscNode(name, arguments_dict) for name in current_node_arguments[2]
        ]

    def combined_weight(self):
        return self.weight + sum([c.combined_weight() for c in self.children])

    def find_different_child(self):
        if len(self.children) < 3:
            return (None, None)

        # inspect first 2 carefully
        first_weight = self.children[0].combined_weight()
        second_weight = self.children[1].combined_weight()
        if first_weight == second_weight:
            expected_weight = first_weight
        else:
            third_weight = self.children[2].combined_weight()
            if first_weight == third_weight:
                return self.children[1], third_weight
            else:
                return self.children[0], third_weight

        # iterate further if first 3 match
        for i, c in enumerate(self.children):
            if c.combined_weight() != expected_weight:
                return c, expected_weight
        return None, None


def build_disctree_arguments_dict(parsed_args_list):
    return {
        args[0]: args for args in parsed_args_list
    }


def find_bottom(parsed_args):
    root_names = set()
    leaf_names = set()
    for arg_set in parsed_args:
        root_names.add(arg_set[0])
        for leaf_name in arg_set[2]:
            leaf_names.add(leaf_name)
    return (root_names - leaf_names).pop()


def parse_disctree_row(line):
    try:
        name = line.split(' ')[0]
        weight = int(line.split('(')[1].split(')')[0])
        children_names = line.split('->')[1].strip().split(', ') if '->' in line else []
    except:
        raise
    return name, weight, children_names


# 8

Instruction = namedtuple('instruction', ['register', 'op', 'amount', 'condition_reg', 'condition_op', 'condition_val'])


def parse_instruction(raw_message):
    tokens = [t for t in raw_message.split() if t != 'if']
    for i, t in enumerate(tokens):
        if all(c in '-0123456789' for c in t):
            tokens[i] = int(t)
    return Instruction(*tokens)


class RegisterMachine:

    def __init__(self):
        self.registers = defaultdict(int)
        self.max_ever = 0

    def process_instruction(self, instruction):
        CONDITION_DICT = {  # probably could've gotten away with eval...
            '>': lambda reg, val: reg > val,
            '<': lambda reg, val: reg < val,
            '>=': lambda reg, val: reg >= val,
            '<=': lambda reg, val: reg <= val,
            '==': lambda reg, val: reg == val,
            '!=': lambda reg, val: reg != val
        }
        OPERATION_DICT = {
            'inc': lambda reg, val: reg + val,
            'dec': lambda reg, val: reg - val
        }
        if CONDITION_DICT[instruction.condition_op](self.registers[instruction.condition_reg], instruction.condition_val):
            new_val = OPERATION_DICT[instruction.op](self.registers[instruction.register], instruction.amount)
            self.registers[instruction.register] = new_val
            self.max_ever = max(new_val, self.max_ever)

    def get_max_register(self):
        return max(self.registers.values())

# 9


def remove_garbage(raw_string):
    # handle !
    no_exclamations_string = ""
    last_exclamation = False
    for i in raw_string:
        if not last_exclamation and i != '!':
            no_exclamations_string += i
        last_exclamation = i == '!' and not last_exclamation

    # remove < > blocks
    discarded_interior = 0
    garbageless_string = ""
    active_left_anglebracket = False
    for i in no_exclamations_string:
        if active_left_anglebracket and i != '>':
            discarded_interior += 1
        if i == '<':
            active_left_anglebracket = True

        if not active_left_anglebracket:
            garbageless_string += i
        else:
            active_left_anglebracket = i != '>'
    return garbageless_string, discarded_interior


def count_depth_score(input_string):
    current_depth = 0
    sum_depth = 0
    for i in input_string:
        if i == '{':
            current_depth += 1
            sum_depth += current_depth
        if i == '}':
            current_depth -= 1
    return sum_depth


# 10

class KnotTwine:

    def __init__(self, size):
        self.twine = list(range(size))
        self.size = size
        self.position = 0
        self.skip_size = 0

    def transform(self, transformation_length):
        left = self.position
        right = self.position + transformation_length
        if right >= self.size:
            modified_section = self.twine[left:self.size + 1] + self.twine[0:right % self.size]
            reversed_modified_section = modified_section[::-1]
            reversed_modified_left = reversed_modified_section[0:self.size - left]
            reversed_modified_right = reversed_modified_section[self.size - left:]
            self.twine[left:self.size] = reversed_modified_left
            self.twine[0:right % self.size] = reversed_modified_right
        else:
            if self.position == 0:
                self.twine[left:right] = self.twine[right - 1::-1]
            else:
                self.twine[left:right] = self.twine[right - 1:left - 1:-1]
        self.position = (self.position + transformation_length + self.skip_size) % self.size
        self.skip_size += 1




def knot_hash(bytesin):
    EXTRA_BYTES = [17, 31, 73, 47, 23]
    lengths = [ord(b) for b in bytesin] + EXTRA_BYTES
    kt = KnotTwine(256)
    for length in lengths * 64:
        kt.transform(length)
    blocks_of_sixteen = (kt.twine[block_num * 16:block_num * 16 + 16] for block_num in range(16))
    xor_results_hex_pairs = ('%02x' % reduce(xor, l) for l in blocks_of_sixteen)
    return reduce(add, xor_results_hex_pairs)

# 12


def p12_parse_line(line):
    left, right = line.split('<->')
    return int(left.strip()), [int(x.strip()) for x in right.split(', ')]


def get_set_of_connecteds(adjacency_dict, subject, seen=set()):
    if (subject not in adjacency_dict) or (subject in seen):
        return set()
    else:
        neighbors = adjacency_dict[subject]
        sets_to_union = (get_set_of_connecteds(adjacency_dict, s, seen.union([subject])) for s in neighbors)
        return {subject}.union(*sets_to_union)

# 13


def build_range_dict(filename):
    with open(filename, 'r') as f:
        return {
            int(t[0]): int(t[1]) for t in [l.split(':') for l in f.readlines() if l.strip()]
        }


def position_at_time(r, t):
    states = list(range(r)) + list(range(r - 2, 0, -1))
    return states[t % len(states)]


def penalty_when_starting_at(starting_time, range_dict):
    penalty = 0
    for d in range(max(range_dict.keys())):
        if d in range_dict and position_at_time(range_dict[d], d + starting_time) == 0:
            penalty += d * range_dict[d]
    return penalty


def gets_caught(starting_time, range_dict):
    for d in range(max(range_dict.keys()) + 1):
        if d in range_dict and position_at_time(range_dict[d], d + starting_time) == 0:
            return True
    return False


# 14

def sum_individual_characters(int_string):
    return sum(int(c) for c in int_string)


def convert_hex_to_bytes(h):
    return "{:0128b}".format(int(h, 16))


#15


def get_generator_seeds(filename):
    rows = get_separated_rows(filename, sep=' ')
    return [int(r[-1]) for r in rows]


GENERATOR_COMPARISON_BOUNDARY = 2 ** 16

GENERATOR_MULTIPLICANDS = [16807, 48271]  # 7 ** 5 and a prime. so certainly relatively prime

GENERATOR_DIVISOR = 2147483647


# 16


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


# 18

DuetInstruction = namedtuple('duetinstruction', ['op', 'x', 'y'])


def parse_duet_instruction(raw_message):
    tokens = raw_message.split()
    if len(tokens) == 3:
        return DuetInstruction(*tokens)
    else:
        return DuetInstruction(*(tokens + [None]))


class DuetMachine:

    def __init__(self, program_id: int, instructions: List[DuetInstruction]) -> None:
        self.registers = defaultdict(int)  # type: Dict[str, int]
        self.registers['p'] = program_id
        self.message_queue = deque()  # type: Sequence[int]
        self.last_message_popped = None  # basically a hack to maintain a solution for p18a
        self.position = 0
        self.instructions = instructions
        self.recipient = self
        self.instructions_count = defaultdict(int)  # type: Dict[str, int]
        self.messages_sent = 0
        self.terminated = False

    def run_instructions(self, break_function=None):
        break_function_triggered = break_function and break_function(self)
        try:
            while self.position < len(self.instructions) + 1 and not break_function_triggered:
                self._process_instruction()
                break_function_triggered = break_function and break_function(self)
        except IndexError:
            return
        self.terminated = True

    def _process_instruction(self):
        register_modifying_operations = {
            'set': lambda x, y: y,
            'add': add,
            'mul': mul,
            'mod': mod,
            'sub': sub
        }

        instruction = self.instructions[self.position]
        x_val = self.registers[instruction.x] if instruction.x.isalpha() else int(instruction.x)
        y_val = instruction.y and (self.registers[instruction.y] if instruction.y.isalpha() else int(instruction.y))
        self.instructions_count[instruction.op] += 1

        if instruction.op in register_modifying_operations:
            f = register_modifying_operations[instruction.op]
            self.registers[instruction.x] = f(x_val, y_val)
            self.position += 1
        elif instruction.op == 'snd':
            self.recipient.message_queue.appendleft(x_val)
            self.position += 1
            self.messages_sent += 1
        elif instruction.op == 'rcv':
            message_in = self.message_queue.pop()
            self.registers[instruction.x] = message_in
            self.last_message_popped = message_in
            self.position += 1
        elif instruction.op == 'jgz':
            step = y_val if x_val > 0 else 1
            self.position += step
        elif instruction.op == 'jnz':
            step = y_val if x_val != 0 else 1
            self.position += step
        else:
            raise NotImplementedError(instruction.op)


# 20


class Particle:

    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.clock = 0

    def __str__(self):
        return "p={0}, v={1}, a={2}".format(self.position, self.velocity, self.acceleration)

    def __repr__(self):
        return str(self)

    def step(self):
        self.clock += 1
        self.velocity = self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1], self.velocity[2] + self.acceleration[2]
        self.position = self.position[0] + self.velocity[0], self.position[1] + self.velocity[1], self.position[2] + self.velocity[2]


def magnitude_manhattan(v):
    return sum(abs(x) for x in v)


def parse_particle(l):
    all_parts = re.split('[<>,]', l)
    relevant_parts = [int(p) for p in all_parts if p and '=' not in p]  # janky!
    return Particle(tuple(relevant_parts[:3]), tuple(relevant_parts[3:6]), tuple(relevant_parts[6:9]))


# 21

def initialize_2d_array(x_size, y_size, initial_val=None):
    matrix = []
    for _ in range(y_size):
        this_row = [initial_val] * x_size
        matrix.append(this_row)
    return matrix


def get_value_at_tuple(grid, t):
    return grid[t[0]][t[1]]


def set_value_at_tuple(grid, t, val):
    grid[t[0]][t[1]] = val
