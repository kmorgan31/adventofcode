#!/usr/bin/python

from aocd import lines

import math

DIRECTIONS = "RL"

EXAMPLE = [
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)"
]

EXAMPLE_2 = [
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]


class Grid:

    def __init__(self, directions):
        self.nodes = {}
        self.directions = directions

    def parse_nodes(self, data):
        for line in data:
            split = line.split()
            self.nodes[split[0]] = (split[2][1:-1], split[3][:-1])

    def find_next_node(self, idx, node):
        if idx >= len(self.directions):
            idx = 0

        return idx, self.nodes[node][self.directions[idx] == "R"]

    def follow_directions(self, start, end):
        dir_idx = 0
        count = 0

        while start != end:
            dir_idx, start = self.find_next_node(dir_idx, start)

            count += 1
            dir_idx += 1

        return count

    def follow_multiple_paths(self):
        total = []

        for node in (n for n in self.nodes if n.endswith("A")):
            dir_idx = 0
            count = 0

            while not node.endswith("Z"):
                dir_idx, node = self.find_next_node(dir_idx, node)

                count += 1
                dir_idx += 1

            total.append(count)

        return(math.lcm(*total))


def example(data, part=None):
    grid = Grid(DIRECTIONS)

    grid.parse_nodes(data)
    return grid.follow_directions("AAA", 0, 0)


def main(part=None):
    grid = Grid(lines[0])
    grid.parse_nodes(lines[2:])

    if part == 1:
        return grid.follow_directions("AAA", "ZZZ")
    elif part == 2:
        return grid.follow_multiple_paths()


if __name__ == '__main__':
    # print(f'Day 8: Part 1 {main(part=1)}')
    print(f'Day 8: Part 2 {main(part=2)}')
