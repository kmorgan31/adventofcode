#!/usr/bin/python

from aocd import lines

import re
from itertools import product

EXAMPLE = [
    "aaaaa-bbb-z-y-x-123[abxyz]",
    "a-b-c-d-e-f-g-h-987[abcde]",
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]"
]


def parse_line(line):
    line = re.split(r'\[([^\]]+)\]', line)
    return line[::2], line[1::2]


def is_abba(word):
    i = 0
    while i <= len(word)-4:
        a, b, c, d = word[i:i+4]
        if [a,b] == [d,c] and a != b:
            return True
        i += 1
    return False


def is_aba(word):
    i = 0

    abas = []
    while i <= len(word)-3:
        x, y, z = word[i:i+3]
        if x == z and x != y:
            abas.append(''.join([x,y,z]))
        i += 1
    return abas


def supports_tls(outer, inner):
    return any(map(is_abba, outer)) and not any(map(is_abba, inner))


def supports_ssl(outer, inner):
    outer_aba, inner_aba = [], []
    for x in outer:
        outer_aba.extend(is_aba(x))
    for x in inner:
        inner_aba.extend(is_aba(x))

    if not(outer_aba and inner_aba):
        return False

    for o, i in product(outer_aba, inner_aba):
        a, b, c = o
        d, e, f = i
        if a == c == e and d == b == f:
            return True
    return False


def main(data, part=None):
    if part == 1:
        return sum(supports_tls(*parse_line(line)) for line in data)
    elif part == 2:
        return sum(supports_ssl(*parse_line(line)) for line in data)


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
