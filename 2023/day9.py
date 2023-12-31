#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45"
]


def find_seq_difference(nums):
    # find difference between each pair of numbers in sequence
    # return new sequence
    return [nums[x+1] - nums[x] for x in range(len(nums)-1)]


def main(data, part=None):
    total = 0
    for line in data:
        pyramid = [list(map(int, line.split()))]

        while not all(x == 0 for x in pyramid[-1]):
            pyramid.append(find_seq_difference(pyramid[-1]))

        for x in range(len(pyramid)-1, -1, -1):
            if part == 1:
                # extrapolate next value
                pyramid[x-1].append(pyramid[x][-1] + pyramid[x-1][-1])
            elif part == 2:
                # extrapolate previous value
                pyramid[x-1].insert(0, pyramid[x-1][0] - pyramid[x][0])

        if part == 1:
            total += pyramid[0][-1]
        elif part == 2:
            total += pyramid[0][0]

    return total


if __name__ == '__main__':
    # print(f'Day 9: Part 1 {main(lines, part=1)}')
    print(f'Day 9: Part 2 {main(lines, part=2)}')
