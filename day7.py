#!/usr/bin/python

import sys
import requests
import math


def determine_question():
    return map(int, sys.argv[1].split('.'))


def fetch_data(day):
    cookie = '53616c7465645f5fa5d68c2c74333c3cf12f7d3fd1879c09c13156e540110a1ab1c384fc44a06720c841e41aa6ec5668'
    target_url = f"https://adventofcode.com/2021/day/{day}/input"
    session = requests.Session()
    return session.get(
        target_url, cookies={'session': cookie}
    ).text.strip().split('\n')


def get_fuel(num, part):
    if part == 1:
        # each step is 1 unit of fuel
        return num
    elif part == 2:
        # sum of increasing units of fuel
        return num * (num + 1) // 2


if __name__ == '__main__':
    day, part = determine_question()

    data = fetch_data(day)
    crab_positions = [x for x in map(int, data[0].split(','))]

    lowest = math.inf
    leftmost_crab, rightmost_crab = min(crab_positions), max(crab_positions)

    for median_pos in range(leftmost_crab, rightmost_crab+1):
        fuel = sum([
            get_fuel(abs(crab_pos - median_pos), part)
            for crab_pos in crab_positions
        ])
        if fuel < lowest:
            lowest = fuel
    print(lowest)
