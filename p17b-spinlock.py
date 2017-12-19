import sys

import shared


def spin_lock(index_of_interest, step_size, iterations):
    cursor = 0
    answer = None
    for current_val in range(1, iterations + 1):
        cursor = (cursor + step_size) % current_val + 1
        if cursor == index_of_interest:
            answer = current_val
    return answer


if __name__ == '__main__':
    step_size = int(shared.get_string(sys.argv[1]).strip())
    print(spin_lock(1, step_size, 50 * 10 ** 6))
