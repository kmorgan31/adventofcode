#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5fee0705e64db4734fc3cdd400cda00b21007ee5c5773b21a9ce5d5c4fcadbc9f9e757bf653e0a030022ef46ceaf2aa00e9920c5481c83d491
from aocd import data

import math
from itertools import permutations


EXAMPLE = """987654321111111
811111111111119
234234234234278
818181911112111"""


def lines(input_data):
    return input_data.split('\n')

def split_parts(num, num_partitions):
    partitions = []

    chunk_size = len(num) // num_partitions
    for x in range(0, num_partitions):
        s, e = x * chunk_size, (x+1) * chunk_size
        partitions += [num[s:e]]
    return partitions

def part1(input_data):
    total_voltage = 0
    for battery_pack in lines(input_data):
        max_voltage = 0
        lst_bp = list(battery_pack)
        print(lst_bp)
        for x in range(len(lst_bp)-1):
            for y in range(x+1, len(lst_bp)):
                voltage = int(f"{lst_bp[x]}{lst_bp[y]}")
                if voltage > max_voltage:
                    max_voltage = voltage
        print(max_voltage)
        total_voltage += max_voltage
    return total_voltage


def validate_joltage(j):
    # validate whether j maintains the order of the battery pack
    return [i[0] for i in j] == sorted([i[0] for i in j])


def part1_2(input_data):
    total_voltage = 0
    for battery_pack in lines(input_data):

        max_voltage = 0
        lst_pos_bp = [(idx, b) for idx, b in enumerate(list(battery_pack))]
        for j in permutations(lst_pos_bp, 2):
            is_valid = validate_joltage(j)
            if not is_valid:
                continue

            voltage = int("".join([i[1] for i in j]))
            if voltage > max_voltage:
                max_voltage = voltage
        print(max_voltage)
        total_voltage += max_voltage
    return total_voltage

def part2(input_data):
    total_voltage = 0
    for battery_pack in lines(input_data):
        on_batteries = list(battery_pack[-12:])
        for b in range(len(battery_pack)-13, -1, -1):
            bat = battery_pack[b]
            for o in range(len(on_batteries)):
                if bat >= on_batteries[o]:
                    on_batteries[o], bat = bat, on_batteries[o]
                else: break
        joltage = int(''.join(map(str, on_batteries)))
        total_voltage += joltage
    return total_voltage



if __name__ == '__main__':
    # print(f'Day 3: Part 1 {part1_2(EXAMPLE)}')
    # print(f'Day 3: Part 2 {part2(EXAMPLE)}')
    # print(f'Day 3: Part 1 {part1_2(data)}')
    print(f'Day 3: Part 2 {part2(data)}')
