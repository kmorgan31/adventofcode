#!/usr/bin/python

from aocd import lines

from day20_example import (
    EXAMPLE,
    EXAMPLE_INCREASE_DEPTH,
    EXAMPLE_DECREASE_DEPTH
)
from day20_example2 import (
    EXAMPLE_2,
    EXAMPLE_2_INCREASE_DEPTH,
    EXAMPLE_2_DECREASE_DEPTH
)


# inner to outer
INCREASE_DEPTH = {
    (28, 73): (2, 65),      # YY
    (28, 41): (2, 31),      # YI
    (28, 35): (81, 2),      # ER
    (28, 45): (71, 2),      # VB
    (28, 61): (65, 2),      # WT
    (28, 53): (114, 67),    # UH
    (28, 63): (53, 112),    # LD
    (28, 79): (114, 37),    # JR
    (71, 28): (2, 59),      # LH
    (45, 28): (35, 112),    # KB
    (37, 28): (114, 49),    # FR
    (53, 28): (114, 81),    # BI
    (65, 28): (114, 57),    # SG
    (77, 28): (85, 112),    # DU
    (88, 55): (2, 77),      # HM
    (88, 59): (39, 2),      # RX
    (88, 47): (57, 2),      # YT
    (88, 77): (57, 112),    # BB
    (88, 67): (77, 112),    # KU
    (88, 37): (114, 63),    # TS
    (39, 86): (2, 39),      # PO
    (35, 86): (2, 51),      # JJ
    (73, 86): (2, 67),      # NS
    (81, 86): (2, 73),      # QG
    (65, 86): (43, 2),      # PU
    (47, 86): (39, 112),    # YB
    (59, 86): (65, 112),    # JN
}

# outer to inner
DECREASE_DEPTH = {
    (2, 31): (28, 41),      # YI
    (2, 39): (39, 86),      # PO
    (2, 51): (35, 86),      # JJ
    (2, 59): (71, 28),      # LH
    (2, 65): (28, 73),      # YY
    (2, 67): (73, 86),      # NS
    (2, 73): (81, 86),      # QG
    (2, 77): (88, 55),      # HM
    (39, 2): (88, 59),      # RX
    (81, 2): (28, 35),      # ER
    (71, 2): (28, 45),      # VB
    (65, 2): (28, 61),      # WT
    (43, 2): (65, 86),      # PU
    (57, 2): (88, 47),      # YT
    (114, 67): (28, 53),    # UH
    (114, 37): (28, 79),    # JR
    (114, 49): (37, 28),    # FR
    (114, 81): (53, 28),    # BI
    (114, 57): (65, 28),    # SG
    (114, 63): (88, 37),    # TS
    (35, 112): (45, 28),    # KB
    (53, 112): (28, 63),    # LD
    (85, 112): (77, 28),    # DU
    (39, 112): (47, 86),    # YB
    (65, 112): (59, 86),    # JN
    (57, 112): (88, 77),    # BB
    (77, 112): (88, 67),    # KU
}


class Maze:

    def __init__(self, data, start, end):
        self.maze = {}
        self.start = start
        self.end = end
        self.parse_data(data)

    def parse_data(self, data):
        for x, line in enumerate(data):
            for y, l in enumerate(line):
                pos = (x, y)

                if l in ["#", "."]:
                    self.maze[pos] = l

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

    def get_surrounding_points(self, pos, depth):
        x, y = pos
        surrounding_points = [
            (sp, depth) for sp in [
                (x, y-1),
                (x, y+1),
                (x-1, y),
                (x+1, y)
            ]
            if self.min_x <= sp[0] <= self.max_x and
            self.min_y <= sp[1] <= self.max_y
        ]

        if pos in DECREASE_DEPTH:
            surrounding_points.append((DECREASE_DEPTH[pos], depth-1))
        elif pos in INCREASE_DEPTH:
            surrounding_points.append((INCREASE_DEPTH[pos], depth+1))

        # if EXAMPLE_DECREASE_DEPTH.get(pos):
        #     surrounding_points.append((EXAMPLE_DECREASE_DEPTH.get(pos), depth-1))
        # elif EXAMPLE_INCREASE_DEPTH.get(pos):
        #     surrounding_points.append((EXAMPLE_INCREASE_DEPTH.get(pos), depth+1))

        # if EXAMPLE_2_DECREASE_DEPTH.get(pos):
        #     surrounding_points.append((EXAMPLE_2_DECREASE_DEPTH.get(pos), depth-1))
        # elif EXAMPLE_2_INCREASE_DEPTH.get(pos):
        #     surrounding_points.append((EXAMPLE_2_INCREASE_DEPTH.get(pos), depth+1))

        return surrounding_points

    def shortest_path(self, start, end):
        visited = set()

        to_visit = [(start, 0)]         # steps, curr_pos
        while to_visit:
            pos, steps = to_visit.pop(0)
            visited.add(pos)

            if pos == end:
                return steps

            for sp, depth in self.get_surrounding_points(pos, 0):
                if self.maze.get(sp, "#") == "." and sp not in visited:
                    to_visit.append((sp, steps+1))

            # self.print_maze(pos, to_visit=to_visit)
            # import pdb; pdb.set_trace()

    def shortest_path_2(self, start, end):
        visited = set()

        steps = 0
        to_visit = [(start, 0)]         # pos, depth, steps
        while to_visit:

            new_to_visit = []
            for x in to_visit:
                pos, depth = x
                if depth == 0 and pos == end:
                    return steps

                visited.add((pos, depth))

                for sp, depth in self.get_surrounding_points(pos, depth):
                    if depth < 0 or (sp, depth) in visited:
                        continue
                    if self.maze.get(sp, "#") == ".":
                        new_to_visit.append((sp, depth))

            if steps > 1 and steps % 1000 == 0:
                depths = [x[1] for x in new_to_visit]
                a, b = min(depths), max(depths)
                print(f"step {steps}, to_visit {len(new_to_visit)} pos, in levels {a} to {b}")

                # self.print_maze(pos, to_visit=new_to_visit)
                # import pdb; pdb.set_trace()

            to_visit = new_to_visit
            steps += 1


def main(data, part=None):

    # example
    # start, end = (2, 9), (16, 13)

    # example 2
    # start, end = (34, 15), (2, 13)

    # input
    start, end = (77, 2), (114, 43)

    maze = Maze(data, start, end)
    if part == 1:
        return maze.shortest_path(start, end)
    elif part == 2:
        return maze.shortest_path_2(start, end)


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE_2, 2)}')
    # print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
