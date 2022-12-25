#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "        ...# ",
    "        .#.. ",
    "        #... ",
    "        .... ",
    "...#.......#",
    "........#...",
    "..#....#....",
    "..........#.",
    "        ...#....",
    "        .....#..",
    "        .#......",
    "        ......#.",
    "",
    "10R5L5R10L4R5L5"
]

COMPASS = ["E", "S", "W", "N"]


class Person:

    def __init__(self, pos, facing):
        self.pos = pos
        self.facing = facing  # N, E, S, W

    def get_next_pos(self, grid, x, y, f):
        if ((x, y), f) in grid.edges:
            np, nf = grid.edges[((x, y), f)]
            return np[0], np[1], nf

        if f == "N":
            x = (x-1)%grid.max_height
        elif f == "S":
            x = (x+1)%grid.max_height
        elif f == "E":
            y = (y+1)%grid.max_width
        elif f == "W":
            y = (y-1)%grid.max_width
        return x, y, f

    def move_forward(self, grid, spaces):
        for i in range(spaces):
            try:
                nx, ny, nf = self.get_next_pos(grid, self.pos[0], self.pos[1], self.facing)
                if grid.grid[nx][ny] == " ":
                    while grid.grid[nx][ny] == " ":
                        # move forward until back onto map
                        nx, ny, nf = self.get_next_pos(grid, nx, ny, nf)

                if grid.grid[nx][ny] == "#":
                    break
            except Exception:
                import pdb; pdb.set_trace()

            self.pos = (nx, ny)
            self.facing = nf

    def change_direction(self, turn):
        if turn == "R":
            self.facing = COMPASS[(COMPASS.index(self.facing)+1) % len(COMPASS)]
        elif turn == "L":
            self.facing = COMPASS[(COMPASS.index(self.facing)-1) % len(COMPASS)]


class Grid:

    def __init__(self, data, part):
        self.edges = {}
        self.max_height = len(data[:-2])
        self.max_width = max(map(len, data[:-2]))

        self.part = part
        self.cube_size = 4 if "E" in self.part else 50

        self.parse(data)

    def parse(self, data):
        self.grid = []
        for line in data[:-2]:
            self.grid.append(list(line.ljust(self.max_width)))

        self.instructions = data[-1]

    def join_edges(self, e1, e2, d1, d2):
        for i in range(len(e1)):
            p1, p2 = e1[i], e2[i]

            # add edges
            self.edges[(p1, d1)] = (p2, d2)

            nd1 = COMPASS[(COMPASS.index(d1)+2) % len(COMPASS)]
            nd2 = COMPASS[(COMPASS.index(d2)+2) % len(COMPASS)]
            self.edges[(p2, nd2)] = (p1, nd1)

    def get_face_boundaries(self):
        # determine the next pos if you land on an edge of the cube

        if "2" not in self.part:
            return

        if "E" in self.part:
            """
                    1111
                    1111
                    1111
                    1111
            222233334444
            222233334444
            222233334444
            222233334444
                    55556666
                    55556666
                    55556666
                    55556666
            """

            # FACE 1: 2
            self.join_edges(
                [(0, y) for y in range(self.cube_size*2, self.cube_size*3)],
                [(self.cube_size*1, y) for y in range(self.cube_size*1-1, -1, -1)],
                "N", "S"
            )
            # FACE 1: 3
            self.join_edges(
                [(x, self.cube_size*2) for x in range(0, self.cube_size*1)],
                [(self.cube_size*1, y) for y in range(self.cube_size*1, self.cube_size*2)],
                "W", "S"
            )
            # FACE 1: 6
            self.join_edges(
                [(x, self.cube_size*3-1) for x in range(0, self.cube_size*1)],
                [(x, self.cube_size*4-1) for x in range(self.cube_size*4-1, self.cube_size*3-1, -1)],
                "E", "W"
            )
            # FACE 2: 6
            self.join_edges(
                [(x, 0) for x in range(self.cube_size*1, self.cube_size*2)],
                [(self.cube_size*3-1, y) for y in range(self.cube_size*4-1, self.cube_size*3-1, -1)],
                "W", "N"
            )
            # FACE 2: 5
            self.join_edges(
                [(self.cube_size*2-1, y) for y in range(0, self.cube_size*1)],
                [(self.cube_size*3-1, y) for y in range(self.cube_size*3-1, self.cube_size*2-1, -1)],
                "S", "N"
            )
            # FACE 3: 5
            self. join_edges(
                [(self.cube_size*2-1, y) for y in range(self.cube_size*1, self.cube_size*2)],
                [(x, self.cube_size*2) for x in range(self.cube_size*3-1, self.cube_size*2-1, -1)],
                "S", "E"
            )
            # FACE 4: 6
            self.join_edges(
                [(x, self.cube_size*3-1) for x in range(self.cube_size*1, self.cube_size*2)],
                [(self.cube_size*2, y) for y in range(self.cube_size*4-1, self.cube_size*3-1, -1)],
                "E", "S"
            )

        else:
            """
                 a  b
                111222
              c 111222 e
                111222
                333 d
              f 333 d
              f 333
             444555
           c 444555 e
             444555
             666 g
           a 666 g
             666
              b
            """

            # FACE 1: 6 (a)
            self.join_edges(
                [(0, y) for y in range(self.cube_size*1, self.cube_size*2)],
                [(x, 0) for x in range(self.cube_size*3, self.cube_size*4)],
                "N", "E"
            )
            # FACE 1: 4 (c)
            self.join_edges(
                [(x, self.cube_size*1) for x in range(0, self.cube_size*1)],
                [(x, 0) for x in range(self.cube_size*3-1, self.cube_size*2-1, -1)],
                "W", "E"
            )
            # FACE 2: 3 (d)
            self.join_edges(
                [(self.cube_size*1-1, y) for y in range(self.cube_size*2, self.cube_size*3)],
                [(x, self.cube_size*2-1) for x in range(self.cube_size*1, self.cube_size*2)],
                "S", "W"
            )
            # FACE 2: 5 (e)
            self.join_edges(
                [(x, self.cube_size*3-1) for x in range(0, self.cube_size*1)],
                [(x, self.cube_size*2-1) for x in range(self.cube_size*3-1,self.cube_size*2-1, -1)],
                "E", "W"
            )
            # FACE 2: 6 (b)
            self.join_edges(
                [(0, y) for y in range(self.cube_size*2, self.cube_size*3)],
                [(self.cube_size*4-1, y) for y in range(0, self.cube_size*1)],
                "N", "N"
            )
            # FACE 3: 4 (f)
            self.join_edges(
                [(x, self.cube_size*1) for x in range(self.cube_size*1, self.cube_size*2)],
                [(self.cube_size*2, y) for y in range(0, self.cube_size*1)],
                "W", "S"
            )
            # FACE 5: 6 (g)
            self.join_edges(
                [(self.cube_size*3-1, y) for y in range(self.cube_size*1, self.cube_size*2)],
                [(x, self.cube_size*1-1) for x in range(self.cube_size*3, self.cube_size*4)],
                "S", "W"
            )


def main(data, part=None):

    grid = Grid(data, part)
    grid.get_face_boundaries()
    person = Person((0, grid.grid[0].index(".")), "E")

    y = ""
    for x in range(len(grid.instructions)):
        curr_letter = grid.instructions[x]
        if curr_letter in ["L", "R"]:
            person.move_forward(grid, int(y))
            person.change_direction(curr_letter)

            # clear stream
            y = ""
        else:
            y += curr_letter

    if y:
        person.move_forward(grid, int(y))

    return (
        1000 * (person.pos[0] + 1) + 4 * (person.pos[1] + 1) +
        COMPASS.index(person.facing)
    )


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, "E2")}')
    print(f'Part 1 {main(lines, "1")}')
    print(f'Part 2 {main(lines, "2")}')
