#!/usr/bin/python

from aocd import lines


def get_surrounding_points(x, y):
    return {
        (x-1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x+1, y-1),
        (x+1, y),
        (x+1, y+1),
        (x, y+1),
        (x, y-1)
    }


def main(data, part=None):
    grid = {}
    for i, line in enumerate(data):
        for j, val in enumerate(line):
            if part == 2 and (i,j) in [(0,0), (0,99), (99,0), (99,99)]:
                val = "#"
            grid[(i, j)] = val

    for x in range(100):
        new_grid = {}
        for pos, val in grid.items():
            if part == 2 and pos in [(0,0), (0,99), (99,0), (99,99)]:
                new_grid[pos] = "#"
                continue

            num_surrounding_points = len(
                [sp for sp in get_surrounding_points(*pos) if grid.get(sp) == "#"]
            )
            if grid[pos] == "#" and num_surrounding_points not in [2, 3]:
                new_grid[pos] = "."
            elif grid[pos] == "." and num_surrounding_points == 3:
                new_grid[pos] = "#"
            else:
                new_grid[pos] = grid[pos]
        grid = new_grid

    return list(grid.values()).count("#")


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
