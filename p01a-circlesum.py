import sys


def get_string(filename):
    with open(filename, 'r') as f:
        raw_contents = f.read()
    return raw_contents


def get_circle_sum(sumstring, debug=False):
    running_sum = 0
    total_length = len(sumstring)
    for i, c in enumerate(sumstring):
        if c == sumstring[(i + 1) % total_length]:
            c_int = int(c)
            running_sum += c_int
        if debug:
            print(running_sum)
            print(sumstring[i:])
    return running_sum


if __name__ == '__main__':
    sumstring = get_string(sys.argv[1])
    debug = len(sys.argv) > 2 and bool(sys.argv[2])
    print(get_circle_sum(sumstring, debug=debug))
