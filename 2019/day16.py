#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    # "12345678",
    # "80871224585914546619083218645595",
    "03036732577212944063491565474664"
]

PATTERN = [0, 1, 0, -1]


def part_1(line):
    i = 0
    while i < 100:

        ans = ""
        for j in range(len(line)):
            tmp_pattern = [y for x in zip(*[PATTERN]*(j+1)) for y in x]
            ans += str(abs(
                sum(
                    (int(line[k]) * int(tmp_pattern[(k+1) % len(tmp_pattern)]))
                    for k in range(len(line))
                )
            ) % 10)
        line = ans
        i += 1

    return line[:8]


def part_2(line):
    # repeat puzzle input 10000 times and offset the input
    offset = int(line[:7])
    line = list((line * 10000)[offset:])

    for p in range(100):
        total = 0
        for i in range(len(line)-1, -1, -1):
            total += int(line[i])
            line[i] = str(total % 10)
    return ''.join(line)[:8]


if __name__ == '__main__':
    # print(f'Part 1 {part_2(EXAMPLE[0])}')
    print(f'Part 1 {part_1(lines[0])}')
    print(f'Part 2 {part_2(lines[0])}')
