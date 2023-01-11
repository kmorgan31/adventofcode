#!/usr/bin/python

import re
from itertools import permutations

from aocd import lines


class File:

    def __init__(self, x, y, size, used, avail, use_percent):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail
        self.use_percent = use_percent


def print_filesystem(filesystem, pos=None):
    xvals = [x for x,y in filesystem]
    yvals = [y for x,y in filesystem]

    for j in range(min(yvals), max(yvals)+1):
        line = []
        for i in range(min(xvals), max(xvals)+1):
            file = filesystem[(i,j)]
            if (i,j) == pos:
                line.append("P")
            elif (i,j) == (max(xvals), 0):
                line.append("G")
            elif (i,j) == (0,0):
                line.append("S")
            elif file.used == 0 and not pos:
                line.append("_")
            elif file.used > 88:
                line.append("#")
            else:
                line.append(".")
        print(' '.join(line))
    print()


def get_empty_pos(filesystem):
    xvals = [x for x,y in filesystem]
    yvals = [y for x,y in filesystem]

    for j in range(min(yvals), max(yvals)+1):
        for i in range(min(xvals), max(xvals)+1):
            file = filesystem[(i,j)]
            if file.used == 0:
                return (i,j)


def get_large_pos(filesystem):
    xvals = [x for x,y in filesystem]
    yvals = [y for x,y in filesystem]

    ans = []
    for j in range(min(yvals), max(yvals)+1):
        for i in range(min(xvals), max(xvals)+1):
            file = filesystem[(i,j)]
            if file.used > 88:
                ans.append((i,j))
    return ans


def main(data, part=None):

    filesystem = {}
    for line in data[2:]:
        nums = list(map(int, re.findall(r'\d+', line)))
        filesystem[(nums[0], nums[1])] = File(*nums)

    if part == 1:
        num_viable = 0
        for p1, p2 in permutations(filesystem.values(), 2):
            if p1.used != 0 and p1.used <= p2.avail:
                num_viable += 1
        return num_viable

    elif part == 2:
        print_filesystem(filesystem)

        # get position of empty pos
        ex, ey = get_empty_pos(filesystem)

        # get position of immovable pos (walls)
        wall = get_large_pos(filesystem)
        edge_of_wall = min(wall)

        num_steps = 0
        num_steps += ex - edge_of_wall[0]+1     # get past edge of wall
        num_steps += ey                         # get to the top of grid
        num_steps += 38 - (edge_of_wall[0]-1)   # get to right edge of grid
        num_steps += (5*37)                     # shift G to top-left edge

        return num_steps


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
