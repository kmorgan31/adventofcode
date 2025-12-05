#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data
import math


EXAMPLE = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def parse_topology_map(data):
    return [list(line) for line in data.split("\n")]

def get_surrounding_points(x, y, topology_map):
    points = [
        (x-1, y),
        (x-1, y+1),
        (x-1, y-1),
        (x, y+1),
        (x, y-1),
        (x+1, y),
        (x+1, y-1),
        (x+1, y+1)
    ]
    return [(i, j) for i,j in points if i >= 0 and i < len(topology_map) and j >= 0 and j < len(topology_map[0])]

def main(data, part):
    topology_map = parse_topology_map(data)

    total_removed = 0

    while True:
        new_total_removed = 0
        for x in range(len(topology_map)):
            for y in range(len(topology_map[x])):
                if topology_map[x][y] != "@":
                    continue

                if sum([topology_map[i][j] == "@" for i,j in get_surrounding_points(x, y, topology_map)]) < 4:
                    total_removed += 1
                    new_total_removed += 1
                    if part == 2:
                        topology_map[x][y] = "."
        if new_total_removed == 0:
            break
    return total_removed


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, 1)}')
    # print(f'Part 1 {main(data, 1)}')
    # print(f'Part 2 {main(EXAMPLE, 2)}')
    print(f'Part 2 {main(data, 2)}')
