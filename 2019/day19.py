#!/usr/bin/python

from aocd import lines

from intcode import Intcode


def in_beam(pos):
    y, x = pos
    intcode = Intcode(list(map(int, lines[0].split(","))))
    return intcode.run_instructions([y, x])[0] == 1


def part_1():
    beam = set()
    for x in range(50):
        for y in range(50):
            if in_beam((y, x)):
                beam.add((y, x))
    return len(beam)


def part_2():
    blx, bly = 0, 10
    while True:
        if in_beam((blx, bly)):
            top_right = (blx + 99, bly - 99)
            if in_beam(top_right):
                top_left = (blx, bly - 99)
                return 10000 * top_left[0] + top_left[1]

            blx, bly = blx, bly + 1
        else:
            blx, bly = blx + 1, bly


if __name__ == '__main__':
    print(f'Part 1 {part_1()}')
    print(f'Part 2 {part_2()}')
