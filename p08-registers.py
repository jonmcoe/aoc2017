import sys

from shared import get_exact_rows, parse_instruction, RegisterMachine


if __name__ == '__main__':
    instructions = [parse_instruction(i) for i in get_exact_rows(sys.argv[1])]
    rm = RegisterMachine()
    for i in instructions:
        rm.process_instruction(i)
    print(rm.get_max_register())
    print(rm.max_ever)

