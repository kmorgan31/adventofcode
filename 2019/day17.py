#!/usr/bin/python

from aocd import lines

from intcode import Intcode


TURN = ["U", "R", "D", "L"]

FACING = {
    "U": "^",
    "R": ">",
    "D": "v",
    "L": "<"
}


def get_surrounding_points(pos):
    x, y = pos
    return [
        (x, y-1),   # N
        (x, y+1),   # S
        (x-1, y),   # W
        (x+1, y)    # E
    ]


def print_map(visited, pos=None, facing=None):
    xvals = [x[0] for x in visited]
    yvals = [x[1] for x in visited]

    for y in range(min(yvals)-1, max(yvals)+2):
        line = ""
        for x in range(min(xvals)-1, max(xvals)+2):
            val = visited.get((x, y))
            if (x, y) == pos:
                line += FACING.get(facing)
            elif val is not None:
                line += val
            else:
                line += " "
        print(line)


def navigate_map(points, intersections, robot, facing):
    path = []

    steps = 0
    while points - intersections:
        turn = None
        # try going forward
        new_pos = go_forward(robot, facing)
        if new_pos not in points:
            # add current steps to path and reset
            if steps:
                path.append(str(steps))
            steps = 0

            # try right
            turn, new_facing = "R", TURN[(TURN.index(facing)+1) % 4]
            new_pos = go_forward(robot, new_facing)

        if new_pos not in points:
            # try left
            turn, new_facing = "L", TURN[(TURN.index(facing)-1) % 4]
            new_pos = go_forward(robot, new_facing)

        # update robot
        robot = new_pos
        facing = new_facing

        if new_pos not in intersections:
            points.remove(new_pos)

        if turn:
            path.append(turn)

        steps += 1
    if steps:
        path.append(str(steps))
    return ','.join(path)


def go_forward(robot, facing):
    x, y = robot
    if facing == "U":
        return x, y-1
    elif facing == "R":
        return x+1, y
    elif facing == "D":
        return x, y+1
    elif facing == "L":
        return x-1, y


def get_scaffold_map(intcode):
    scaffold_map = {}

    while not intcode.halted:
        output = intcode.run_instructions()

    # parse output
    i, j = 0, 0
    while output:
        o = output.pop(0)
        if chr(o) == "\n":
            i = 0
            j += 1
            continue

        scaffold_map[(i, j)] = chr(o)
        i += 1

    return scaffold_map


def get_robot_pos(scaffold_map):
    for x, y in scaffold_map.items():
        if y == "^":
            return x, "U"
        elif y == ">":
            return x, "R"
        elif y == "v":
            return x, "D"
        elif y == "<":
            return x, "L"


def main(data, part=None):
    intcode = Intcode(list(map(int, lines[0].split(","))))
    scaffold_map = get_scaffold_map(intcode)
    # import pdb; pdb.set_trace()

    scaffold_points = set(x for x, y in scaffold_map.items() if y == "#")
    robot_pos, robot_facing = get_robot_pos(scaffold_map)

    intersections = set()
    for x, y in scaffold_points:
        if not (set(get_surrounding_points((x, y))) - scaffold_points):
            intersections.add((x, y))

    if part == 1:
        return sum(x*y for x, y in intersections)

    elif part == 2:
        # map path along scaffolding
        print_map(scaffold_map)
        navigate_map(scaffold_points, intersections, robot_pos, robot_facing)

        """
        R,12,L,8,R,12,              # A
        R,8,R,6,R,6,R,8,            # B
        R,12,L,8,R,12,              # A
        R,8,R,6,R,6,R,8,            # B
        R,8,L,8,R,8,R,4,R,4,        # C
        R,8,L,8,R,8,R,4,R,4,        # C
        R,8,R,6,R,6,R,8,            # B
        R,8,L,8,R,8,R,4,R,4,        # C
        R,8,R,6,R,6,R,8,            # B
        R,12,L,8,R,12               # A
        """

        inputs = [
            "A,B,A,B,C,C,B,C,B,A",
            "R,12,L,8,R,12",
            "R,8,R,6,R,6,R,8",
            "R,8,L,8,R,8,R,4,R,4",
            "n"
        ]

        intcode = Intcode(list(map(int, lines[0].split(","))))
        intcode.instructions[0] = 2

        i = 0
        while not intcode.halted:
            output = intcode.run_instructions([ord(x) for x in inputs[i]] + [10])
            if intcode.waiting:
                i += 1

        return output[-1]


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
