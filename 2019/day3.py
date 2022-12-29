#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "R8,U5,L5,D3",
    "U7,R6,D4,L4"
]

EXAMPLE_2 = [
    "R75,D30,R83,U83,L12,D49,R71,U7,L72",
    "U62,R66,U55,R34,D71,R55,D58,R83"
]


def get_wire(directions):
    wire = []

    x, y = 0, 0
    for d in directions:
        spaces = int(d[1:])
        if d[0] == "R":
            wire.extend((x, i) for i in range(y+1, y+spaces+1))
            y += spaces
        elif d[0] == "L":
            wire.extend((x, i) for i in range(y-1, y-spaces-1, -1))
            y -= spaces
        elif d[0] == "D":
            wire.extend((j, y) for j in range(x+1, x+spaces+1))
            x += spaces
        elif d[0] == "U":
            wire.extend((j, y) for j in range(x-1, x-spaces-1, -1))
            x -= spaces
    return wire


def closest_overlap(overlaps):
    closest = (9999, (0, 0))
    for x, y in overlaps:
        dist = abs(x) + abs(y)
        if dist <= closest[0]:
            closest = (dist, (x, y))
    return closest


def manhattan_distance(x, y):
    return abs(x) + abs(y)


def main(data, part=None):
    wire_1, wire_2 = [get_wire(line.split(",")) for line in data]
    overlaps = set(wire_1) & set(wire_2)

    if part == 1:
        return min(manhattan_distance(x, y) for x, y in overlaps)
    elif part == 2:
        return min(
            sum(wire.index(x)+1 for wire in [wire_1, wire_2]) for x in overlaps
        )


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE_2, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
