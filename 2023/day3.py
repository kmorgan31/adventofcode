#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5fc4d1838d6c26850845cb7f79b05413c2b6943f5e387aad806bbd2298cce594f8f0cd7053b0191c213323b1295f5491f6b5295c984461a77a

from aocd import lines

import re
# from typing import Generator, Tuple, List

EXAMPLE = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]


def is_symbol(x):
    return x != "." and not x.isdigit()


def get_numbers(data):
    """
    Generates tuples containing the line index, line content, start index, end index, and number for each number in the lines.
    """
    for i, line in enumerate(data):
        # Loop over each number in the line
        for match in re.finditer(r"\d+", line):
            start_index = match.start(0) - 1
            end_index = match.end(0)
            number = int(match.group(0))
            yield i, line, start_index, end_index, number


def get_parts(data):
    """
    Extracts the parts from the lines.
    """
    parts = []
    for i, line in enumerate(data):
        parts.append([])

        # Find all numbers in the line
        for match in re.finditer(r"\d+", line):
            start_index = match.start(0) - 1
            end_index = match.end(0)
            number = int(match.group(0))
            part = (start_index, end_index, number)
            parts[i].append(part)

    return parts


def part_1(data):
    count = 0
    for (i, line, start_index, end_index, number) in get_numbers(data):
        # Check if number is not surrounded by symbols
        if (start_index >= 0 and is_symbol(line[start_index])) or (
            end_index < len(line) and is_symbol(line[end_index])
        ):
            count += number
            continue

        # Check if number is surrounded by symbols on the line above or below
        # the current line
        # loop over each digit in the number
        for j in range(start_index, end_index + 1):
            # Check if we are at the end of the line
            if j >= len(line):
                continue

            # Check the line above and below for symbols
            if (i > 0 and is_symbol(data[i - 1][j])) or (
                i < len(data) - 2 and is_symbol(data[i + 1][j])
            ):
                count += number
                break
    return count


def part_2(data):
    count = 0
    parts = get_parts(data)

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char != "*":
                continue

            adjacent_parts = []

            # Loop over the line above, the current line, and the line below
            for k in range(-1, 2):
                # Check if the line exists
                if i + k < 0 or i + k > len(data):
                    continue

                # Loop over each part in the line
                for start_index, end_index, number in parts[i + k]:
                    if start_index <= j <= end_index:
                        adjacent_parts.append(number)

            # If there are two adjacent parts, multiply them and add to the count
            if len(adjacent_parts) == 2:
                count += adjacent_parts[0] * adjacent_parts[1]
    return count

if __name__ == '__main__':
    print(f'Day 3: Part 1 {part_1(lines)}')
    print(f'Day 3: Part 2 {part_2(lines)}')
