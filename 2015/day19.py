#!/usr/bin/python

from aocd import lines

import re

from collections import defaultdict

EXAMPLE = "HOH"

RULES = [
    "H => HO",
    "H => OH",
    "O => HH",
    "e => H",
    "e => O"
]

INPUT = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"


def get_all_indexes(molecule, el):
    indexes = []

    start = 0
    while molecule.find(el, start) >= 0:
        idx = molecule.find(el, start)
        indexes.append(idx)
        start = idx + 1
    return indexes


def get_new_molecule(molecule, start_idx, el, new_el):
    return molecule[:start_idx] + new_el + molecule[start_idx+len(el):]


def get_rules(data):
    rules = defaultdict(list)
    for line in data:
        if not line:
            break

        line = line.split()
        rules[line[0]].append(line[2])
    return rules


def part_1(data, molecule):
    molecules = set()

    rules = get_rules(data)
    for k, v in rules.items():
        indexes = get_all_indexes(molecule, k)
        for z in v:
            for i in indexes:
                molecules.add(get_new_molecule(molecule, i, k, z))

    return len(molecules)


part_2_rules = {}
for line in lines:
    if not line:
        break
    line = line.split()
    part_2_rules[line[2]] = line[0]

# A* search to find the recipe length
def part_2(seed, length=0):
    if seed == "e":
        return length

    # Grab the possible next steps
    next_steps = set()
    for initial, replacement in part_2_rules.items():
        for m in re.finditer(initial, seed):
            next_steps.add(seed[: m.span()[0]] + replacement + seed[m.span()[1] :])

    # A* bit... sort the options by estimated cost (use length as proxy)
    next_steps = sorted(sorted(next_steps, reverse=True), key=len)

    # Try the next steps until we find one that isn't a dead end
    if next_steps:
        return part_2(next_steps.pop(0), length + 1)


if __name__ == '__main__':
    # print(f'Example {part_1(RULES, EXAMPLE)}')
    print(f'Part 1 {part_1(lines, INPUT)}')
    print(f'Part 2 {part_2(INPUT)}')
