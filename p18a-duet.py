import sys

from shared import get_exact_rows, parse_duet_instruction, DuetMachine


if __name__ == '__main__':
    instructions = [parse_duet_instruction(l) for l in get_exact_rows(sys.argv[1])]
    dm = DuetMachine(0, instructions)
    dm.run_instructions(break_function=lambda s: s.last_message_popped is not None)
    print(dm.last_message_popped)
