#!/usr/bin/python

from aocd import lines


PART_1 = {
    (0, 0): "1",
    (0, 1): "2",
    (0, 2): "3",
    (1, 0): "4",
    (1, 1): "5",
    (1, 2): "6",
    (2, 0): "7",
    (2, 1): "8",
    (2, 2): "9"
}

PART_2 = {
    (0, 2): "1",
    (1, 1): "2",
    (1, 2): "3",
    (1, 3): "4",
    (2, 0): "5",
    (2, 1): "6",
    (2, 2): "7",
    (2, 3): "8",
    (2, 4): "9",
    (3, 1): "A",
    (3, 2): "B",
    (3, 3): "C",
    (4, 2): "D"
}


def main(data, part=None):
    if part == 1:
        x, y = (1, 1)  # start (5)
        keypad = PART_1
    elif part == 2:
        x, y = (2, 0)  # start (5)
        keypad = PART_2

    code = []
    for line in data:
        for step in line:
            nx, ny = x, y
            if step == "U":
                nx = x-1
            elif step == "R":
                ny = y+1
            elif step == "D":
                nx = x+1
            elif step == "L":
                ny = y-1

            if keypad.get((nx, ny)):
                x, y = nx, ny

        code.append(keypad[(x, y)])
    return ''.join(code)


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
