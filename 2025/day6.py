#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data
import math


EXAMPLE = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def parse_equations(data):
    equations = []
    for line in data.split("\n"):
        line = line.split()

        if line[0] == '*' or line[0] == '+':
            operations = line
        else:
            equations.append(line)
    return equations, operations

def part1(data):
    equations, operations = parse_equations(data)

    final_total = 0
    for y in range(len(equations[0])):
        numbers = [int(equations[x][y]) for x in range(len(equations))]

        if operations[y] == "*":
            total = math.prod(numbers)
        elif operations[y] == "+":
            total = sum(numbers)

        final_total += total
    return final_total


def part2(data):
    lines = data.split("\n")

    final_total = 0
    numbers = []
    for y in range(len(lines[0])-1, -1, -1):
        number = "".join([lines[x][y] for x in range(len(lines)-1)])

        if number.isspace():
            print(f"Numbers: {numbers}, operation: {operation}")
            if operation == "*":
                total = math.prod([int(n) for n in numbers])
            elif operation == "+":
                total = sum([int(n) for n in numbers])
            final_total += total

            # reset
            numbers = []
        else:
            numbers.append(number)
            operation = lines[-1][y]

    # last equation
    print(f"Numbers: {numbers}, operation: {operation}")
    if operation == "*":
        total = math.prod([int(n) for n in numbers])
    elif operation == "+":
        total = sum([int(n) for n in numbers])
    final_total += total

    return final_total


if __name__ == '__main__':
    # print(f'Part 1 {part1(EXAMPLE)}')
    # print(f'Part 1 {part1(data)}')
    # print(f'Part 2 {part2(EXAMPLE)}')
    print(f'Part 2 {part2(data)}')
