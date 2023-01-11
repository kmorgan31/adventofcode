#!/usr/bin/python

from aocd import lines

from itertools import combinations, permutations

EXAMPLE = [
    "###########",
    "#0.1.....2#",
    "#.#######.#",
    "#4.......3#",
    "###########"
]


def get_surrounding_points(pos):
    x, y = pos
    return {
        (x-1, y),    # up
        (x+1, y),   # down
        (x, y-1),   # left
        (x, y+1)   # right
    }


def get_shortest_path(walls, start, end):
    visited = set([(start[0], start[1])])

    to_visit = [(start[0], start[1], 0)]      # posx, posy, steps
    while to_visit:

        x, y, steps = to_visit.pop(0)
        if (x, y) == end:
            return steps

        for sp in get_surrounding_points((x, y)):
            if sp not in walls and sp not in visited:
                to_visit.append((sp[0], sp[1], steps+1))
                visited.add(sp)


def main(data, part=None):
    walls = set()
    points = {}
    for x, line in enumerate(data):
        for y, z in enumerate(line):
            if z == "#":
                walls.add((x, y))
            elif z.isdigit():
                points[int(z)] = (x, y)

    shortest_paths = {}
    for p1, p2 in combinations(points.keys(), 2):
        path = get_shortest_path(walls, points[p1], points[p2])
        shortest_paths[(p1, p2)] = path
        shortest_paths[(p2, p1)] = path

    min_path = 999999999
    dests = [x for x in points if x != 0]
    for path in permutations(dests, len(dests)):
        path = [0] + list(path)
        if part == 2:
            path += [0]

        steps = sum(
            shortest_paths[(path[i], path[i+1])] for i in range(len(path)-1)
        )
        min_path = min(min_path, steps)
    return min_path


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
