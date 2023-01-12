#!/usr/bin/python

from aocd import lines

from itertools import permutations

EXAMPLE = [
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141",
]


def main(data, part=None):
    dist = {}
    nodes = set()
    for line in data:
        line = line.split()

        nodes.add(line[0])
        nodes.add(line[2])

        dist[(line[0], line[2])] = int(line[4])
        dist[(line[2], line[0])] = int(line[4])

    target_steps = 99999999 if part == 1 else 0
    for path in permutations(nodes):
        steps = 0
        for i in range(len(path)-1):
            steps += dist[(path[i], path[i+1])]

        if part == 1:
            target_steps = min(target_steps, steps)
        elif part == 2:
            target_steps = max(target_steps, steps)
    return target_steps


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
