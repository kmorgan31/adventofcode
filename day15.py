#!/usr/bin/python

from aocd import lines
from queue import PriorityQueue

import sys


# Vertex - chiton
# weight - risk level
# Cave - graph


test_data = [
    '1163751742',
    '1381373672',
    '2136511328',
    '3694931569',
    '7463417111',
    '1319128137',
    '1359912421',
    '3125421639',
    '1293138521',
    '2311944581'
]


class Cavern():
    # Graph
    def __init__(self, part):
        self.part = part

    def get_cave_risk_map(self, data):
        # converts data to nested array (stores weights of each vertex)
        self.cave_risks = [[int(c) for c in line] for line in data]
        self.board_size = len(self.cave_risks)

        if self.part == 2:
            # calculate risk level for extra sections
            def get_new_risk_level(self, x, y):
                risk_level_in_original_section = (
                    self.cave_risks[x % self.board_size][y % self.board_size]
                )
                risk_level_in_current_section = (
                    risk_level_in_original_section +
                    (x//self.board_size) + (y//self.board_size)
                )
                risk_level_in_current_section = risk_level_in_current_section % 9
                if not risk_level_in_current_section:
                    # risk level does not reset to 0
                    risk_level_in_current_section = 9
                return risk_level_in_current_section

            # initialize board for new size
            new_cave_risks = [
                [
                    '.' for x in range(self.board_size * 5)
                ] for y in range(self.board_size * 5)
            ]

            # update board size
            for x in range(self.board_size * 5):
                for y in range(self.board_size * 5):
                    new_cave_risks[x][y] = get_new_risk_level(self, x, y)

            self.cave_risks = new_cave_risks
            self.board_size = len(self.cave_risks)

    def get_surrounding_caves(self, cave):
        x, y = cave
        surrounding_caves = [
            (x-1, y),       # left
            (x, y-1),       # up
            (x, y+1),       # down
            (x+1, y),       # right
        ]
        return [
            (i, j) for i, j in surrounding_caves
            if 0 <= i <= self.board_size-1 and 0 <= j <= self.board_size-1
        ]

    def get_shortest_path(self, start, end):
        # initialize priority queue (cost, next_cave) with starting cave
        caves_to_visit = PriorityQueue()
        caves_to_visit.put([0, start])

        # initialize dict to store total_risk to any node from start
        self.total_risk_dict = {}

        # initiate path of visited caves
        visited = set()

        while caves_to_visit:
            # get first entry
            total_risk, (x, y) = caves_to_visit.get()
            if (x, y) in visited:
                continue

            if (x, y) == end:
                return total_risk + self.cave_risks[x][y]

            visited.add((x, y))

            # update cost to cave_to_visit (x, y)
            if (x, y) == start:
                self.total_risk_dict[(x, y)] = 0
            else:
                min_risk = self.get_min_risk_to_visit_surrounding_caves((x, y))
                self.total_risk_dict[(x, y)] = min_risk + self.cave_risks[x][y]

            # add cost to surrounding caves to caves_to_visit
            for i, j in self.get_surrounding_caves((x, y)):
                caves_to_visit.put([self.total_risk_dict[(x, y)], (i, j)])

    def get_min_risk_to_visit_surrounding_caves(self, cave):
        min_risk = sys.maxsize
        for i, j in self.get_surrounding_caves(cave):
            if self.total_risk_dict.get((i, j), sys.maxsize) < min_risk:
                min_risk = self.total_risk_dict[(i, j)]
        return min_risk


def main(data, part):
    cavern = Cavern(part)
    cavern.get_cave_risk_map(data)

    end = (cavern.board_size-1, cavern.board_size-1)
    total_risk = cavern.get_shortest_path((0, 0), end)
    return total_risk


if __name__ == '__main__':

    # test
    print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 15: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
