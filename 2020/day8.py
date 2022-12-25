#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6"
]


def parse_instructions(data):
    i = 0
    jmp_nop_idx = []
    instructions = []
    for i in range(len(data)):
        x, y = data[i].split()
        instructions.append((x, int(y)))

        if x in ["jmp", "nop"]:
            jmp_nop_idx.append(i)
    return instructions, jmp_nop_idx


def run_instructions(instructions):
    i = 0
    gv = 0

    visited = set()
    while i not in visited and i < len(instructions):
        visited.add(i)

        action, v = instructions[i]
        if action == "nop":
            i += 1
        elif action == "jmp":
            i += v
        elif action == "acc":
            gv += v
            i += 1

    return i, gv


def switch_action(instructions, idx):
    instructions = instructions[:]
    action, v = instructions[idx]
    if action == "jmp":
        instructions[idx] = ("nop", v)
    elif action == "nop":
        instructions[idx] = ("jmp", v)
    return instructions


def main(data, part=None):
    instructions, jmp_nop_idx = parse_instructions(data)

    if part == 1:
        return run_instructions(instructions)[1]

    elif part == 2:
        for x in jmp_nop_idx:
            new_instructions = switch_action(instructions, x)
            i, gv = run_instructions(new_instructions)
            if i == len(instructions):
                return gv


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
