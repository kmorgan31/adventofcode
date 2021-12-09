#!/usr/bin/python

import sys
import requests
from collections import defaultdict


def determine_question():
    return map(int, sys.argv[1].split('.'))


def fetch_data(day):
    cookie = '53616c7465645f5fa5d68c2c74333c3cf12f7d3fd1879c09c13156e540110a1ab1c384fc44a06720c841e41aa6ec5668'
    target_url = f"https://adventofcode.com/2021/day/{day}/input"
    session = requests.Session()
    return session.get(
        target_url, cookies={'session': cookie}
    ).text.strip().split('\n')


def decrease_lanternfish_days(lanternfish_count):
    babies = lanternfish_count[0]

    for x in range(9):
        lanternfish_count[x] = lanternfish_count[x+1]

    # add new_babies
    lanternfish_count[8] = babies

    # reset moms
    lanternfish_count[6] += babies

    return lanternfish_count


if __name__ == '__main__':
    day, part = determine_question()

    data = fetch_data(day)
    lanternfish = [x for x in map(int, data[0].split(','))]

    lanternfish_count = defaultdict(int)
    for x in lanternfish:
        lanternfish_count[x] += 1

    for x in range(256):
        if x == 80:
            print(sum(lanternfish_count.values()))
        lanternfish_count = decrease_lanternfish_days(lanternfish_count)
    print(sum(lanternfish_count.values()))
