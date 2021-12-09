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


def parse_coords(data):
    coords = []
    for line in data:
        x, y = line.split(' -> ')
        x1, y1 = map(int, x.split(','))
        x2, y2 = map(int, y.split(','))
        coords.append([(x1, y1), (x2, y2)])
    return coords


def determine_points(a, b):
    x1, y1 = a
    x2, y2 = b
    d = (x2 - x1, y2 - y1)

    if d[0] == 0:
        steps = abs(d[1])
    else:
        steps = abs(d[0])

    d = (d[0] // steps, d[1] // steps)

    points = []
    while a != b:
        points.append(a)
        a = (a[0] + d[0], a[1] + d[1])
    points.append(b)

    return points


if __name__ == '__main__':
    day, part = determine_question()

    data = fetch_data(day)
    coords = parse_coords(data)

    floor_map = {}
    for a,b in coords:
        if part == 1:
            if a[0] != b[0] and a[1] != b[1]:
                continue

        points = determine_points(a,b)
        if not points:
            continue

        for point in points:
            if floor_map.get(point):
                floor_map[point] += 1
            else:
                floor_map[point] = 1

    overlap = {
        k for k,v in floor_map.items() if v >= 2
    }
    print(overlap)
    print(len(overlap))
