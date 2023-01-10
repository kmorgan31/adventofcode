#!/usr/bin/python

from aocd import lines

import re
from collections import defaultdict


def main(data, part=None):
    bots = defaultdict(list)
    outputs = defaultdict(list)

    instructions = {}
    for line in data:
        if line.startswith("value"):
            n, b = map(int, re.findall(r'-?\d+', line))
            bots[b].append(n)
        elif line.startswith("bot"):
            who, n1, n2 = map(int, re.findall(r'-?\d+', line))
            t1, t2 = re.findall(r' (bot|output)', line)
            instructions[who] = (t1, n1), (t2, n2)

    while bots:
        for k, v in dict(bots).items():
            if len(v) == 2:
                v = sorted(bots.pop(k))
                if part == 1 and v == [17, 61]: return k

                for ins, z in zip(instructions[k], v):
                    x, y = ins
                    if x == "bot":      bots[y].append(z)
                    if x == "output":   outputs[y].append(z)

    if part == 2:
        return outputs[0][0] * outputs[1][0] * outputs[2][0]


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
