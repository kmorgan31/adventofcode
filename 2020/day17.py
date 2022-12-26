#!/usr/bin/python

from aocd import lines

from itertools import combinations


EXAMPLE = [
    ".#.",
    "..#",
    "###"
]


def parse_data(data, part):
    active = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "#":
                if part == 1:
                    active.add((i, j, 0))
                elif part == 2:
                    active.add((i, j, 0, 0))
    return active


def part_1(active):
    def get_surrounding_points(pos):
        x, y, z = pos
        return set(
            [(i, j, k) for i in (x-1, x, x+1) for j in (y-1, y, y+1) for k in (z-1, z, z+1)]
        ) - {pos}

    for x in range(6):
        xvals = [x[0] for x in active]
        yvals = [x[1] for x in active]
        zvals = [x[2] for x in active]

        new_active = set()
        for x in range(min(xvals)-1, max(xvals)+2):
            for y in range(min(yvals)-1, max(yvals)+2):
                for z in range(min(zvals)-1, max(zvals)+2):
                    surrounding_points = get_surrounding_points((x, y, z))

                    num_surrounding_active = len(surrounding_points & active)
                    if (x,y,z) not in active and num_surrounding_active == 3:
                        new_active.add((x,y,z))
                    elif (x,y,z) in active and num_surrounding_active in [2, 3]:
                        new_active.add((x,y,z))
        active = new_active
    return len(active)


def part_2(active):
    def get_surrounding_points(pos):
        x, y, z, w = pos
        return set([
            (i, j, k, l)
            for i in (x-1, x, x+1)
            for j in (y-1, y, y+1)
            for k in (z-1, z, z+1)
            for l in (w-1, w, w+1)
        ]) - {pos}

    for x in range(6):
        xvals = [x[0] for x in active]
        yvals = [x[1] for x in active]
        zvals = [x[2] for x in active]
        wvals = [x[3] for x in active]

        new_active = set()
        for x in range(min(xvals)-1, max(xvals)+2):
            for y in range(min(yvals)-1, max(yvals)+2):
                for z in range(min(zvals)-1, max(zvals)+2):
                    for w in range(min(wvals)-1, max(wvals)+2):
                        surrounding_points = get_surrounding_points((x, y, z, w))

                        num_surrounding_active = len(surrounding_points & active)
                        if (x,y,z,w) not in active and num_surrounding_active == 3:
                            new_active.add((x,y,z,w))
                        elif (x,y,z,w) in active and num_surrounding_active in [2, 3]:
                            new_active.add((x,y,z,w))
        active = new_active
    return len(active)


def main(data, part=None):
    return (part_1 if part == 1 else part_2)(parse_data(data, part))


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
