#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5fee0705e64db4734fc3cdd400cda00b21007ee5c5773b21a9ce5d5c4fcadbc9f9e757bf653e0a030022ef46ceaf2aa00e9920c5481c83d491
from aocd import data

import math
from collections import Counter


EXAMPLE = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def lines(input_data):
    return input_data.split('\n')

def part1(input_data):
    zero_count = 0
    pos = 50

    for line in lines(input_data):
        direction, steps = line[0], int(line[1:])
        if direction == "L":
            pos -= steps
        else:
            pos += steps

        pos %= 100 
        if pos == 0:
            zero_count += 1
    return zero_count

def part2(input_data):
    zero_count = 0
    curr_pos = 50

    # print(f"Step 0. Pos {curr_pos}")
    for line in lines(input_data):
        direction, steps = line[0], int(line[1:])

        num_rotations = steps // 100
        remaining_steps = steps % 100
        if direction == "L":
            new_pos = curr_pos - remaining_steps
        else:
            new_pos = curr_pos + remaining_steps

        zero_count += num_rotations
        if curr_pos != 0 and (new_pos <= 0 or new_pos >= 100):
            zero_count += 1
 
        curr_pos = new_pos % 100
    return zero_count
     

if __name__ == '__main__':
    print(f'Day 1: Part 1 {part1(EXAMPLE)}')
    print(f'Day 1: Part 2 {part2(EXAMPLE)}')
    print(f'Day 1: Part 1 {part1(data)}')
    print(f'Day 1: Part 2 {part2(data)}')
