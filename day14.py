#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9"
]


def get_points_on_line(coord_1, coord_2):
    coords = []
    if coord_1[0] == coord_2[0]:
        # same col, diff row
        col = coord_1[0]
        for row in range(
            min(coord_1[1], coord_2[1]), max((coord_1[1], coord_2[1]))+1
        ):
            coords.append((col, row))
    elif coord_1[1] == coord_2[1]:
        # same row, diff col
        row = coord_1[1]
        for col in range(
            min(coord_1[0], coord_2[0]), max((coord_1[0], coord_2[0]))+1
        ):
            coords.append((col, row))
    return coords


class Cave:

    def __init__(self, part):
        # stores x,y coords that already have rock or sand
        self.rocks = set()
        self.sand = set()
        self.part = part

    def plot_rocks(self, data, part):
        for line in data:
            coords = line.split(" -> ")
            coords = map(lambda x: x.split(","), coords)
            coords = list(map(lambda x: (int(x[0]), int(x[1])), coords))

            i = 0
            for i in range(len(coords)-1):
                coord_1, coord_2 = coords[i:i+2]
                self.rocks.update(get_points_on_line(coord_1, coord_2))

        self.lowest_rock = max([x[1] for x in self.rocks])
        self.floor = self.lowest_rock + 2

    def drop_sand(self, point):
        x, y = point

        if self.part == 2 and y == self.floor-1:
            self.sand.add(point)
            return False
        if y > self.lowest_rock:
            return True

        down_p = (x, y+1)
        left_p = (x-1, y+1)
        right_p = (x+1, y+1)

        if down_p not in self.rocks and down_p not in self.sand:
            return self.drop_sand(down_p)
        elif left_p not in self.rocks and left_p not in self.sand:
            return self.drop_sand(left_p)
        elif right_p not in self.rocks and right_p not in self.sand:
            return self.drop_sand(right_p)
        else:
            self.sand.add(point)
            return point == (500, 0)

    def draw_cave(self):
        rocks_and_sand = self.rocks | self.sand | {(500, 0)}

        min_row = min([x[0] for x in rocks_and_sand])
        max_row = max([x[0] for x in rocks_and_sand])

        min_col = min([x[1] for x in rocks_and_sand])
        max_col = max([x[1] for x in rocks_and_sand])

        for j in range(min_col, max_col+1):
            line = ""
            for i in range(min_row, max_row+1):
                if (i, j) in self.rocks:
                    line += "#"
                elif (i, j) in self.sand:
                    line += "o"
                elif (i, j) == (500, 0):
                    line += "+"
                else:
                    line += "."
            print(line)
        print("#" * (abs(max_row-min_row)+1))


def main(data, part=None):
    cave = Cave(part)
    cave.plot_rocks(data, part)

    ans = False
    while not ans:
        ans = cave.drop_sand((500, 0))

    return(len(cave.sand))


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
