#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5fee0705e64db4734fc3cdd400cda00b21007ee5c5773b21a9ce5d5c4fcadbc9f9e757bf653e0a030022ef46ceaf2aa00e9920c5481c83d491
from aocd import data

import math
from collections import Counter


EXAMPLE = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def ranges(input_data):
    return input_data.split(',')

def split_parts(num, num_partitions):
    partitions = []

    chunk_size = len(num) // num_partitions
    for x in range(0, num_partitions):
        s, e = x * chunk_size, (x+1) * chunk_size
        partitions += [num[s:e]]
    return partitions

def main(input_data, part=None):
    invalid_ids = set()

    for ids in ranges(input_data):
        start, end = map(int, ids.split('-'))
        for x in range(start, end+1):
            max_partitions = 2 if part == 1 else len(str(x))

            for np in range(2, max_partitions+1):
                if len(str(x)) % np != 0:
                    continue
                partitions = split_parts(str(x), np)
                if len(set(partitions)) > 1:
                    continue
                invalid_ids.add(x)
    return sum(invalid_ids)


if __name__ == '__main__':
    print(f'Day 2: Part 1 {main(EXAMPLE, 1)}')
    print(f'Day 2: Part 2 {main(EXAMPLE, 2)}')
    print(f'Day 2: Part 1 {main(data, 1)}')
    print(f'Day 2: Part 2 {main(data, 2)}')
