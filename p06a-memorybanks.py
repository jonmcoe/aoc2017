import sys

import shared


if __name__ == '__main__':
    banks = tuple(list(shared.get_separated_rows(sys.argv[1], sep='\t', func=lambda x: int(x)))[0])
    banks_seen = set()
    steps = 0
    while banks not in banks_seen:
        banks_seen.add(banks)
        banks = shared.reallocate_banks(banks)
        steps += 1
    print(steps)
