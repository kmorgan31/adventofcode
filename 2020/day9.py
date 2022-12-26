#!/usr/bin/python

from aocd import lines

from itertools import combinations

EXAMPLE = [
    "35",
    "20",
    "15",
    "25",
    "47",
    "40",
    "62",
    "55",
    "65",
    "95",
    "102",
    "117",
    "150",
    "182",
    "127",
    "219",
    "299",
    "277",
    "309",
    "576"
]


def part_1(nums, window):
    for i in range(len(nums)-window):
        preamble = nums[i:i+window]
        j = nums[i+window]

        found = False
        for x in combinations(preamble, 2):
            if sum(x) == j:
                found = True
                break
        if not found:
            return j


def part_2(data, window):
    nums = list(map(int, data))

    invalid_num = part_1(nums, window)
    for i in range(len(nums)-2):
        for j in range(i+2, len(nums)):
            if sum(nums[i:j]) == invalid_num:
                return min(nums[i:j]) + max(nums[i:j])


if __name__ == '__main__':
    # print(f'EXAMPLE {part_2(EXAMPLE, 5)}')
    print(f'Part 1 {part_1(lines, 25)}')
    print(f'Part 2 {part_2(lines, 25)}')
