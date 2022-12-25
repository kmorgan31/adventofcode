#!/usr/bin/python

from aocd import lines


def part_1(data):
    horizontal, depth = 0, 0
    for action in data:
        direction, x = action.split()

        amount = int(x)
        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount

    return horizontal * depth


def part_2(data):
    horizontal, depth, aim = 0, 0, 0
    for action in data:
        direction, x = action.split()

        amount = int(x)
        if direction == "forward":
            horizontal += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount

    return horizontal * depth


if __name__ == '__main__':
    print(f'Day 2: Part 1 {part_1(lines)}, Part 2 {part_2(lines)}')
