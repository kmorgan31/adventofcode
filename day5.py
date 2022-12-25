#!/usr/bin/python

from aocd import lines


def parse_coords(data):
    coords = []
    for line in data:
        x, y = line.split(' -> ')
        x1, y1 = map(int, x.split(','))
        x2, y2 = map(int, y.split(','))
        coords.append([(x1, y1), (x2, y2)])
    return coords


def determine_points(a, b):
    x1, y1 = a
    x2, y2 = b
    d = (x2 - x1, y2 - y1)

    if d[0] == 0:
        steps = abs(d[1])
    else:
        steps = abs(d[0])

    d = (d[0] // steps, d[1] // steps)

    points = []
    while a != b:
        points.append(a)
        a = (a[0] + d[0], a[1] + d[1])
    points.append(b)

    return points


def main(coords, part):
    floor_map = {}
    for a, b in coords:
        if part == 1:
            if a[0] != b[0] and a[1] != b[1]:
                continue

        points = determine_points(a, b)
        if not points:
            continue

        for point in points:
            if floor_map.get(point):
                floor_map[point] += 1
            else:
                floor_map[point] = 1

    return {
        k for k, v in floor_map.items() if v >= 2
    }


if __name__ == '__main__':
    coords = parse_coords(lines)

    print(f'Day 5: Part 1 {len(main(coords, 1))}, Part 2 {len(main(coords, 2))}')
