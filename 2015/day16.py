#!/usr/bin/python

from aocd import lines


PART_1 = {
    "children": lambda x: x == 3,
    "cats": lambda x: x == 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x == 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x == 5,
    "trees": lambda x: x == 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1
}


PART_2 = {
    "children": lambda x: x == 3,
    "cats": lambda x: x > 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x < 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x < 5,
    "trees": lambda x: x > 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1
}


def main(data, part):
    for line in data:
        line = line.split()

        sue = int(line[1][:-1])
        items = {
            line[2][:-1]: int(line[3][:-1]),
            line[4][:-1]: int(line[5][:-1]),
            line[6][:-1]: int(line[7]),
        }

        if any(not part[k](v) for k, v in items.items()):
            continue

        return sue


if __name__ == '__main__':
    # print(f'Example {part_1(EXAMPLE)}')
    print(f'Part 1 {main(lines, PART_1)}')
    print(f'Part 2 {main(lines, PART_2)}')
