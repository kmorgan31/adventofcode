#!/usr/bin/python

from aocd import lines

import math


EXAMPLE = [
    ".#..##.###...#######",
    "##.############..##.",
    ".#.######.########.#",
    ".###.#######.####.#.",
    "#####.##.#.##.###.##",
    "..#####..#.#########",
    "####################",
    "#.####....###.#.#.##",
    "##.#################",
    "#####.##.###..####..",
    "..######..##.#######",
    "####.##.####...##..#",
    ".#####..#.######.###",
    "##...#.##########...",
    "#.##########.#######",
    ".####.#.###.###.#.##",
    "....##.##.###..#####",
    ".#.#.###########.###",
    "#.#.#.#####.####.###",
    "###.##.####.##.#..##"
]


class Space:

    def __init__(self, data):
        self.asteroids = set()
        for y, line in enumerate(data):
            for x, a in enumerate(line):
                if a == "#":
                    self.asteroids.add((x, y))

    def get_angle(self, a1, a2):
        res = math.atan2(a2[0] - a1[0], a1[1] - a2[1]) * 180 / math.pi
        return 360 + res if res < 0 else res


def manhattan_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def main(data, part=None):
    space = Space(data)

    # get the unique angles from the current asteriod to all other asteroids
    # for all asteroids
    num_asteroids = sorted(
        [
            (a, len({space.get_angle(a, a2) for a2 in space.asteroids if a != a2}))
            for a in space.asteroids
        ], key=lambda x: x[1], reverse=True
    )

    loc, num = num_asteroids[0]
    if part == 1:
        return num

    space.asteroids.remove(loc)

    # get the angles of the asteroids from `loc`, sorted by the manhattan distance
    # from the laser location
    dist_asteroids = sorted(
        [
            (space.get_angle(loc, a), a) for a in space.asteroids
        ], key=lambda x: (x[0], manhattan_distance(loc, x[1]))
    )

    # move laser clockwise and remove entries from dist_asteroids as
    # asteroids are vaporized
    angle_idx = 0
    last_angle, last_a = dist_asteroids.pop(angle_idx)

    count = 1
    while count < 200 and dist_asteroids:
        if angle_idx >= len(dist_asteroids):
            # laser made one circle, restart from beginning of the asteroids
            angle_idx, last_angle = 0, None
        if last_angle == dist_asteroids[angle_idx][0]:
            angle_idx += 1
            continue

        # 'vaporize' the asteroid by moving to the next nearest asteroid
        last_angle, last_a = dist_asteroids.pop(angle_idx)
        count += 1
    return last_a[0] * 100 + last_a[1]


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
