#!/usr/bin/python

from aocd import lines
from collections import defaultdict


def decrease_lanternfish_days(lanternfish_count):
    babies = lanternfish_count[0]

    for x in range(9):
        lanternfish_count[x] = lanternfish_count[x+1]

    # add new_babies
    lanternfish_count[8] = babies

    # reset moms
    lanternfish_count[6] += babies

    return lanternfish_count


if __name__ == '__main__':
    lanternfish = [x for x in map(int, lines[0].split(','))]

    lanternfish_count = defaultdict(int)
    for x in lanternfish:
        lanternfish_count[x] += 1

    for x in range(256):
        if x == 80:
            part_1 = sum(lanternfish_count.values())
        lanternfish_count = decrease_lanternfish_days(lanternfish_count)

    part_2 = sum(lanternfish_count.values())

    print(f'Day 6: Part 1 {part_1}, Part 2 {part_2}')
