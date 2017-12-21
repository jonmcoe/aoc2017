import sys

from shared import get_exact_rows, parse_particle


if __name__ == '__main__':
    lines = get_exact_rows(sys.argv[1])
    particles_dict = dict((i, parse_particle(l)) for i, l in enumerate(lines))

    for _ in range(10000):
        position_to_particle_id = {}
        deletion_set = set()
        # if _ % 1000 == 0:
        #     print(_)
        for p_id, particle in particles_dict.items():
            particle.step()
            if particle.position in position_to_particle_id:
                deletion_set.add(p_id)
                deletion_set.add(position_to_particle_id[particle.position])
            else:
                position_to_particle_id[particle.position] = p_id
        for deletion_candidate in deletion_set:
            del particles_dict[deletion_candidate]
    print(len(particles_dict))
