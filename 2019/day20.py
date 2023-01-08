#!/usr/bin/python

from aocd import lines

# from day20_example import (
#     EXAMPLE,
#     EXAMPLE_INCREASE_DEPTH,
#     EXAMPLE_DECREASE_DEPTH
# )
# from day20_example2 import (
#     EXAMPLE_2,
#     EXAMPLE_2_INCREASE_DEPTH,
#     EXAMPLE_2_DECREASE_DEPTH
# )


class Portal:
    def __init__(self, name, inner, outer):
        self.name = name
        self.inner = inner
        self.outer = outer


portals = [
    Portal("YY", (28, 73), (2, 65)),
    Portal("YI", (28, 41), (2, 31)),
    Portal("ER", (28, 35), (81, 2)),
    Portal("VB", (28, 45), (71, 2)),
    Portal("WT", (28, 61), (65, 2)),
    Portal("UH", (28, 53), (114, 67)),
    Portal("LD", (28, 63), (53, 112)),
    Portal("JR", (28, 79), (114, 37)),
    Portal("LH", (71, 28), (2, 59)),
    Portal("KB", (45, 28), (35, 112)),
    Portal("FR", (37, 28), (114, 49)),
    Portal("BI", (53, 28), (114, 81)),
    Portal("SG", (65, 28), (114, 57)),
    Portal("DU", (77, 28), (85, 112)),
    Portal("HM", (88, 55), (2, 77)),
    Portal("RX", (88, 59), (39, 2)),
    Portal("YT", (88, 47), (57, 2)),
    Portal("BB", (88, 77), (57, 112)),
    Portal("KU", (88, 67), (75, 112)),
    Portal("TS", (88, 37), (114, 63)),
    Portal("PO", (39, 86), (2, 39)),
    Portal("JJ", (35, 86), (2, 51)),
    Portal("NS", (73, 86), (2, 67)),
    Portal("QG", (81, 86), (2, 73)),
    Portal("PU", (65, 86), (43, 2)),
    Portal("YB", (47, 86), (39, 112)),
    Portal("JN", (59, 86), (65, 112)),
]


# inner to outer
INCREASE_DEPTH = {p.inner: p.outer for p in portals}

# outer to inner
DECREASE_DEPTH = {p.outer: p.inner for p in portals}


class Maze:

    def __init__(self, data, start, end):
        self.start = start
        self.end = end

        self.parse_data(data)
        self.get_boundaries()

    def parse_data(self, data):
        self.maze = {}
        for x, line in enumerate(data):
            for y, l in enumerate(line):
                pos = (x, y)

                if l in ["#", "."]:
                    self.maze[pos] = l

    def get_boundaries(self):
        xvals = [x for x, _ in self.maze]
        yvals = [y for _, y in self.maze]

        self.min_x, self.max_x = min(xvals), max(xvals)
        self.min_y, self.max_y = min(yvals), max(yvals)

    def print_maze(self, pos=None, to_visit=None):
        if to_visit:
            to_visit_dct = {x[0]: x for x in to_visit}

        for x in range(self.min_x-1, self.max_x+2):
            line = ""
            for y in range(self.min_y-1, self.max_y+2):
                if (x, y) == pos:
                    line += "X"
                elif (x, y) == self.start:
                    line += "S"
                elif (x, y) == self.end:
                    line += "E"
                elif to_visit and (x, y) in to_visit_dct:
                    val = to_visit_dct[(x, y)]
                    line += "N" if len(val) != 2 else str(val[1])
                elif (x, y) in self.maze:
                    line += self.maze[(x, y)]
                else:
                    line += " "
            print(line)

    def get_surrounding_points(self, pos):
        x, y = pos
        return [
            (x, y-1),
            (x, y+1),
            (x-1, y),
            (x+1, y)
        ]

    def shortest_path(self, start, end):
        visited = set()

        to_visit = [(start, 0)]         # steps, curr_pos
        while to_visit:
            pos, steps = to_visit.pop(0)
            x, y = pos
            visited.add(pos)

            if pos == end:
                return steps

            for sp in self.get_surrounding_points(pos):
                if self.maze.get(sp, "#") == "." and sp not in visited:
                    to_visit.append((sp, steps+1))

    def shortest_path_2(self, start, end):
        visited = set()

        steps = 0
        to_visit = [(start, 0, 0)]         # pos, depth, steps
        while to_visit:

            pos, depth, steps = to_visit.pop(0)
            if depth == 0 and pos == end:
                return steps

            for sp in self.get_surrounding_points(pos):
                ndepth = depth
                # sp takes us through an inner portal
                if self.is_inner_portal(sp):
                    # go through, increase depth
                    ndepth += 1
                    sp = INCREASE_DEPTH[pos]
                elif self.is_outer_portal(sp) and pos not in [start, end]:
                    # go through, decrease depth
                    ndepth -= 1
                    sp = DECREASE_DEPTH[pos]

                if ndepth < 0 or (sp, ndepth) in visited:
                    continue
                visited.add((sp, ndepth))

                if self.maze.get(sp, "#") == ".":
                    to_visit.append((sp, ndepth, steps+1))

    def is_outer_portal(self, pos):
        x, y = pos
        return x < self.min_x or y < self.min_y or x > self.max_x or y > self.max_y

    def is_inner_portal(self, pos):
        x, y = pos
        return 28 < x < 88 and 28 < y < 86


def main(data, part=None):

    # example
    # start, end = (2, 9), (16, 13)

    # example 2
    # start, end = (34, 15), (2, 13)

    # input
    AA, ZZ = (77, 2), (114, 43)

    maze = Maze(data, AA, ZZ)
    if part == 1:
        return maze.shortest_path(AA, ZZ)
    elif part == 2:
        return maze.shortest_path_2(AA, ZZ)


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE_2, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
