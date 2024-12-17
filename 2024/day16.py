#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

import heapq


EXAMPLE = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # N, E, S, W

class Maze():

    def __init__(self, data):
        lines = data.split("\n")
        self.max_x = len(lines)
        self.max_y = len(lines[0])
        self.parse_lines(lines)

    def parse_lines(self, lines):
        self.walls = set()
        for x in range(self.max_x):
            for y in range(self.max_y):
                if lines[x][y] == "#":
                    self.walls.add((x, y))
                elif lines[x][y] == "S":
                    self.start = (x, y)
                elif lines[x][y] == "E":
                    self.end = (x, y)

    def explore_forward(self):
        best = None
        seen = set()
        distances = {}

        queue = []
        heapq.heappush(queue, (0, self.start, 1)) # score, pos, d

        while queue:
            score, pos, d = heapq.heappop(queue)
            if (pos, d) not in distances:
                distances[(pos, d)] = score
            if pos == self.end and best is None:
                best = score
            if (pos, d) in seen:
                continue

            # visit
            seen.add((pos, d))
            dx, dy = DIRS[d]
            nx, ny = pos[0]+dx, pos[1]+dy
            if 0 <= nx < self.max_x and 0 <= ny < self.max_y and (nx, ny) not in self.walls:
                # go straight
                heapq.heappush(queue, (score+1, (nx, ny), d))
            # go clockwise
            heapq.heappush(queue, (score+1000, pos, (d+1)%4))
            # go counterclockwise
            heapq.heappush(queue, (score+1000, pos, (d-1)%4))
        return best, distances

    def explore_backward(self):
        seen = set()
        distances = {}

        # initialize with all directions from end
        queue = []
        for d in range(len(DIRS)):
            heapq.heappush(queue, (0, self.end, d)) # score, pos, d

        while queue:
            score, pos, d = heapq.heappop(queue)
            if (pos, d) not in distances:
                distances[(pos, d)] = score
            if (pos, d) in seen:
                continue

            # visit
            seen.add((pos, d))
            # go backwards
            dx, dy = DIRS[(d+2)%4]
            nx, ny = pos[0]+dx, pos[1]+dy
            if 0 <= nx < self.max_x and 0 <= ny < self.max_y and (nx, ny) not in self.walls:
                # go straight
                heapq.heappush(queue, (score+1, (nx, ny), d))
            # go clockwise
            heapq.heappush(queue, (score+1000, pos, (d+1)%4))
            # go counterclockwise
            heapq.heappush(queue, (score+1000, pos, (d-1)%4))
        return distances

    def best_path_pos(self, best, dist1, dist2):
        path = set()
        for x in range(self.max_x):
            for y in range(self.max_y):
                pos = (x, y)
                for d in range(len(DIRS)):
                    if (pos, d) in dist1 and (pos, d) in dist2 and dist1[(pos, d)] + dist2[(pos, d)] == best:
                        path.add(pos)
        return path

    def print(self, path):
        for x in range(self.max_x):
            line = ""
            for y in range(self.max_y):
                if (x, y) in self.walls:
                    line += "#"
                elif (x, y) == self.start:
                    line += "S"
                elif (x, y) == self.end:
                    line += "E"
                elif (x, y) in path:
                    line += "O"
                else:
                    line += "."
            print(line)


def main(data, part):
    maze = Maze(data)
    best, dist1 = maze.explore_forward()
    if part == 1:
        return best
    elif part == 2:
        dist2 = maze.explore_backward()
        return len(maze.best_path_pos(best, dist1, dist2))


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, 1)}')
    # print(f'Part 1 {main(data, 1)}')
    # print(f'Part 2 {main(EXAMPLE, 2)}')
    print(f'Part 2 {main(data, 2)}')
