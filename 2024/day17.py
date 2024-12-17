#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data


EXAMPLE = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

EXAMPLE_2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""


def get_combo(operand, a, b, c):
    if operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c

def get_program(data):
    lines = data.split("\n")
    return list(map(int, lines[4].split(":")[1].split(",")))

def get_a(data):
    lines = data.split("\n")
    return int(lines[0].split(":")[1])


def run_program(program, a):
    out = []
    b, c = 0, 0

    idx = 0
    while idx < len(program)-1:
        opcode, operand = program[idx:idx+2]
        if opcode == 0:
            # adv - division
            a //= (1 << get_combo(operand, a, b, c))
        elif opcode == 1:
            # bxl - bitwise XOR: b and operand
            b ^= operand
        elif opcode == 2:
            # bst - combo % 8
            b = get_combo(operand, a, b, c) % 8
        elif opcode == 3 and a != 0:
            # jnz - nothing if a == 0; else jump idx to operand
            idx = operand
            continue
        elif opcode == 4:
            # bxc - bitwise XOR: b and c
            b ^= c
        elif opcode == 5:
            # out - outputs combo % 8
            out.append(get_combo(operand, a, b, c) % 8)
        elif opcode == 6:
            # bdv - outputs combo % 8
            b = a // (1 << get_combo(operand, a, b, c))
        elif opcode == 7:
            # cdv - outputs combo % 8
            c = a // (1 << get_combo(operand, a, b, c))
        idx += 2

    return out


def part_1(data):
    out = run_program(get_program(data), get_a(data))
    return ",".join(map(str, out))


def part_2(data):
    # reverse-engineer from answer to a
    queue = list(range(8)) # 3 bits

    program = get_program(data)
    for i in range(len(program)):
        valid = []
        for q in queue:
            out = run_program(program, q)
            if out[0] == program[-(i+1)]:
                valid.append(q)

        # go to next bit in output
        queue = [v * 8 + j for j in range(8) for v in valid]

    return min(valid)


if __name__ == '__main__':
    print(f'Part 1 {part_1(EXAMPLE)}')
    print(f'Part 1 {part_1(data)}')
    print(f'Part 2 {part_2(EXAMPLE_2)}')
    print(f'Part 2 {part_2(data)}')
