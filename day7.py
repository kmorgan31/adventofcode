#!/usr/bin/python

from aocd import lines
import math


def get_fuel(num, part):
    if part == 1:
        # each step is 1 unit of fuel
        return num
    elif part == 2:
        # sum of increasing units of fuel
        return num * (num + 1) // 2


def main(crab_positions, part):
    lowest = math.inf
    leftmost_crab, rightmost_crab = min(crab_positions), max(crab_positions)

    for median_pos in range(leftmost_crab, rightmost_crab+1):
        fuel = sum([
            get_fuel(abs(crab_pos - median_pos), part)
            for crab_pos in crab_positions
        ])
        if fuel < lowest:
            lowest = fuel

    return lowest


if __name__ == '__main__':
    crab_positions = [x for x in map(int, lines[0].split(','))]
    print(f'Day 7: Part 1 {main(crab_positions, 1)}, Part 2 {main(crab_positions, 2)}')
