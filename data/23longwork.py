import math


def prime(x):
    if x < 2:
        return False
    return not any(x % d == 0 for d in range(2, int(math.sqrt(x) + 2)))


# value initialization
a = 1  # from written instructions for part 2
b = 81
c = b
if a != 0:
    b *= 100
    b += 100000
    c = b + 17000

# start main loop
h = 0

# while True:
for b in range(b, c + 1, 17):
    if not prime(b):
        h += 1

    # # becomes f == int(prime(b))
    # f = 1
    # for d in range(2, b + 1):
    #     for e in range(2, b + 1)
    #         if d * e == b:
    #             f = 0
    #
    # # can kill short-lived f and instead immediately increment h
    # if f != 0:
    #     h += 1

    # # can turn this stuff and the while into a for/range
    # if b == c:
    #     break
    # b += 17

print(h)