#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "cpy 41 a",
    "inc a",
    "inc a",
    "dec a",
    "jnz a 2",
    "dec a",
]


def get_val(x, registers):
    try:
        return int(x)
    except:
        return registers[x]


def main(data, part=None):
    registers = {"a": 0, "b": 0}

    if part == 2:
        registers["a"] = 1

    i = 0
    while i < len(data):
        print(f"Line {i+1}: {data[i]} - {registers}")
        line = data[i].split()
        action, params = line[0], line[1:]

        if action == "hlf":
            registers[params[0]] /= 2
        if action == "tpl":
            registers[params[0]] *= 3
        if action == "inc":
            registers[params[0]] += 1
        if action == "jmp":
            i += int(params[0])
            continue
        if action == "jie":
            x, y = params[0][:-1], int(params[1])
            if registers[x] % 2 == 0:
                i += y
                continue
        if action == "jio":
            x, y = params[0][:-1], int(params[1])
            if registers[x] == 1:
                i += y
                continue
        i += 1
    return registers['b']


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    # print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
