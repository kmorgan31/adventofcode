#!/usr/bin/python

from aocd import lines


def part_1(data):
    num_code, num_inmem = 0, 0

    for line in data:

        i = 0
        while i < len(line):
            if line[i] == "\"":
                num_code += 1
                i += 1
            elif line[i] == "\\":
                num_code += 1
                if line[i+1] in ["\\", "\""]:
                    num_inmem += 1
                    num_code += 1
                    i += 2
                elif line[i+1] == "x":
                    num_code += 3
                    num_inmem += 1
                    i += 4
            else:
                num_inmem += 1
                num_code += 1
                i += 1
    return num_code - num_inmem


def part_2(data):
    num_code, num_encoded = 0, 0

    for line in data:

        i = 0
        while i < len(line):
            if line[i] == "\"":
                num_encoded += 3
                num_code += 1
                i += 1
            elif line[i] == "\\":
                num_encoded += 3
                num_code += 1
                if line[i+1] in ["\\", "\""]:
                    num_encoded += 1
                    num_code += 1
                    i += 2
                elif line[i+1] == "x":
                    num_encoded += 2
                    num_code += 3
                    i += 4
            else:
                num_encoded += 1
                num_code += 1
                i += 1
    return num_encoded - num_code


if __name__ == '__main__':
    print(f'Part 1 {part_1(lines)}')
    print(f'Part 2 {part_2(lines)}')
