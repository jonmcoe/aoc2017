import sys

import shared


if __name__ == '__main__':
    instructions = [int(x) for x in shared.get_string(sys.argv[1]).split('\n')]
    print(shared.run_instructions(instructions, lambda x: x - 1 if x >= 3 else x + 1))
