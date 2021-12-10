#!/usr/bin/python

from aocd import lines
import math


test_data = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678'
]


def parse_heat_map(data):
    return [list(line) for line in data]


def get_surrounding_points(x, y, heat_map):
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


def is_low_point(x, y, heat_map):
    curr_value = int(heat_map[x][y])
    surrounding_points = get_surrounding_points(x, y, heat_map)
    surrounding_values = [int(heat_map[x][y]) for x, y in surrounding_points]
    return all([curr_value < x for x in surrounding_values])


def get_low_points(heat_map):
    low_points = []
    for x in range(len(heat_map)):
        for y in range(len(heat_map[x])):
            if is_low_point(x, y, heat_map):
                low_points.append((x, y))
    return low_points


def calculate_total_risk_level(low_points, heat_map):
    total_risk_level = 0
    for x, y in low_points:
        risk_level = int(heat_map[x][y]) + 1
        total_risk_level += risk_level
    return total_risk_level


def find_basins(low_points, heat_map):
    return [
        len(expand_basin(x, y, set(), heat_map))
        for x, y in low_points
    ]


def expand_basin(x, y, basin_points, heat_map):
    # add current point to basin
    basin_points.add((x, y))

    # get surrounding points
    curr_value = int(heat_map[x][y])
    surrounding_points = [
        (i, j) for i, j in get_surrounding_points(x, y, heat_map)
        if curr_value < int(heat_map[i][j]) < 9
    ]

    if surrounding_points:
        # add surrounding points to basin
        basin_points.update(surrounding_points)
        for x, y in surrounding_points:
            # explore surrounding points
            expand_basin(x, y, basin_points, heat_map)

    return basin_points


def main(data, part):
    heat_map = parse_heat_map(data)
    low_points = get_low_points(heat_map)

    if part == 1:
        return calculate_total_risk_level(low_points, heat_map)
    elif part == 2:
        basins = sorted(find_basins(low_points, heat_map), reverse=True)
        return math.prod(basins[:3])


if __name__ == '__main__':

    # test
    print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 9: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
