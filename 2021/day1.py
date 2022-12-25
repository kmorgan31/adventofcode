#!/usr/bin/python

from aocd import lines

WINDOW_SIZE = {
    1: 1,
    2: 3
}


def set_range(x, part):
    return x, x+WINDOW_SIZE.get(part, 1)


def main(data, part):
    start, end = set_range(0, part)

    increased = 0
    prev_sum = 0
    while end < len(data):
        next_sum = sum(map(int, data[start:end]))
        if next_sum > prev_sum:
            increased += 1
        prev_sum = next_sum
        start, end = set_range(start+1, part)

    return increased


if __name__ == '__main__':
    print(f'Day 1: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
