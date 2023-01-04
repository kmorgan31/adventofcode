#!/usr/bin/python

from aocd import lines

from intcode import Intcode


def get_surrounding_points(pos):
    x, y = pos
    return [
        (x, y-1),   # N
        (x, y+1),   # S
        (x-1, y),   # W
        (x+1, y)    # E
    ]


def print_map(visited, pos=None, to_visit=None):
    xvals = [x[0] for x in visited]
    yvals = [x[1] for x in visited]

    dct = {
        0: "#",
        1: ".",
        2: "O"
    }

    for x in range(min(xvals)-1, max(xvals)+2):
        line = ""
        for y in range(min(yvals)-1, max(yvals)+2):
            val = visited.get((x, y))
            if (x, y) == pos:
                line += "R"
            elif to_visit and (x, y) in to_visit:
                line += str(to_visit.index((x, y)))
            elif (x,y) == (0,0):
                line += "S"
            elif val is not None:
                line += dct.get(val, val)
            else:
                line += " "
        print(line)


def navigate_map(points, start):
    visited = set()
    to_visit = [(start, 0)]

    while to_visit:
        pos, step = to_visit.pop(0)
        visited.add(pos)

        # get possible locations to visit
        for d, sp in enumerate(get_surrounding_points(pos)):
            if sp not in visited:
                # get item at point
                point = points.get(sp, 0)
                if point == 2:
                    return (sp, step+1)
                elif point == 1:
                    to_visit.append((sp, step+1))


def fill_map(points, start):
    visited = set()
    to_visit = [start]

    mins = -1
    while to_visit:

        new_to_visit = []
        while to_visit:
            pos = to_visit.pop()
            visited.add(pos)
            points[pos] = 2

            for sp in get_surrounding_points(pos):
                if sp not in visited and points.get(sp, 0) == 1:
                    new_to_visit.append(sp)
        to_visit = new_to_visit
        mins += 1
    return mins


def plot_map(intcode):
    visited_intcodes = {(0, 0): intcode}
    visited_points = {}

    to_visit = [(0, 0)]
    while to_visit:
        x, y = to_visit.pop(0)

        for d, sp in enumerate(get_surrounding_points((x, y))):
            if sp not in visited_points:
                # copy the intcode and run with the direction
                intcode = visited_intcodes[(x, y)].copy()
                status = intcode.run_instructions(d+1)[0]

                # add new point to visited
                visited_intcodes[sp] = intcode
                visited_points[sp] = status

                # add new space to to_visit queue
                if status != 0:
                    # didn't hit a wall
                    to_visit.append(sp)

    return visited_points


def main(data, part=None):
    intcode = Intcode(list(map(int, lines[0].split(","))))
    points = plot_map(intcode)

    oxygen, steps = navigate_map(points, (0, 0))

    if part == 1:
        return steps
    elif part == 2:
        return fill_map(points, oxygen)


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
