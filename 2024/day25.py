#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

from collections import defaultdict


EXAMPLE = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""
    

def read_schematic(schematic):
    coords = defaultdict(int)
    for x in range(len(schematic)):
        for y in range(len(schematic[0])):
            if schematic[x][y] == "#":
                coords[y] += 1
    return tuple([coords[x] for x in range(5)])


def main(data):
    locks, keys = [], []
    lines = data.splitlines()
    for x in range(0, len(lines), 8):
        if lines[x] == ".....":
            keys.append(read_schematic(lines[x: x+7]))
        else:
            locks.append(read_schematic(lines[x: x+7]))

    total = 0
    for x in locks:
        for y in keys:
            if all([x[i] + y[i] <= 7 for i in range(5)]):
                total += 1
    return total


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE)}')
    print(f'Part 1 {main(data)}')
