#!/usr/bin/python

from aocd import lines

from collections import Counter


def main(data, part=None):
    if part == 1:
        return ''.join([
            Counter([line[i] for line in data]).most_common()[0][0]
            for i in range(len(data[0]))
        ])
    elif part == 2:
        return ''.join([
            Counter([line[i] for line in data]).most_common()[-1][0]
            for i in range(len(data[0]))
        ])


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
