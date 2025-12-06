#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5fee0705e64db4734fc3cdd400cda00b21007ee5c5773b21a9ce5d5c4fcadbc9f9e757bf653e0a030022ef46ceaf2aa00e9920c5481c83d491
from aocd import data

import math
from itertools import permutations


EXAMPLE = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def parse_data(input_data):
    ranges = []
    ingredients = []

    lines = input_data.split('\n')
    for line in lines:
        if line == '':
            continue
        if line.find("-") > 0:
            s, e = line.split("-")
            ranges.append([int(s), int(e)])
        else:
            ingredients.append(int(line))
    return ranges, ingredients


def part1(input_data):
    ingredient_count = 0
    ranges, ingredients = parse_data(input_data)
    for x in ingredients:
        if any([x >= y and x <= z for y,z in ranges]):
            ingredient_count += 1
    return ingredient_count

def find_ranges(valid_ranges):
    i = 0
    while i < len(valid_ranges):
        id_range = valid_ranges[i]
        j = i + 1
        if j < len(valid_ranges) and valid_ranges[i][1] >= valid_ranges[j][0]:
            valid_ranges[i][1] = max(valid_ranges[i][1], valid_ranges[j][1])
            valid_ranges.pop(j)
            i -= 1

        i += 1
    return valid_ranges


def part2(input_data):
    ingredient_count = 0
    ranges, ingredients = parse_data(input_data)
    ranges = sorted(ranges, key=lambda x:(x[0], x[1]))
    for y,z in find_ranges(ranges):
        ingredient_count += z-y+1
    return ingredient_count



if __name__ == '__main__':
    # print(f'Day 5: Part 1 {part1(EXAMPLE)}')
    print(f'Day 5: Part 2 {part2(EXAMPLE)}')
    # print(f'Day 5: Part 1 {part1(data)}')
    print(f'Day 5: Part 2 {part2(data)}')
