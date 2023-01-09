#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "ADVENT",
    "A(1x5)BC",
    "(3x3)XYZ",
    "A(2x2)BCD(2x2)EFG",
    "(6x1)(1x3)A",
    "X(8x2)(3x3)ABCY"
]

EXAMPLE_2 = [
    "(3x3)XYZ",
    "X(8x2)(3x3)ABCY",
    "(27x12)(20x12)(13x14)(7x10)(1x12)A",
    "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
]


def has_marker(section):
    return '(' in section and ")" in section


def decompress(line, part=None):
    if not has_marker(line):
        return len(line)

    res = 0
    while has_marker(line):
        # find first marker
        res += line.find('(')
        line = line[line.find('('):]

        # get marker
        mx, my = list(map(int, line[1:line.find(')')].split('x')))

        # update line to remove marker
        line = line[line.find(')')+1:]

        if part == 2:
            # decompress mx characters of string, including inner markers
            res += decompress(line[:mx], part=part) * my
        else:
            # decompress mx characters of string, ignore inner markers
            res += len(line[:mx]) * my

        # move along line
        line = line[mx:]

    # update res with remaining length of line
    res += len(line)
    return res


def prep_data(data):
    return ''.join(data)


if __name__ == '__main__':
    # print(f'Example {decompress(prep_data(EXAMPLE_2), 2)}')
    print(f'Part 1 {decompress(prep_data(lines), 1)}')
    print(f'Part 2 {decompress(prep_data(lines), 2)}')
