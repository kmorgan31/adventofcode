#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

import os
import time
import copy

from aocd import data


EXAMPLE = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

COMPASS = ["E", "S", "W", "N"]


class Guard:

    def __init__(self, pos, facing):
        self.pos = pos
        self.facing = facing  # N, E, S, W
        self.path = set()
        self.visited = set()

    def get_next_pos(self, grid, x, y, f):
        if f == "N":
            x = (x-1)
        elif f == "S":
            x = (x+1)
        elif f == "E":
            y = (y+1)
        elif f == "W":
            y = (y-1)
        return x, y, f

    def move_forward(self, grid):
        nx, ny, nf = self.get_next_pos(grid, self.pos[0], self.pos[1], self.facing)
        if (nx, ny) in grid.obs or (nx, ny) == grid.new_obs:
            # turn to the right
            self.facing = COMPASS[(COMPASS.index(self.facing)+1) % len(COMPASS)]
        else:
            # move
            self.path.add((self.pos[0], self.pos[1], self.facing))
            self.visited.add((self.pos[0], self.pos[1]))
            self.pos = (nx, ny)

    def in_loop(self):
        return (self.pos[0], self.pos[1], self.facing) in self.path


class Grid:

    def __init__(self, data):
        lines = data.split("\n")
        self.max_x = len(lines)
        self.max_y = len(lines[0])
        self.new_obs = (-1, -1)
        self.parse(lines)

    def parse(self, data):
        self.obs = set()
        for x in range(self.max_x):
            for y in range(self.max_y):
                if data[x][y] == "#":
                    self.obs.add((x, y))
                elif data[x][y] == "^":
                    self.guard = (x, y)

    def add_obs(self, pos):
        self.new_obs = pos

    def print(self, guard):
        for x in range(self.max_x):
            line = ""
            for y in range(self.max_y):
                if (x, y) in self.obs:
                    line += "#"
                elif (x, y) == self.new_obs: 
                    line += "O"
                elif (x, y) == guard.pos:
                    line += "G"
                elif (x, y) in guard.visited:
                    line += "X"
                else:
                    line += "."
            print(f"{line}\n")


def part_1(data):

    grid = Grid(data)
    guard = Guard(grid.guard, "N")

    while 0 <= guard.pos[0] < grid.max_x and 0 <= guard.pos[1] < grid.max_y and not guard.in_loop():
        guard.move_forward(grid)

    return len(guard.visited)

def part_2(data):
    grid = Grid(data)

    loop = 0
    for x in range(grid.max_x):
        for y in range(grid.max_y):
            if (x, y) not in grid.obs:
                grid.add_obs((x, y))
                guard = Guard(grid.guard, "N")

                while 0 <= guard.pos[0] < grid.max_x and 0 <= guard.pos[1] < grid.max_y and not guard.in_loop():
                    guard.move_forward(grid)

                if guard.in_loop():
                    loop += 1
    return loop


if __name__ == '__main__':
    print(f'Part 1 {part_1(EXAMPLE)}')
    print(f'Part 1 {part_1(data)}')
    print(f'Part 2 {part_2(EXAMPLE)}')
    print(f'Part 2 {part_2(data)}')
