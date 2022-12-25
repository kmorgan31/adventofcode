#!/usr/bin/python

from aocd import lines

from collections import defaultdict, deque


EXAMPLE = [
    "..............",
    "..............",
    ".......#......",
    ".....###.#....",
    "...#...#.#....",
    "....#...##....",
    "...#.###......",
    "...##.#.##....",
    "....#..#......",
    "..............",
    "..............",
    ".............."
]


def parse_input(data):
    elves = set()
    for i in range(len(data)):
        line = list(data[i])
        for j in range(len(line)):
            if line[j] == "#":
                elves.add((i, j))
    return elves


def get_surrounding_elves(elf):
    x, y = elf
    return {
        (x-1, y-1),     # top left
        (x-1, y),       # left
        (x-1, y+1),     # bottom left
        (x, y-1),       # up
        (x, y+1),       # down
        (x+1, y-1),     # top right
        (x+1, y),       # right
        (x+1, y+1),     # bottom right
    }


def draw_elves(elves, elf=None):
    xlst = sorted(elves, key=lambda elf: elf[0])
    ylst = sorted(elves, key=lambda elf: elf[1])
    xmin, xmax = xlst[0][0], xlst[-1][0]
    ymin, ymax = ylst[0][1], ylst[-1][1]

    for x in range(xmin, xmax+1):
        line = ""
        for y in range(ymin, ymax+1):
            if (x, y) in elves:
                line += "@" if (x, y) == elf else "#"
            else:
                line += "."
        print(line)
    print()


def evaluate_elves(elves):
    xlst = sorted(elves, key=lambda elf: elf[0])
    ylst = sorted(elves, key=lambda elf: elf[1])
    xmin, xmax = xlst[0][0], xlst[-1][0]
    ymin, ymax = ylst[0][1], ylst[-1][1]

    area = abs(xmax - xmin+1) * abs(ymax - ymin+1)
    return area - len(elves)


def main(data, rounds):

    elves = parse_input(data)
    dir_q = deque(["N", "S", "W", "E"])

    round = 0
    while round < rounds:
        n_elves = set()
        moves = defaultdict(list)

        for elf in elves:
            x, y = elf
            surrounding_elves = get_surrounding_elves(elf)
            if not surrounding_elves.intersection(elves):
                # elf doesn't move
                moves[elf].append(elf)
                continue

            n_elf = None
            for dir in dir_q:
                if dir == "N" and not set(
                    [(i, j) for i, j in surrounding_elves if i < x]
                ).intersection(elves):
                    # no elves in the north
                    n_elf = (x-1, y)
                    break
                if dir == "S" and not set(
                    [(i, j) for i, j in surrounding_elves if i > x]
                ).intersection(elves):
                    # no elves in the south
                    n_elf = (x+1, y)
                    break
                if dir == "W" and not set(
                    [(i, j) for i, j in surrounding_elves if j < y]
                ).intersection(elves):
                    # no elves in the west
                    n_elf = (x, y-1)
                    break
                if dir == "E" and not set(
                    [(i, j) for i, j in surrounding_elves if j > y]
                ).intersection(elves):
                    # no elves in the east
                    n_elf = (x, y+1)
                    break

            if not n_elf:
                # elf cannot move
                moves[elf].append(elf)
            else:
                # elf proposed new position
                moves[n_elf].append(elf)

        for k, lst in moves.items():
            if len(lst) == 1:
                # elf moves into position (k)
                n_elves.add(k)
            else:
                # more than 1 elf wanted to go into position: neither move
                n_elves.update(lst)

        if n_elves == elves:
            print(f"No elf moved at round {round+1}")
            return evaluate_elves(elves)

        # rotate direction order
        elves = n_elves
        round += 1
        dir_q.rotate(-1)

    return evaluate_elves(elves)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 10)}')
    print(f'Part 1 {main(lines, 10)}')
    # print(f'Part 2 {main(lines, 9999)}')
