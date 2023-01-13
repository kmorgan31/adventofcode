#!/usr/bin/python

import math
from collections import Counter

INPUT = 29000000


def part_1():
    house_dict = {}
    for i in range(1, (INPUT//10)):
        for j in range(i, INPUT//10, i):
            if j in house_dict:
                house_dict[j] += i * 10
            else:
                house_dict[j] = 10

    for key, value in house_dict.items():
        if value >= INPUT:
            print(f"House is {key}")
            break


def part_2(house_number):
    # starting where we previously ended because I'm sure it's going to be higher
    presents_delivered = 0
    while presents_delivered < INPUT:
        presents_delivered = (
            11 * sum(
                house_number // elf
                for elf in range(1, 51)
                if house_number % elf == 0
            )
        )
        house_number += 1
    return house_number-1


if __name__ == "__main__":
    # print(f"Part 1: {part_1()}")        # 665280
    print(f"Part 2: {part_2(665280)}")
