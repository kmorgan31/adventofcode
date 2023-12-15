#!/usr/bin/python

from aocd import lines

from collections import defaultdict

EXAMPLE = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]


def determine_points(winning_nums, nums):
    num_matches = determine_num_matches(winning_nums, nums)
    return 2**(num_matches-1) if num_matches > 0 else 0


def determine_num_matches(winning_nums, nums):
    return sum(1 for num in nums if num in winning_nums)


def part_1(data):
    total = 0
    for line in data:
        winning_nums, nums = line.split(':')[1].lstrip().split("|")
        total += determine_points(winning_nums.split(), nums.split())
    return total


def part_2(data):
    card_dct = defaultdict(int)
    for card_num, line in enumerate(data, 1):
        # process original card
        card_dct[card_num] += 1

        winning_nums, nums = line.split(':')[1].lstrip().split("|")
        num_matches = determine_num_matches(winning_nums.split(), nums.split())

        # update dct with new cards
        for x in range(card_num+1, card_num+num_matches+1):
            card_dct[x] += card_dct[card_num]

    return sum(card_dct.values())


if __name__ == '__main__':
    print(f'Day 4: Part 1 {part_1(lines)}')
    print(f'Day 2: Part 2 {part_2(lines)}')
