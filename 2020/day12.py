#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11"
]

COMPASS = ["N", "E", "S", "W"]
ROTATION = {
    90: lambda x, y: (-y, x),
    180: lambda x, y: (-x, -y),
    270: lambda x, y: (y, -x)
}


def part_1(data):
    x, y = 0, 0
    facing = "E"

    for line in data:
        d, v = line[0], int(line[1:])

        if d == "F":
            d = facing

        if d == "N":
            x -= v
        elif d == "S":
            x += v
        elif d == "E":
            y += v
        elif d == "W":
            y -= v
        elif d == "L":
            facing = COMPASS[(COMPASS.index(facing)-(v//90)) % 4]
        elif d == "R":
            facing = COMPASS[(COMPASS.index(facing)+(v//90)) % 4]

    return abs(x) + abs(y)


def print_xy(x, y):
    x_dir = "S" if x > 0 else "N"
    y_dir = "E" if y > 0 else "W"
    return f"{abs(y)}{y_dir}", f"{abs(x)}{x_dir}"


def part_2(data):
    x, y = 0, 0
    wx, wy = -1, 10

    for line in data:
        d, v = line[0], int(line[1:])
        if d == "N":
            wx -= v
        elif d == "S":
            wx += v
        elif d == "E":
            wy += v
        elif d == "W":
            wy -= v
        elif d == "L":
            wx, wy = ROTATION[v](wx, wy)
        elif d == "R":
            wx, wy = ROTATION[360-v](wx, wy)
        elif d == "F":
            dx, dy = (wx*v), (wy*v)
            x, y = x+dx, y+dy
    return abs(x) + abs(y)


if __name__ == '__main__':
    # print(f'EXAMPLE {part_2(EXAMPLE)}')
    print(f'Part 1 {part_1(lines)}')
    print(f'Part 2 {part_2(lines)}')
