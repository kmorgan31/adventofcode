#!/usr/bin/python

from aocd import lines


def main(line, part=None):
    if part == 1:
        return line.count("(") - line.count(")")
    elif part == 2:
        ans = 0
        for i, char in enumerate(line, start=1):
            ans += 1 if char == "(" else -1
            if ans == -1:
                return i


if __name__ == '__main__':
    print(f'Part 1 {main(lines[0], 1)}')
    print(f'Part 2 {main(lines[0], 2)}')
