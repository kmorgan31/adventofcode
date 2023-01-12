#!/usr/bin/python

from aocd import lines

import re

EXAMPLE = [
    "2x3x4",
    "1x1x10"
]


def calculate_surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l


def smallest_side_area(l, w, h):
    return min([l*w, w*h, h*l])


def calculate_ribbon_length(l, w, h):
    sorted_by_size = sorted([l, w, h])

    present = 2*sorted_by_size[0] + 2*sorted_by_size[1]
    bow = l * w * h
    return present + bow


def main(data, part=None):
    total = 0

    for line in data:
        l, w, h = map(int, re.findall(r'\d+', line))

        if part == 1:
            total += calculate_surface_area(l, w, h) + smallest_side_area(l, w, h)
        elif part == 2:
            total += calculate_ribbon_length(l, w, h)

    return total


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
