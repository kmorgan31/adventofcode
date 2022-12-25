#!/usr/bin/python

from aocd import lines

from math import prod
from itertools import combinations

EXAMPLE = [
    "1721",
    "979",
    "366",
    "299",
    "675",
    "1456"
]


def main(data, c):
    for x in combinations(map(int, data), c):
        if sum(x) == 2020:
            return prod(x)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 2)}')
    print(f'Part 2 {main(lines, 3)}')
