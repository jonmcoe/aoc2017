import string


# 1


def get_string(filename):
    with open(filename, 'r') as f:
        raw_contents = f.read()
    return raw_contents


def get_circle_sum(sumstring, counterpart_func, debug=False):
    running_sum = 0
    total_length = len(sumstring)
    for i, c in enumerate(sumstring):
        if c == sumstring[counterpart_func(i, total_length)]:
            c_int = int(c)
            running_sum += c_int
        if debug:
            print(running_sum)
            print(sumstring[i:])
    return running_sum


#2

class DancerLineup(object):

    def __init__(self, n):
        self._offset = 0
        self._number_of_dancers = n
        self._dancers = list(string.ascii_lowercase[:n])
        # self._name_to_index = {
        #     k: v for v, k in enumerate(self._dancers)
        # }

    def __str__(self):
        return ''.join(self._dancers[i - self._offset] for i in range(self._number_of_dancers))

    def spin(self, step):
        self._offset += step
        self._offset %= self._number_of_dancers

    def exchange(self, first_index, second_index):
        internal_first_index = first_index - self._offset
        internal_second_index = second_index - self._offset
        self._dumb_swap(internal_first_index , internal_second_index)
        # self._name_to_index[self._dancers[internal_first_index]]

    def partner(self, first_name, second_name):
        internal_first_index = self._dancers.index(first_name)
        internal_second_index = self._dancers.index(second_name)
        self._dumb_swap(internal_first_index, internal_second_index)

    def _dumb_swap(self, first_index, second_index):
        self._dancers[first_index], self._dancers[second_index] = self._dancers[second_index], self._dancers[first_index]

    def process_move(self, movestring):
        move_func = {
            's': self.spin,
            'x': self.exchange,
            'p': self.partner
        }[movestring[0]]
        args = movestring[1:].split('/')
        args = [(int(a) if a.isdigit() else a) for a in args]
        move_func(*args)


# CHARACTER_TO_FUNCTION = {
#     's': spin,
#     'x': exchange,
#     'p': partner
# }


def get_moves(filename):
    with open(filename, 'r') as f:
        raw_contents = f.read()
    return raw_contents.split(',')
