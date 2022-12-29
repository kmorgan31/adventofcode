#!/usr/bin/python

from aocd import lines

import operator as op


OPS_CODES = {
    1: op.add,
    2: op.mul
}


def get_value(line, val, mode):
    return line[val] if mode == 0 else val


def part_1(line):
    line = list(map(int, line.split(",")))

    i = 0
    while i < len(line):
        prog = str(line[i]).zfill(5)
        ma, mb, mc, op = prog[0], prog[1], prog[2], prog[3:5]

        if OPS_CODES.get(int(op)):
            x, y, z = line[i+1:i+4]
            line[z] = OPS_CODES[int(op)](
                get_value(line, x, mc), get_value(line, y, mb)
            )
            i += 4
        elif int(op) == 3:
            line[line[i+1]] = 1
            i += 2
        elif int(op) == 4:
            print(line[line[i+1]])
            i += 2
        elif int(op) == 99:
            break


def main(data, part=None):
    part_1(data[0])


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    # print(f'Part 2 {main(lines, 2)}')
