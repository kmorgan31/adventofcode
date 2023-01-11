#!/usr/bin/python

from hashlib import md5


INPUT = "qljzarfv"


def get_doors_is_open(pos, hashed):
    def is_open(x):
        return x in ["b", "c", "d", "e", "f"]

    x, y = pos
    u, d, l, r = hashed[:4]
    doors = {
        (x-1, y): ("U", is_open(u)),  # up
        (x+1, y): ("D", is_open(d)),  # down
        (x, y-1): ("L", is_open(l)),  # left
        (x, y+1): ("R", is_open(r)),  # right
    }

    return {
        k: v for k,v in doors.items() if
        0 <= k[0] < 4 and 0 <= k[1] < 4
    }


def main(word, part=None):
    max_path = 0

    to_visit = [(0, 0, "")]      # startx, starty, path
    while to_visit:
        x, y, path = to_visit.pop(0)
        if (x, y) == (3, 3):
            if part == 1:
                return path
            else:
                max_path = max(max_path, len(path))
                continue

        hashed = md5((word + path).encode()).hexdigest()
        for sp, is_open in get_doors_is_open((x, y), hashed).items():
            if is_open[1]:
                to_visit.append((sp[0], sp[1], path+is_open[0]))

    if part == 2:
        return max_path


if __name__ == '__main__':
    print(f'Part 1 {main(INPUT, 1)}')
    print(f'Part 2 {main(INPUT, 2)}')
