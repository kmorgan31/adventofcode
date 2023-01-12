#!/usr/bin/python

from aocd import lines

import re


def main(data, part=None):
    grid = {
        (x,y): 0 for x in range(1000) for y in range(1000)
    }

    for line in data:
        command = line.split()
        px, py, qx, qy = map(int, re.findall(r'\d+', line))

        if part == 1:
            for x in range(px, qx+1):
                for y in range(py, qy+1):
                    if command[0] == "turn":
                        if command[1] == "on":
                            grid[(x,y)] = 1
                        elif command[1] == "off":
                            grid[(x,y)] = 0
                    elif command[0] == "toggle":
                        grid[(x,y)] = 1 if grid[(x,y)] == 0 else 0
        elif part == 2:
            for x in range(px, qx+1):
                for y in range(py, qy+1):
                    if command[0] == "turn":
                        if command[1] == "on":
                            grid[(x,y)] += 1
                        elif command[1] == "off":
                            grid[(x,y)] = max(0, grid[(x,y)]-1)
                    elif command[0] == "toggle":
                        grid[(x,y)] += 2

    return sum(grid.values())


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
