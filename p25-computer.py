import sys
from collections import defaultdict, namedtuple

from typing import Dict, Iterator, Tuple

import shared


Maneuver = namedtuple('Maneuver', ['write_value', 'tape_step', 'next_state'])


Instruction = Tuple[Maneuver, Maneuver]


Instructions = Dict[str, Instruction]


class Computer:

    def __init__(self, instructions: Instructions, starting_state: str) -> None:
        self.tape = defaultdict(int)  # type: Dict[int, int]
        self.position = 0
        self.instructions = instructions
        self.state = starting_state
        self.running_sum = 0

    def run_step(self) -> None:
        tape_value_before = self.tape[self.position]
        current_instruction = self.instructions[self.state][tape_value_before]
        self.tape[self.position] = current_instruction.write_value
        self.running_sum += (current_instruction.write_value - tape_value_before)
        self.position += current_instruction.tape_step
        self.state = current_instruction.next_state


def parse_single_instruction(lines_iterator: Iterator[str]) -> Tuple[str, Instruction]:
    # this could be better...

    next(raw_lines_iterator)  # expected blank line
    l = next(lines_iterator)
    current_state = l[-2]

    next(lines_iterator)  # 0 always comes before 1
    write_value = int(next(lines_iterator)[-2])
    tape_step = {'right': 1, 'left': -1}[next(lines_iterator).split()[-1][:-1]]
    next_state = next(lines_iterator)[-2]
    maneuver0 = Maneuver(write_value, tape_step, next_state)

    next(lines_iterator)  # 1 always comes after 0
    write_value = int(next(lines_iterator)[-2])
    tape_step = {'right': 1, 'left': -1}[next(lines_iterator).split()[-1][:-1]]
    next_state = next(lines_iterator)[-2]
    maneuver1 = Maneuver(write_value, tape_step, next_state)
    return current_state, (maneuver0, maneuver1)


def parse_instructions(lines_iterator: Iterator[str]) -> Instructions:
    instructions_out = {}
    try:
        while True:
            state_letter, new_instruction = parse_single_instruction(lines_iterator)
            instructions_out[state_letter] = new_instruction
    except StopIteration:
        pass
    return instructions_out


if __name__ == '__main__':
    raw_lines_iterator = shared.get_exact_rows(sys.argv[1])
    starting_state = next(raw_lines_iterator)[-2]
    checksum_amount = int(next(raw_lines_iterator).split()[-2])
    parsed_instructions = parse_instructions(raw_lines_iterator)
    computer = Computer(parsed_instructions, starting_state)
    for _ in range(checksum_amount):
        computer.run_step()
    print(computer.running_sum)