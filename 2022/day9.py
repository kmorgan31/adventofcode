#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2"
]

EXAMPLE_2 = [
    "R 5",
    "U 8",
    "L 8",
    "D 3",
    "R 17",
    "D 10",
    "L 25",
    "U 20"
]


class Knot():

    def __init__(self, name):
        self.name = name
        self.pos_x = 0
        self.pos_y = 0
        self.visited = {(0, 0)}

    def move(self, direction):
        if "R" in direction:
            self.pos_x += 1
        if "L" in direction:
            self.pos_x -= 1
        if "U" in direction:
            self.pos_y += 1
        if "D" in direction:
            self.pos_y -= 1

    def determine_direction(self, knot):
        # determine direction to move current knot to touch given knot (H)
        x = knot.pos_x - self.pos_x
        y = knot.pos_y - self.pos_y

        direction = ""
        if x == 2:
            direction = "R"
            if y > 0:
                direction += "U"
            elif y < 0:
                direction += "D"
        elif x == -2:
            direction = "L"
            if y > 0:
                direction += "U"
            elif y < 0:
                direction += "D"
        elif y == 2:
            direction = "U"
            if x > 0:
                direction += "R"
            elif x < 0:
                direction += "L"
        elif y == -2:
            direction = "D"
            if x > 0:
                direction += "R"
            elif x < 0:
                direction += "L"
        return direction

    def visit(self):
        self.visited.add((self.pos_x, self.pos_y))

    def print_knot(self):
        print(f'{self.name}: ({self.pos_x}, {self.pos_y})')


def main(data, part=None):
    len_rope = 2 if part == 1 else 10
    rope = [Knot(str(x)) for x in range(len_rope)]

    for line in data:
        direction, steps = line.split()

        for x in range(int(steps)):
            # move H one step
            rope[0].move(direction)

            for y in range(1, len(rope)):
                # determine direction T should move
                rope[y].move(rope[y].determine_direction(rope[y-1]))
                rope[y].visit()

    return len(rope[-1].visited)


if __name__ == '__main__':
    # print(f'Example  {main(EXAMPLE, 1)}')
    # print(f'Example  {main(EXAMPLE_2, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
