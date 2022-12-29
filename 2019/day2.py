#!/usr/bin/python

from aocd import lines

import operator as op


EXAMPLE = [
    "1,9,10,3,2,3,11,0,99,30,40,50"
]

OPS_CODES = {
    1: op.add,
    2: op.mul
}

PART_2_OUTPUT = 19690720


def part_1(line):
    line = list(map(int, line.split(",")))

    # update values
    line[1] = 12
    line[2] = 2

    i = 0
    while i < len(line):
        opcode, x, y, z = line[i:i+4]

        if opcode == 99:
            break

        line[z] = OPS_CODES[opcode](line[x], line[y])

        i += 4
    return line[0]


def main(data, part=None):
    ans = part_1(data[0])
    if part == 1:
        return ans

    diff = PART_2_OUTPUT - ans
    noun = diff // 900000
    verb = diff % 10
    return 100 * (noun+12) + (verb+2)


if __name__ == '__main__':
    # print(f'EXAMPLE {main([1969], 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
