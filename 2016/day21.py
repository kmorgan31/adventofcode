#!/usr/bin/python

from aocd import lines

from collections import deque


EXAMPLE = [
    "swap position 4 with position 0",
    "swap letter d with letter b",
    "reverse positions 0 through 4",
    "rotate left 1 step",
    "move position 1 to position 4",
    "move position 3 to position 0",
    "rotate based on position of letter b",
    "rotate based on position of letter d"
]


def scramble(data, word):
    inp = deque(word)
    for line in data:
        line = line.split()

        if line[0] == "swap":
            if line[1] == "position":
                x, y = int(line[2]), int(line[5])
            elif line[1] == "letter":
                x, y = inp.index(line[2]), inp.index(line[5])
            inp[x], inp[y] = inp[y], inp[x]
        elif line[0] == "rotate":
            if line[1] == "left":
                inp.rotate(-int(line[2]))
            elif line[1] == "right":
                inp.rotate(int(line[2]))
            elif line[5] == "letter":
                idx = inp.index(line[6])
                num_rotate = idx + 1 + (1 if idx >= 4 else 0)
                inp.rotate(num_rotate)
        elif line[0] == "reverse":
            tmp = list(inp)
            x, y = int(line[2]), int(line[4])
            inp = deque(tmp[:x] + tmp[x:y+1][::-1] + tmp[y+1:])
        elif line[0] == "move":
            x = inp[int(line[2])]
            inp.remove(x)
            inp.insert(int(line[5]), x)
        print(f"Line {' '.join(line)}: s: {''.join(inp)}")

    return ''.join(inp)


def unscramble(data, word):
    # pos, rotate val
    inverse_rotate = {
        0: -1,
        1: -1,
        2: 2,
        3: -2,
        4: 1,
        5: -3,
        7: 4
    }

    inp = deque(word)
    for line in data[::-1]:
        line = line.split()

        if line[0] == "swap":
            if line[1] == "position":
                x, y = int(line[2]), int(line[5])
            elif line[1] == "letter":
                x, y = inp.index(line[2]), inp.index(line[5])
            inp[x], inp[y] = inp[y], inp[x]
        elif line[0] == "rotate":
            if line[1] == "left":
                inp.rotate(int(line[2]))
            elif line[1] == "right":
                inp.rotate(-int(line[2]))
            elif line[5] == "letter":
                rot = inverse_rotate.get(inp.index(line[6]))
                if rot:
                    inp.rotate(rot)
        elif line[0] == "reverse":
            tmp = list(inp)
            x, y = int(line[2]), int(line[4])
            inp = deque(tmp[:x] + tmp[x:y+1][::-1] + tmp[y+1:])
        elif line[0] == "move":
            x = inp[int(line[5])]
            inp.remove(x)
            inp.insert(int(line[2]), x)

    return ''.join(inp)


if __name__ == '__main__':
    # print(f'EXAMPLE {scramble(EXAMPLE, "abcde")}')
    # print(f'EXAMPLE {unscramble(EXAMPLE, "decab")}')
    print(f'Part 1 {scramble(lines, "abcdefgh")}')
    print(f'Part 2 {unscramble(lines, "fbgdceah")}')
