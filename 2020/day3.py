#!/usr/bin/python

from aocd import lines

from math import prod

EXAMPLE = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]

SLOPES = [
    (3, 1),
    (1, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


def main(data, part=None):

    grid = [list(line) for line in data]
    height, width = len(grid), len(grid[0])

    def get_num_trees(r, d):
        trees = 0
        for x in range(height):
            i, j = x*d, (x*r)%width
            if i < height and grid[i][j] == "#":
                trees += 1
        return trees

    if part == 1:
        return get_num_trees(*SLOPES[0])
    elif part == 2:
        return prod(get_num_trees(*i) for i in SLOPES)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
