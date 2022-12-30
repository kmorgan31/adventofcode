#!/usr/bin/python

from aocd import lines

import math
from itertools import combinations


EXAMPLE = [
    (-1, 0, 2),
    (2, -10, -7),
    (4, -8, 8),
    (3, 5, -1)
]

INPUT = [
    (-16, -1, -12),
    (0, -4, -17),
    (-11, 11, 0),
    (2, 2, -6)
]


def lcm(a, b):
    return a * b // math.gcd(a, b)


class Moon:

    def __init__(self, num, pos, vel=None):
        x, y, z = pos
        self.num = num
        self.pos = (x, y, z)
        self.vel = vel or (0, 0, 0)

    def apply_velocity(self, vel):
        self.vel = vel
        self.pos = tuple([self.pos[i] + self.vel[i] for i in range(3)])

    def calculate_energy(self):
        return sum(abs(i) for i in self.pos) * sum(abs(i) for i in self.vel)

    def print_moon(self):
        print(f"pos={self.pos}, vel={self.vel}")


def run_steps(pos_vel, steps=float('inf')):
    previous_states = set()

    i = 0
    while i < steps and tuple(pos_vel.items()) not in previous_states:
        # add state to previous states
        previous_states.add(tuple(pos_vel.items()))

        new_velocities = {k: v[1] for k, v in pos_vel.items()}
        for pair in combinations(pos_vel.items(), 2):
            pv1, pv2 = pair

            if pv1[1][0] > pv2[1][0]:
                new_velocities[pv1[0]] -= 1
                new_velocities[pv2[0]] += 1
            elif pv1[1][0] < pv2[1][0]:
                new_velocities[pv1[0]] += 1
                new_velocities[pv2[0]] -= 1

        # update positions; write new velocities of moons
        pos_vel = {
            k: (pos_vel[k][0] + new_velocities[k], new_velocities[k])
            for k in range(len(pos_vel))
        }

        i += 1

    return i, pos_vel


def main(data, steps, part=None):

    # 0: x, 1: y, 2: z
    position_velocities = {
        i: {m: (pos[i], 0) for m, pos in enumerate(data)} for i in range(3)
    }

    if part == 1:
        for x, moon_pv in position_velocities.items():
            _, position_velocities[x] = run_steps(moon_pv, steps)

        # create Moons
        moons = [
            Moon(
                i,
                tuple(position_velocities[j][i][0] for j in range(3)),
                tuple(position_velocities[j][i][1] for j in range(3))
            ) for i in range(4)
        ]

        return sum(m.calculate_energy() for m in moons)

    elif part == 2:
        steps = {}
        for x, moon_pv in position_velocities.items():
            steps[x], position_velocities[x] = run_steps(moon_pv)

        return lcm(lcm(steps[0], steps[1]), steps[2])


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, 1000, 2)}')
    print(f'Part 1 {main(INPUT, 1000, 1)}')
    print(f'Part 2 {main(INPUT, 1000, 2)}')
