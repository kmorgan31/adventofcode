#!/usr/bin/python

from aocd import lines

from functools import reduce
from itertools import permutations
from math import floor, ceil


def get_flattened_lines(data):
    flattened_lines = []
    for line in data:
        flatline = []
        depth = 0

        for c in line:
            if c == '[':
                # entering nested list
                depth += 1
            elif c == ']':
                # closing nested list
                depth -= 1
            elif c.isdigit():
                # add entry to flatline at depth
                flatline.append((int(c), depth))
        flattened_lines.append(flatline)
    return flattened_lines


def explode(line):
    # analyzes pairs of numbers in line to determine depth of original nested pair to explode
    for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(line, line[1:])):
        if depth1 < 5 or depth1 != depth2:
            continue

        if i > 0:
            # add num1 to the entry to the left
            line[i-1] = (line[i-1][0] + num1, line[i-1][1])
        if i < len(line) - 2:
            # add num2 to the entry to the right
            line[i+2] = (line[i+2][0] + num2, line[i+2][1])

        # return line after explosion
        return True, line[:i] + [(0, depth1-1)] + line[i+2:]
    return False, line


def split(line):
    for i, (num, depth) in enumerate(line):
        if num < 10:
            continue

        split_rounded_down = floor(num / 2.0)
        split_rounded_up = ceil(num / 2.0)

        return True, (
            line[:i] +
            [(split_rounded_down, depth+1), (split_rounded_up, depth+1)] +
            line[i+1:]
        )
    return False, line


def add(line1, line2):
    # combine num1 and num2, increasing depth of all nums
    line = [(num, depth+1) for num, depth in line1 + line2]
    while True:
        # explode any pairs
        changed, line = explode(line)
        if changed:
            # repeat loop and try exploding again
            continue

        # split any pairs
        changed, line = split(line)
        if not changed:
            # nothing to split, leave loop
            break

    return line


def calculate_magnitude(line):
    while len(line) > 1:
        # analyzes pairs of numbers in line to match depths of original nested pair to calculate
        for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(line, line[1:])):
            if depth1 != depth2:
                continue
            magnitude = (3 * num1) + (2 * num2)

            # update line
            line = line[:i] + [(magnitude, depth1-1)] + line[i+2:]
            break
    return line[0][0]


def main(data, part):
    flattened_lines = get_flattened_lines(data)

    if part == 1:
        return calculate_magnitude(reduce(add, flattened_lines))
    elif part == 2:
        return max(
            calculate_magnitude(add(line1, line2))
            for line1, line2 in permutations(flattened_lines, 2)
        )


if __name__ == '__main__':

    # tests
    # print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 18: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
