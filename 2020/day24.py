#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "sesenwnenenewseeswwswswwnenewsewsw",
    "neeenesenwnwwswnenewnwwsewnenwseswesw",
    "seswneswswsenwwnwse",
    "nwnwneseeswswnenewneswwnewseswneseene",
    "swweswneswnenwsewnwneneseenw",
    "eesenwseswswnenwswnwnwsewwnwsene",
    "sewnenenenesenwsewnenwwwse",
    "wenwwweseeeweswwwnwwe",
    "wsweesenenewnwwnwsenewsenwwsesesenwne",
    "neeswseenwwswnwswswnw",
    "nenwswwsewswnenenewsenwsenwnesesenew",
    "enewnwewneswsewnwswenweswnenwsenwsw",
    "sweneswneswneneenwnewenewwneswswnese",
    "swwesenesewenwneswnwwneseswwne",
    "enesenwswwswneneswsenwnewswseenwsese",
    "wnwnesenesenenwwnenwsewesewsesesew",
    "nenewswnwewswnenesenwnesewesw",
    "eneswnwswnwsenenwnwnwwseeswneewsenese",
    "neswnwewnwnwseenwseesewsenwsweewe",
    "wseweeenwnesenwwwswnew"
]


def get_num_surrounding_tiles(tile, black):
    x, y = tile
    return {
        (x, y+2),       # e
        (x-1, y+1),     # ne
        (x+1, y+1),     # se
        (x, y-2),       # w
        (x-1, y-1),     # nw
        (x+1, y-1)      # sw
    } & black


def part_1(data, black):
    for line in data:

        x, y = 0, 0
        while line:
            if line[0] == "e":
                line = line[1:]
                y += 2
            elif line[0] == "w":
                line = line[1:]
                y -= 2
            elif line[0:2] == "ne":
                line = line[2:]
                x -= 1; y += 1
            elif line[0:2] == "nw":
                line = line[2:]
                x -= 1; y -= 1
            elif line[0:2] == "se":
                line = line[2:]
                x += 1; y += 1
            elif line[0:2] == "sw":
                line = line[2:]
                x += 1; y -= 1

        method = "remove" if (x, y) in black else "add"
        getattr(black, method)((x, y))

    return black


def part_2(day, black):
    new_black = set()

    xvals = [x for x, y in black]
    yvals = [y for x, y in black]

    for x in range(min(xvals)-1, max(xvals)+2):
        for y in range(min(yvals)-1, max(yvals)+2):
            surrounding_black = get_num_surrounding_tiles((x,y), black)

            if (x, y) in black and not(
                len(surrounding_black) == 0 or len(surrounding_black) > 2
            ):
                new_black.add((x, y))
            elif (x, y) not in black and len(surrounding_black) == 2:
                new_black.add((x, y))

    return new_black


def main(data, part=None):
    black = part_1(data, set())

    if part == 2:
        for day in range(100):
            black = part_2(day, black)

    return len(black)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
