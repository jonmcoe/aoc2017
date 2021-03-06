import sys

from typing import Dict, Tuple

import shared


if __name__ == '__main__':
    banks = tuple(list(shared.get_separated_rows(sys.argv[1], sep='\t', func=lambda x: int(x)))[0])
    banks_seen = {}  # type: Dict[Tuple[int, ...], int]
    steps = 0
    while banks not in banks_seen:
        banks_seen[banks] = steps
        banks = shared.reallocate_banks(banks)
        steps += 1
    print(steps - banks_seen[banks])
