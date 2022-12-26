#!/usr/bin/python

from aocd import lines

import re
from itertools import combinations


EXAMPLE = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0"
]

EXAMPLE_2 = [
    "mask = 000000000000000000000000000000X1001X",
    "mem[42] = 100",
    "mask = 00000000000000000000000000000000X0XX",
    "mem[26] = 1"
]


def part_1(data):

    def apply_mask(binval):
        for i, x in mask.items():
            binval[i] = x
        return binval

    mem = {}
    for line in data:
        line = line.split()

        if line[0] == "mask":
            mask = {i: x for i, x in enumerate(line[2]) if x != "X"}

        elif "mem" in line[0]:
            key = int(re.findall(r'\d+', line[0])[0])
            binval = apply_mask(
                list(format(int(line[-1]), "b").zfill(36))
            )
            mem[key] = ''.join(binval)

    return sum(int(v, 2) for v in mem.values())


def part_2(data):
    mem = {}
    for line in data:
        line = line.split()

        if line[0] == "mask":
            mask = {i: x for i, x in enumerate(line[2]) if x != "X"}

        elif "mem" in line[0]:
            key = int(re.findall(r'\d+', line[0])[0])
            binaddress = list(format(key, "b").zfill(36))

            floating_bits = []
            for i in range(36):
                if mask.get(i) == "0":
                    # no change
                    pass
                elif mask.get(i) == "1":
                    binaddress[i] = "1"
                else:
                    floating_bits.append(i)

            addresses = set()
            if floating_bits:
                for perm in set(combinations('01'*len(floating_bits), len(floating_bits))):
                    for i in range(len(perm)):
                        binaddress[floating_bits[i]] = perm[i]
                    addresses.add(''.join(binaddress))
            else:
                addresses.add(''.join(binaddress))

            binval = list(format(int(line[-1]), "b").zfill(36))
            for a in addresses:
                mem[int(a, 2)] = ''.join(binval)

    return sum(int(v, 2) for v in mem.values())


if __name__ == '__main__':
    # print(f'EXAMPLE {part_2(EXAMPLE_2)}')
    print(f'Part 1 {part_1(lines)}')
    print(f'Part 2 {part_2(lines)}')
