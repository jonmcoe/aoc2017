import sys

from shared import get_exact_rows, parse_duet_instruction, DuetMachine


if __name__ == '__main__':
    instructions = [parse_duet_instruction(l) for l in get_exact_rows(sys.argv[1])]
    dm = DuetMachine(instructions)
    dm.run_instructions(break_function=lambda s: len(s.recovered_sounds) > 0)
    print(dm.recovered_sounds)
