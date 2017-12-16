import sys

from shared import get_separated_rows


def divide_two_divisibles(l):
    l = list(l)
    for left_cur_index, left_cur_val in enumerate(l):
        for right_cur_val in l[left_cur_index+1:]:
            if max(left_cur_val, right_cur_val) % min(left_cur_val, right_cur_val) == 0:
                return max(left_cur_val, right_cur_val) / min(left_cur_val, right_cur_val)


if __name__ == '__main__':
    lines = get_separated_rows(sys.argv[1], sep='\t', func=lambda x: int(x))
    print(sum(divide_two_divisibles(l) for l in lines))
