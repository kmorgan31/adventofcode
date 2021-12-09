#!/usr/bin/python

import sys
import requests
import math


test_data = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678'
]

heat_map = {}


def determine_question():
    return map(int, sys.argv[1].split('.'))


def fetch_data(day):
    cookie = '53616c7465645f5fa5d68c2c74333c3cf12f7d3fd1879c09c13156e540110a1ab1c384fc44a06720c841e41aa6ec5668'
    target_url = f"https://adventofcode.com/2021/day/{day}/input"
    session = requests.Session()
    return session.get(
        target_url, cookies={'session': cookie}
    ).text.strip().split('\n')


def parse_heat_map(data):
    return [list(line) for line in data]


def get_surrounding_points(x, y):
    surrounding_points = []
    if x > 0:
        # left
        surrounding_points.append((x-1, y))
    if y > 0:
        # up
        surrounding_points.append((x, y-1))
    if x < len(heat_map)-1:
        # right
        surrounding_points.append((x+1, y))
    if y < len(heat_map[x])-1:
        # down
        surrounding_points.append((x, y+1))
    return surrounding_points


def is_low_point(x, y):
    curr_value = int(heat_map[x][y])
    surrounding_points = get_surrounding_points(x, y)
    surrounding_values = [int(heat_map[x][y]) for x, y in surrounding_points]
    return all([curr_value < x for x in surrounding_values])


def get_low_points():
    low_points = []
    for x in range(len(heat_map)):
        for y in range(len(heat_map[x])):
            if is_low_point(x, y):
                low_points.append((x, y))
    return low_points


def calculate_total_risk_level(low_points):
    total_risk_level = 0
    for x, y in low_points:
        risk_level = int(heat_map[x][y]) + 1
        total_risk_level += risk_level
    return total_risk_level


def find_basins(low_points):
    return [
        len(expand_basin(x, y, set()))
        for x, y in low_points
    ]


def expand_basin(x, y, basin_points):
    # add current point to basin
    basin_points.add((x, y))

    # get surrounding points
    curr_value = int(heat_map[x][y])
    surrounding_points = [
        (i, j) for i, j in get_surrounding_points(x, y)
        if curr_value < int(heat_map[i][j]) < 9
    ]

    if surrounding_points:
        # add surrounding points to basin
        basin_points.update(surrounding_points)
        for x, y in surrounding_points:
            # explore surrounding points
            expand_basin(x, y, basin_points)

    return basin_points


if __name__ == '__main__':
    day, part = determine_question()
    data = fetch_data(day)

    if 'test' in sys.argv:
        data = test_data

    heat_map = parse_heat_map(data)

    low_points = get_low_points()
    if part == 1:
        total_risk_level = calculate_total_risk_level(low_points)
        print(total_risk_level)
    elif part == 2:
        basins = sorted(find_basins(low_points), reverse=True)
        print(math.prod(basins[:3]))
