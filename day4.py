#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8"
]


def _range(a):
    return set(range(int(a[0]), a[1]+1))


def _prepare(a):
    x, y = map(int, a.split('-'))
    return (x, y)


def _engulfs(a, b):
    range_a = _range(a)
    range_b = _range(b)
    return range_a.issubset(range_b) or range_b.issubset(range_a)


def _overlaps(a, b):
    range_a = _range(a)
    range_b = _range(b)
    return range_a & range_b

function = {
    1: _engulfs,
    2: _overlaps
}

def main(data, part):
    count = 0

    for line in data:
        a, b = line.split(',')
        if function[part](_prepare(a), _prepare(b)):
            count += 1

    return count


if __name__ == '__main__':
    print(f'Day 1: Part 1 {main(lines, 1)}')
    # print(f'Day 1: Part 2 {part_1(EXAMPLE)}')
    print(f'Day 1: Part 2 {main(lines, 2)}')
