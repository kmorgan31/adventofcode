#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data
import math


EXAMPLE = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def parse_topology_map(data):
    return [list(line) for line in data.split("\n")]
 
def get_surrounding_points(x, y, topology_map):
    surrounding_points = []
    if x > 0:
        # left
        surrounding_points.append((x-1, y))
    if y > 0:
        # up
        surrounding_points.append((x, y-1))
    if x < len(topology_map)-1:
        # right
        surrounding_points.append((x+1, y))
    if y < len(topology_map[x])-1:
        # down
        surrounding_points.append((x, y+1))
    return surrounding_points


def get_starting_points(topology_map):
    starting_points = []
    for x in range(len(topology_map)):
        for y in range(len(topology_map[x])):
            if topology_map[x][y] == "0":
                starting_points.append((x, y))
    return starting_points

def explore_trailhead(x, y, trailhead_points, topology_map):
    # add current point to trailhead
    trailhead_points.append((x, y))

    curr_value = int(topology_map[x][y])
    if curr_value == 9:
        # reached end of trailhead
        return trailhead_points

    # get surrounding points
    surrounding_points = [
        (i, j) for i, j in get_surrounding_points(x, y, topology_map)
        if curr_value + 1 == int(topology_map[i][j])
    ]

    if surrounding_points:
        # add surrounding points to trailhead
        trailhead_points.extend(surrounding_points)
        for x, y in surrounding_points:
            # explore surrounding points
            explore_trailhead(x, y, trailhead_points, topology_map)

    return trailhead_points


def main(data, part):
    topology_map = parse_topology_map(data)

    total = 0
    for x, y in get_starting_points(topology_map):
        trailhead_points = explore_trailhead(x, y, [], topology_map)
        if part == 1:
            # calculate trailhead score: unique 9s
            total += [topology_map[x][y] for x, y in set(trailhead_points)].count("9")
        elif part == 2:
            # calculate trailhead rating: repeated 9s
            total += [topology_map[x][y] for x, y in trailhead_points].count("9")/2
    return total


if __name__ == '__main__':
    print(f'Part 1 {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(data, 1)}')
    print(f'Part 2 {main(EXAMPLE, 2)}')
    print(f'Part 2 {main(data, 2)}')
