#!/usr/bin/python

import sys
import requests


def determine_question():
    return map(int, sys.argv[1].split('.'))


def fetch_data(day):
    cookie = '53616c7465645f5fa5d68c2c74333c3cf12f7d3fd1879c09c13156e540110a1ab1c384fc44a06720c841e41aa6ec5668'
    target_url = f"https://adventofcode.com/2021/day/{day}/input"
    session = requests.Session()
    return session.get(
        target_url, cookies={'session': cookie}
    ).text.strip().split('\n')


if __name__ == '__main__':
    day, part = determine_question()

    data = fetch_data(day)
    horizontal, depth, aim = 0, 0, 0

    if part == 1:
        for action in data:
            direction, x = action.split()
            amount = int(x)

            if direction == "forward":
                horizontal += amount
            elif direction == "down":
                depth += amount
            elif direction == "up":
                depth -= amount
    elif part == 2:
        for action in data:
            direction, x = action.split()
            amount = int(x)

            if direction == "forward":
                horizontal += amount
                depth += aim * amount
            elif direction == "down":
                aim += amount
            elif direction == "up":
                aim -= amount

    print(horizontal * depth)