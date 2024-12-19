#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

from functools import lru_cache


EXAMPLE = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def parse_lines(data):
    lines = data.split("\n")
    return set([x.strip() for x in lines[0].split(",")]), lines[2:]

def part_1(data):
    towels, patterns = parse_lines(data)

    def is_possible(design):
        if len(design) == 0:
            return True

        for t in towels:
            if design.startswith(t) and is_possible(design[len(t):]):
                return True
        return False

    total = 0
    for pattern in patterns:
        total += 1 if is_possible(pattern) else 0
    return total

def part_2(data):
    towels, patterns = parse_lines(data)

    @lru_cache
    def is_possible(design):
        if len(design) == 0:
            return 1

        total = 0
        for t in towels:
            if design.startswith(t):
                total += is_possible(design[len(t):])
        return total

    total = 0
    for pattern in patterns:
        total += is_possible(pattern)
    return total


if __name__ == '__main__':
    print(f'Part 1 {part_1(EXAMPLE)}')
    print(f'Part 1 {part_1(data)}')
    print(f'Part 2 {part_2(EXAMPLE)}')
    print(f'Part 2 {part_2(data)}')
