#!/usr/bin/python

from aocd import lines


FACING = ["N", "E", "S", "W"]


def manhattan_distance(x, y):
    return abs(x) + abs(y)


def main(data, part=None):
    x, y, facing = 0, 0, "N"

    pos = set()

    directions = data.split(', ')
    for direction in directions:
        if direction[0] == "R":
            facing = FACING[(FACING.index(facing) + 1) % 4]
        else:
            facing = FACING[(FACING.index(facing) - 1) % 4]

        steps = int(direction[1:])
        for i in range(steps):
            if facing == "N":
                x -= 1
            elif facing == "E":
                y += 1
            elif facing == "S":
                x += 1
            elif facing == "W":
                y -= 1

            if (x,y) not in pos:
                pos.add((x,y))
            elif part == 2:
                return manhattan_distance(x, y)

    if part == 1:
        return manhattan_distance(x, y)


if __name__ == '__main__':
    # print(f'Part 1 {main(lines[0], 1)}')
    print(f'Part 2 {main(lines[0], 2)}')
