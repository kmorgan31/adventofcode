#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "....#",
    "#..#.",
    "#..##",
    "..#..",
    "#...."
]


class Eris:

    def __init__(self, data):
        self.eris = {}
        for x, line in enumerate(data):
            for y, state in enumerate(line):
                self.eris[(x, y)] = state

    @property
    def biodiversity(self):
        total = 0
        for x in range(5):
            for y in range(5):
                if self.is_bug((x, y)):
                    total += 2 ** ((x*5) + y)
        return total

    def get_surrounding_bugs(self, pos):
        x, y = pos
        return {
            (i, j) for i, j in {
                (x, y-1),
                (x, y+1),
                (x-1, y),
                (x+1, y)
            } if 0 <= i < 5 and 0 <= j < 5
        }

    def get_recursive_surrounding_bugs(self, pos, depth):
        x, y = pos
        return {
            (i, j) for i, j in {
                (x, y-1),
                (x, y+1),
                (x-1, y),
                (x+1, y)
            } if 0 <= i < 5 and 0 <= j < 5
        }

    def print_eris(self):
        for x in range(5):
            line = ""
            for y in range(5):
                line += self.eris[(x, y)]
            print(line)
        print()

    def is_bug(self, pos):
        return self.eris[pos] == "#"

    def is_space(self, pos):
        return self.eris[pos] == "."


class RecursiveEris:
    def __init__(self, data):
        self.eris = {}
        for x, line in enumerate(data):
            for y, state in enumerate(line):
                self.eris[(x, y, 0)] = state

    @property
    def max_depth(self):
        return max(set(k[2] for k in self.eris))

    @property
    def min_depth(self):
        return min(set(k[2] for k in self.eris))

    @property
    def bug_count(self):
        count = 0
        for k, v in self.eris.items():
            x, y, d = k
            if (x,y) != (2,2) and v == "#":
                count += 1
        return count

    def get_surrounding_bugs(self, pos, depth):
        res = set()

        x, y = pos
        surrounding_pos = {
            (x, y-1),
            (x, y+1),
            (x-1, y),
            (x+1, y)
        }
        for spx, spy in surrounding_pos:

            if spx < 0:
                # beyond upper bound, depth decreases as we go up
                res.add(((1, 2), depth-1))
            elif spx > 4:
                # beyond lower bound, depth decreases as we go up
                res.add(((3, 2), depth-1))
            elif spy < 0:
                # beyond left bound, depth decreases as we go up
                res.add(((2, 1), depth-1))
            elif spy > 4:
                res.add(((2, 3), depth-1))
            elif spx == 2 and spy == 2:
                if pos == (1, 2):
                    res.update([((0, i), depth+1) for i in range(5)])
                elif pos == (3, 2):
                    res.update([((4, i), depth+1) for i in range(5)])
                elif pos == (2, 1):
                    res.update([((i, 0), depth+1) for i in range(5)])
                elif pos ==(2, 3):
                    res.update([((i, 4), depth+1) for i in range(5)])
            else:
                res.add(((spx, spy), depth))
        return res

    def print_eris(self):
        for d in range(self.min_depth, self.max_depth+1):
            print(f"Depth {d}")
            for x in range(5):
                line = ""
                for y in range(5):
                    if (x, y) == (2, 2):
                        line += "?"
                    else:
                        line += self.eris.get((x, y, d), ".")
                print(line)
            print()

    def is_bug(self, pos, depth):
        x, y = pos
        return self.eris.get((x,y,depth), ".")== "#"

    def is_space(self, pos, depth):
        x, y = pos
        return self.eris.get((x,y,depth), ".") == "."


def part_1(data):
    eris = Eris(data)

    layouts = set()
    while True:
        neris = {}
        for x in range(5):
            for y in range(5):
                pos = (x, y)
                num_surrounding_bugs = len([
                    sp for sp in eris.get_surrounding_bugs(pos)
                    if eris.is_bug(sp)
                ])
                if eris.is_bug(pos) and num_surrounding_bugs != 1:
                    neris[pos] = "."
                elif eris.is_space(pos) and num_surrounding_bugs in [1, 2]:
                    neris[pos] = "#"

        eris.eris.update(neris)

        # calculate biodiversity
        if eris.biodiversity in layouts:
            return eris.biodiversity
        layouts.add(eris.biodiversity)


def part_2(data, mins):
    eris = RecursiveEris(data)

    for i in range(mins):
        min_depth, max_depth = eris.min_depth, eris.max_depth

        neris = {}
        for depth in range(min_depth-1, max_depth+2):
            for x in range(5):
                for y in range(5):
                    num_surrounding_bugs = len([
                        sp for sp, d in eris.get_surrounding_bugs((x, y), depth)
                        if eris.is_bug(sp, d)
                    ])
                    if eris.is_bug((x,y), depth) and num_surrounding_bugs != 1:
                        neris[(x,y,depth)] = "."
                    elif eris.is_space((x,y), depth) and num_surrounding_bugs in [1, 2]:
                        neris[(x,y,depth)] = "#"

        eris.eris.update(neris)

    # eris.print_eris()
    return eris.bug_count


if __name__ == '__main__':
    # print(f'Part 1 {part_2(EXAMPLE, 10)}')
    print(f'Part 1 {part_1(lines)}')
    print(f'Part 2 {part_2(lines, 200)}')
