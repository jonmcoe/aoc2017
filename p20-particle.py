import math
import re
import sys

import shared


class Particle:

    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.clock = 0

    def __str__(self):
        return "p={0}, v={1}, a={2}".format(self.position, self.velocity, self.acceleration)

    def __repr__(self):
        return str(self)

    def step(self):
        self.clock += 1
        for i in range(len(self.position)):
            self.velocity[i] += self.acceleration[i]
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]


def magnitude_pythag(v):
    return math.sqrt(sum(x * x for x in v))


def magnitude_manhattan(v):
    return sum(abs(x) for x in v)


def parse_particle(l):
    all_parts = re.split('[<>,]', l)
    relevant_parts = [int(p) for p in all_parts if p and '=' not in p]
    return Particle(relevant_parts[:3], relevant_parts[3:6], relevant_parts[6:9])


if __name__ == '__main__':
    lines = shared.get_exact_rows(sys.argv[1])
    particles = list((i, parse_particle(l)) for i, l in enumerate(lines))
    closest_particle = min(particles, key=lambda x: (magnitude_manhattan(x[1].acceleration), magnitude_manhattan(x[1].velocity)))
    print(closest_particle)

    # for _ in range(100000):
    #     if _ % 1000 == 0:
    #         print(_)
    #     for p in particles:
    #         p[1].step()
    # closest_particle = min(particles, key=lambda x: magnitude_manhattan(x[1].position))
    # print(closest_particle)
    #

