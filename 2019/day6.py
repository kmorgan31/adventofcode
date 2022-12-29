#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
]

EXAMPLE_2 = EXAMPLE + [
    "K)YOU",
    "I)SAN"
]


def dfs(grid, node):
    if not grid.get(node):
        return 0
    else:
        return sum(dfs(grid, k) for k in grid[node])


def main(data, part=None):
    grid = {}
    for line in data:
        parent, child = line.split(")")
        grid[child] = parent

    paths_to_com = {}
    for k in grid:
        path = []
        parent = grid.get(k)
        while parent:
            path.append(parent)
            parent = grid.get(parent)
        paths_to_com[k] = path

    if part == 1:
        return sum(len(path) for path in paths_to_com.values())
    elif part == 2:
        return len(set(paths_to_com["YOU"]) ^ set(paths_to_com["SAN"]))


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE_2, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
