#!/usr/bin/python

from aocd import lines

from collections import defaultdict, deque


EXAMPLE = [
    "#.######",
    "#>>.<^<#",
    "#.<..<<#",
    "#>v.><>#",
    "#<^v^^>#",
    "######.#"
]


class Forest:

    def __init__(self, data, start=None, end=None):
        self.height = len(data)
        self.width = len(data[0])
        self.get_blizzards(data)
        self.get_walls(data)

    def get_blizzards(self, data):
        self.blizzards = defaultdict(list)
        for i in range(len(data)):
            line = data[i]
            for j in range(len(line)):
                if data[i][j] in [">", "<", "^", "v"]:
                    self.blizzards[(i, j)].append(data[i][j])

    def get_walls(self, data):
        self.walls = set(
            [(0, y) for y in range(self.width) if data[0][y] != "."] +
            [(self.height-1, y) for y in range(self.width) if data[self.height-1][y] != "."] +
            [(x, 0) for x in range(self.height)] +
            [(x, self.width-1) for x in range(self.height)]
        )

    def get_neighbours(self, pos):
        px, py = pos
        neighbours = [
            (px-1, py), (px+1, py), (px, py-1), (px, py+1)
        ]
        return [
            (i, j) for i, j in neighbours
            if (i, j) not in self.walls and
            (i, j) not in self.blizzards.keys() and
            0 <= i < self.height and 0 <= j < self.width
        ]

    def move_blizzards(self):
        def move_blizzard(blizzard, dir):
            x, y = blizzard
            if d == ">":
                return (x%self.height, (y+1)%self.width)
            elif d == "<":
                return (x%self.height, (y-1)%self.width)
            elif d == "^":
                return ((x-1)%self.height, y%self.width)
            elif d == "v":
                return ((x+1)%self.height, y%self.width)

        new_blizzards = defaultdict(list)
        for b, lst in self.blizzards.items():
            for d in lst:
                x, y = move_blizzard(b, d)
                while (x, y) in self.walls:
                    x, y = move_blizzard((x, y), d)
                new_blizzards[(x, y)].append(d)
        self.blizzards = new_blizzards

    def draw(self, to_visit=None, p=None):
        for i in range(self.height):
            row = ""
            for j in range(self.width):
                if (i, j) in self.walls:
                    row += "#"
                elif (i, j) in self.blizzards:
                    if len(self.blizzards[(i, j)]) == 1:
                        row += self.blizzards[(i, j)][0]
                    else:
                        row += str(len(self.blizzards[(i, j)]))
                elif to_visit and (i, j) in to_visit:
                    row += "N"
                elif (i, j) == p:
                    row += "E"
                else:
                    row += "."
            print(row)

    def traverse(self, start, end):
        mins = 0

        curr_positions = {start}
        while end not in curr_positions:
            self.move_blizzards()

            next_positions = set()
            for p in curr_positions:
                # find the next positions that don't have blizzards or walls
                if p not in self.blizzards and p != start:
                    # wait
                    next_positions.add(p)

                next_positions.update(self.get_neighbours(p))

            # move into new positions
            if not next_positions:
                # abandon that expedition
                # would be better to wait for a better time to traverse
                curr_positions = {start}
            else:
                curr_positions = next_positions

            mins += 1
        return mins


def main(data, part=None):

    forest = Forest(data)

    start = (0, data[0].index("."))
    end = forest.height-1, data[forest.height-1].index(".")

    mins = 0
    points = deque([start, end])
    for i in range(1, 4):
        mins += forest.traverse(*points)

        if part == 1:
            return mins

        points.rotate(-1)

    return mins


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
