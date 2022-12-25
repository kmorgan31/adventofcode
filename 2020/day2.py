#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]


def main(data, part=None):

    valid = 0
    for line in data:
        line = line.split()
        lb, ub = map(int, line[0].split("-"))
        x = line[1][0]

        if part == 1 and lb <= line[2].count(x) <= ub:
            valid += 1
        elif part == 2 and [line[2][lb-1], line[2][ub-1]].count(x) == 1:
            valid += 1
    return valid


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
