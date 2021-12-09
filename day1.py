#!/usr/bin/python

import sys
import requests

WINDOW_SIZE = {
    1: 1,
    2: 3
}


def determine_question():
    return map(int, sys.argv[1].split('.'))


def fetch_data(day):
    cookie = '53616c7465645f5fa5d68c2c74333c3cf12f7d3fd1879c09c13156e540110a1ab1c384fc44a06720c841e41aa6ec5668'
    target_url = f"https://adventofcode.com/2021/day/{day}/input"
    session = requests.Session()
    return session.get(
        target_url, cookies={'session': cookie}
    ).text.strip().split('\n')


def set_range(x, part):
    return x, x+WINDOW_SIZE.get(part, 1)


if __name__ == '__main__':
    day, part = determine_question()

    data = fetch_data(day)
    start, end = set_range(0, part)

    increased = 0
    prev_sum = 0
    while end < len(data):
        next_sum = sum(map(int, data[start:end]))
        if next_sum > prev_sum:
            increased += 1
        prev_sum = next_sum
        start, end = set_range(start+1, part)

    print(increased)