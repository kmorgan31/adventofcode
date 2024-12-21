#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

import heapq


EXAMPLE = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


class Grid:

    def __init__(self, data):
        lines = data.splitlines()
        self.max_x = len(lines)
        self.max_y = len(lines[0])
        self.parse_lines(lines)

    def parse_lines(self, lines):
        self.walls = []
        for x in range(self.max_x):
            for y in range(self.max_y):
                if lines[x][y] == "S":
                    self.start = (x, y)
                elif lines[x][y] == "E":
                    self.end = (x, y)
                elif lines[x][y] == "#":
                    self.walls.append((x, y))

    def get_surrounding_points(self, x, y):
        return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    def get_path(self):
        seen = set()

        queue = []
        heapq.heappush(queue, (0, [self.start])) # score, path

        while queue:
            score, path = heapq.heappop(queue)

            pos = path[-1]
            if pos == self.end:
                return score, path
            if pos in seen:
                continue

            # visit
            seen.add(pos)
            for nx, ny in self.get_surrounding_points(pos[0], pos[1]):
                if 0 <= nx < self.max_x and 0 <= ny < self.max_x and (nx, ny) not in self.walls:
                    heapq.heappush(queue, (score+1, path + [(nx, ny)]))

    def print_grid(self, path):
        for x in range(self.max_x):
            line = ""
            for y in range(self.max_y):
                if (x, y) == self.start:
                    line += "S"
                elif (x, y) == self.end:
                    line += "E"
                # elif (x, y) in path:
                #     line += "O"
                elif (x, y) in self.walls:
                    line += "#"
                else:
                    line += "."
            print(line)
        print()


def main(data, cheat, min_saving):
    grid = Grid(data)
    max_steps, path = grid.get_path()

    total = 0
    for idx, (x, y) in enumerate(path):
        if len(path) - 1 - idx < min_saving:
            break

        for (i, j) in path[idx+min_saving:]:
            dst = abs(x-i) + abs(y-j)
            if dst > cheat:
                continue
            steps = idx + dst + (max_steps - path.index((i, j)))
            if max_steps - steps >= min_saving:
                total += 1
    return total


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, 1, 64)}')
    print(f'Part 1 {main(data, 2, 100)}')
    print(f'Part 2 {main(data, 20, 100)}')
