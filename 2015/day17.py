#!/usr/bin/python

from aocd import lines


from collections import defaultdict


EXAMPLE = [
    "20",
    "15",
    "10",
    "5",
    "5"
]


def main(data, eggnog, part=None):
    data = list(map(int, data))
    possible_states = 2 ** len(data)

    ways = defaultdict(int)   # num_containers: ways_count
    for i in range(1, possible_states):
        binary = bin(i)[2:].zfill(len(data))
        total = sum(data[i] for i, x in enumerate(binary) if x == "1")
        if total == eggnog:
            ways[binary.count("1")] += 1

    if part == 1:
        return sum(ways.values())
    elif part == 2:
        min_num = min(ways)
        return ways[min_num]


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 25)}')
    print(f'Part 1 {main(lines, 150, 1)}')
    print(f'Part 2 {main(lines, 150, 2)}')
