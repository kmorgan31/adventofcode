#!/usr/bin/python

from aocd import lines

import operator as op


OPS_CODES = {
    1: op.add,
    2: op.mul
}


def get_value(line, val, mode):
    return line[val] if mode == 0 else val


def main(line, part=None):
    line = list(map(int, line.split(",")))

    i = 0
    while i < len(line):
        prog = str(line[i]).zfill(5)
        ma, my, mx, op = list(map(int, [prog[0], prog[1], prog[2], prog[3:5]]))

        if OPS_CODES.get(op):
            x, y, z = line[i+1:i+4]
            line[z] = OPS_CODES[op](get_value(line, x, mx), get_value(line, y, my))
            i += 4
        elif op == 3:
            line[line[i+1]] = 1 if part == 1 else 5
            i += 2
        elif op == 4:
            print(get_value(line, line[i+1], mx))
            i += 2
        elif op == 5:
            x, y = line[i+1:i+3]
            i = get_value(line, y, my) if get_value(line, x, mx) != 0 else i + 3
        elif op == 6:
            x, y = line[i+1:i+3]
            i = get_value(line, y, my) if get_value(line, x, mx) == 0 else i + 3
        elif op == 7:
            x, y, z = line[i+1:i+4]
            line[z] = 1 if get_value(line, x, mx) < get_value(line, y, my) else 0
            i += 4
        elif op == 8:
            x, y, z = line[i+1:i+4]
            line[z] = 1 if get_value(line, x, mx) == get_value(line, y, my) else 0
            i += 4
        elif op == 99:
            break


if __name__ == '__main__':
    print(f'Part 1 {main(lines[0], 1)}')
    print(f'Part 2 {main(lines[0], 2)}')
