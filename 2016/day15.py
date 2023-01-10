#!/usr/bin/python

INPUT = [
    # disc_num, period, start_pos
    (1, 13, 11),
    (2, 5, 0),
    (3, 17, 11),
    (4, 3, 0),
    (5, 7, 2),
    (6, 19, 17)
]


def part_1(data):
    i, d = 0, 1
    for offset, b, start_pos in data:
        while True:
            i += d
            if (i + offset + start_pos) % b == 0:
                d *= b
                break
    return i


def part_2(data):
    return part_1(data + [(7, 11, 0)])


if __name__ == '__main__':
    print(f'Part 1 {part_1(INPUT)}')
    print(f'Part 2 {part_2(INPUT)}')
