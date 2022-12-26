#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "939",
    "7,13,x,x,59,x,31,19"
]


def part_1(data):
    ts = int(data[0])
    buses = [int(x) for x in data[1].split(',') if x.isdigit()]

    while True:
        for b in buses:
            if ts % b == 0:
                return b*(ts-int(data[0]))
        ts += 1


def part_2(data):
    buses = [(i, int(x)) for i, x in enumerate(data[1].split(',')) if x != "x"]

    i, d = 0, 1
    for offset, b in buses:
        while True:
            i += d
            if (i + offset) % b == 0:
                d *= b
                break
    return i


if __name__ == '__main__':
    # print(f'EXAMPLE {part_2(EXAMPLE)}')
    print(f'Part 1 {part_1(lines)}')
    print(f'Part 2 {part_2(lines)}')
