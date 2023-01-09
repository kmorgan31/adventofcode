#!/usr/bin/python

from aocd import lines

import re
from collections import deque


def print_grid(grid):
    for x in grid:
        print(''.join(x))


def create_grid(x, y):
    grid = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(".")
        grid.append(row)
    return grid


def main(data):
    grid = create_grid(6, 50)
    for line in data:
        action, rc = line.split()[:2]
        i, j = list(map(int, re.findall(r'\d+', line)))
        if action == "rect":
            for x in range(j):
                for y in range(i):
                    grid[x][y] = "#"
        elif action == "rotate":
            if rc == "row":
                # move row a by b spaces
                grid_q = deque(grid[i])
                grid_q.rotate(j)
                grid[i] = list(grid_q)

            elif rc == "column":
                # move col a by b spaces
                grid_q = deque([grid[x][i] for x in range(len(grid))])
                grid_q.rotate(j)
                for k, x in enumerate(list(grid_q)):
                    grid[k][i] = x

    print_grid(grid)

    count = 0
    for x in grid:
        for i, y in enumerate(x):
            if y == "#":
                count += 1
    return count


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
