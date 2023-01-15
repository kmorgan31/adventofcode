#!/usr/bin/python

from aocd import lines

from math import prod
from itertools import combinations

EXAMPLE = ["1", "2", "3", "4", "5", "7", "8", "9", "10", "11"]


def update_min(min_first, min_e, first, qe):
    return (
        len(first) < min_first or (len(first) == min_first and qe < min_e)
    )


def split_remaining_weights(weights, start_size, num_splits, first, min_first, min_e, qe):
    for j in range(start_size, len(weights)//num_splits):
        for group1 in combinations(weights, j):
            if sum(group1) != sum(first):
                # don't bother trying to split
                continue

            group2 = set(weights) - set(group1)
            if sum(first) * (num_splits-1) != sum(group2):
                # don't bother trying to split
                continue

            if num_splits-1 > 1:
                split = split_remaining_weights(
                    group2, start_size-1, num_splits-1, first, min_first, min_e, qe
                )
                if split:
                    return split

            if sum(first) == sum(group2):
                if update_min(min_first, min_e, first, qe):
                    return len(first), qe


def main(data, num_splits, start_size):
    weights = set(map(int, data))

    min_first = len(data)
    min_e = 999999999999999999

    for i in range(3, len(weights)//num_splits):
        for first in combinations(weights, i):
            qe = prod(first)
            if not update_min(min_first, min_e, first, qe):
                # if this first won't be less, don't bother
                continue

            # find the rem_weights to split between second and third
            rem_weights = set(weights) - set(first)
            if sum(first) * (num_splits-1) != sum(rem_weights):
                # don't bother trying to split
                continue

            split = split_remaining_weights(
                rem_weights, start_size-1, num_splits-1, first, min_first, min_e, qe
            )
            if split:
                min_first, min_e = split
                print(f'Min first: {min_first}, min qe: {min_e}')
                continue

    return min_e


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 3)}')
    print(f'Part 2 {main(lines, 4)}')
