#!/usr/bin/python

from aocd import lines

import re

EXAMPLE = [
    "Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
    "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
    "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
    "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
    "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
    "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
    "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
    "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
    "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
    "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
    "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
    "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
    "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
    "Sensor at x=20, y=1: closest beacon is at x=15, y=3"
]


def manhattan_distance(px, py):
    return abs(px[0] - py[0]) + abs(px[1] - py[1])


def get_coord(x, y):
    coords = [i[0] for i in map(lambda s: re.findall(r'-?\d+', s), [x, y])]
    return (int(coords[0]), int(coords[1]))


def main(data, B, part=None):
    sensor_beacon_distance_map = {}

    for line in data:
        line = line.split()
        sensor = get_coord(line[2], line[3])
        beacon = get_coord(line[8], line[9])

        sensor_beacon_distance_map[sensor] = manhattan_distance(sensor, beacon)

    if part == 1:
        return (
            max(k[0] - abs(B - k[1]) + v for k, v in sensor_beacon_distance_map.items()) -
            min(k[0] + abs(B - k[1]) - v for k, v in sensor_beacon_distance_map.items())
        )
    if part == 2:
        for k, v in sensor_beacon_distance_map.items():
            for i, j in sensor_beacon_distance_map.items():
                a = k[0]-k[1]-v
                b = i[0]+i[1]+j
                X, Y = (b+a)//2, (b-a)//2+1

                if not (0 < X < B and 0 < Y <= B):
                    # outside of boundary
                    continue

                if all(
                    manhattan_distance((X, Y), (p[0], p[1])) > q
                    for p, q in sensor_beacon_distance_map.items()
                ):
                    print(4000000*X + Y)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 20, 2)}')
    print(f'Part 1 {main(lines, 2000000, 1)}')
    print(f'Part 2 {main(lines, 4000000, 2)}')
