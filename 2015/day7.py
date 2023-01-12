#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i"
]


def get_val(x, wires):
    return int(x) if x.isdigit() else wires[x]


def main(data, part=None):
    wires = {}

    while data:
        line = data.pop(0)

        nline = line.split()
        command, dest = nline[:-1], nline[-1]

        if part == 2 and dest == 'b':
            # override wire 'b'
            wires['b'] = 956
            continue

        ars = [x for x in command if x.islower() or x.isdigit()]
        op = [x for x in command if not (x.islower() or x.isdigit() or x == "->")]

        reg_ars = [a for a in ars if not a.isdigit()]
        if set(reg_ars) - set(wires):
            # values for the necessary ars' wires have not been found
            # add line back to data
            data.append(line)
            continue

        if len(ars) == 1:
            if not op:
                # assignment
                wires[dest] = get_val(ars[0], wires)
            elif op[0] == "NOT":
                wires[dest] = 65535 - get_val(ars[0], wires)
        else:
            x, y = ars
            if op[0] == "AND":
                wires[dest] = get_val(x, wires) & get_val(y, wires)
            elif op[0] == "OR":
                wires[dest] = get_val(x, wires) | get_val(y, wires)
            elif op[0] == "LSHIFT":
                wires[dest] = get_val(x, wires) << get_val(y, wires)
            elif op[0] == "RSHIFT":
                wires[dest] = get_val(x, wires) >> get_val(y, wires)

    return wires['a'] if part else wires


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
