import sys

from shared import get_exact_rows, magnitude_manhattan, parse_particle


if __name__ == '__main__':
    lines = get_exact_rows(sys.argv[1])
    particles = list((i, parse_particle(l)) for i, l in enumerate(lines))
    closest_particle = min(particles, key=lambda x: (magnitude_manhattan(x[1].acceleration), magnitude_manhattan(x[1].velocity)))
    print(closest_particle)
