#!/usr/bin/python

from aocd import lines

import re

EXAMPLE = [
    "FBFBBFFRLR",
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"
]


def main(data, part=None):

    seat_ids = []
    for line in data:
        x, y = line[:7], line[7:]

        # find row
        lx, ux = 0, 127
        for i in x:
            mid = (ux + lx)//2
            if i == "F":
                ux = mid
            elif i == "B":
                lx = mid+1

        # find col
        ly, uy = 0, 7
        for i in y:
            mid = (uy + ly)//2
            if i == "L":
                uy = mid
            elif i == "R":
                ly = mid+1

        seat_ids.append((lx * 8) + ly)

    seat_ids.sort()
    if part == 1:
        return seat_ids[-1]
    elif part == 2:
        for i in range(1, len(seat_ids)-2):
            if abs(seat_ids[i] - seat_ids[i+1]) == 2:
                return seat_ids[i]+1


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
