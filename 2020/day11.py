#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL"
]


class Plane:

    def __init__(self, data):
        self.max_x = len(data)
        self.max_y = len(data[0])
        self.seats = self.get_seats(data)

        self.immediate_neighbours = {}
        self.get_immediate_neighbours()

        self.closest_neighbours = {}
        self.get_closest_neighbours()

    def get_seats(self, data):
        seats = {}
        for i in range(self.max_x):
            for j in range(self.max_y):
                if data[i][j] == ".":
                    continue
                seats[(i, j)] = data[i][j]
        return seats

    def get_immediate_neighbours(self):
        for seat in self.seats:
            x, y = seat
            self.immediate_neighbours[seat] = [
                (i, j) for i, j in {
                    (x-1, y-1),     # top left
                    (x-1, y),       # left
                    (x-1, y+1),     # bottom left
                    (x, y-1),       # up
                    (x, y+1),       # down
                    (x+1, y-1),     # top right
                    (x+1, y),       # right
                    (x+1, y+1),     # bottom right
                }
                if 0 <= i < self.max_x and 0 <= j < self.max_y
                and (i, j) in self.seats
            ]

    def get_closest_neighbours(self):
        for seat in self.seats:
            x, y = seat

            self.closest_neighbours[seat] = (
                # N
                [(i, y) for i in range(x-1, -1, -1) if (i, y) in self.seats][:1] +
                # E
                [(x, j) for j in range(y+1, self.max_y) if (x, j) in self.seats][:1] +
                # S
                [(i, y) for i in range(x+1, self.max_x) if (i, y) in self.seats][:1] +
                # W
                [(x, j) for j in range(y-1, -1, -1) if (x, j) in self.seats][:1] +
                # NE
                [(i, j) for i, j in zip(range(x-1, -1, -1), range(y+1, self.max_y)) if (i, j) in self.seats][:1] +
                # SE
                [(i, j) for i, j in zip(range(x+1, self.max_x), range(y+1, self.max_y)) if (i, j) in self.seats][:1] +
                # SW
                [(i, j) for i, j in zip(range(x+1, self.max_x), range(y-1, -1, -1)) if (i, j) in self.seats][:1] +
                # NW
                [(i, j) for i, j in zip(range(x-1, -1, -1), range(y-1, -1, -1)) if (i, j) in self.seats][:1]
            )

    def print(self):
        for i in range(self.max_x):
            line = ""
            for j in range(self.max_y):
                if (i, j) not in self.seats:
                    line += "."
                else:
                    line += self.seats[(i, j)]
            print(line)


def main(data, part=None):
    plane = Plane(data)

    while True:
        new_seats = {}
        for seat, state in plane.seats.items():

            neighbours = plane.immediate_neighbours[seat] if part == 1 else plane.closest_neighbours[seat]
            occupied_neighbours = [n for n in neighbours if plane.seats[n] == "#"]

            if state == "L" and len(occupied_neighbours) == 0:
                new_seats[seat] = "#"
            elif part == 1 and state == "#" and len(occupied_neighbours) >= 4:
                new_seats[seat] = "L"
            elif part == 2 and state == "#" and len(occupied_neighbours) >= 5:
                new_seats[seat] = "L"

        if not new_seats:
            break

        plane.seats.update(new_seats)

    return len([x for x in plane.seats.values() if x == "#"])


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
