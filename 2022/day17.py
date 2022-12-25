#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
]

MAX_ROCKS = 1000000000000


class Rock:

    def __init__(self, points):
        self.points = points
        self.left_edge = min(x[0] for x in self.points)
        self.bottom_edge = min(x[1] for x in self.points)
        self.right_edge = max(x[0] for x in self.points)


ROCKS = [
    Rock([(0, 0), (1, 0), (2, 0), (3, 0)]),
    Rock([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]),
    Rock([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
    Rock([(0, 0), (0, 1), (0, 2), (0, 3)]),
    Rock([(0, 0), (1, 0), (0, 1), (1, 1)])
]


class Chamber:

    def __init__(self):
        self.rocks = set()

    @property
    def highest_rock(self):
        return (
            0 if not self.rocks else
            max(y for x, y in self.rocks)+1
        )

    def move(self, rock, direction):
        if direction == ">":
            points = [(i+1, j) for i, j in rock.points]
        elif direction == "<":
            points = [(i-1, j) for i, j in rock.points]

        if not all(0 <= x < 7 for x, y in points):
            # overlaps with walls
            return rock
        if any(set(points) & self.rocks):
            # overlaps with other rocks
            return rock

        rock.points = points
        return rock

    def drop(self, rock):
        # returns 'rested' and updated rock
        points = [(i, j-1) for i, j in rock.points]
        # import pdb; pdb.set_trace()
        if any(y < 0 for x, y in points):
            # overlaps with floor
            return True, rock
        if any(set(points) & self.rocks):
            # overlaps with other rocks
            return True, rock

        rock.points = points
        return False, rock

    def draw(self, rock=None):
        rock_points = set(rock.points if rock else [])
        all_rocks = self.rocks | rock_points

        max_height = (
            max([x[1] for x in all_rocks]) if all_rocks else 0
        ) + 4

        for j in reversed(range(max_height)):
            row = ""
            for i in range(7):
                if (i, j) in self.rocks:
                    row += "#"
                elif rock and (i, j) in set(rock.points):
                    row += "@"
                else:
                    row += "."
            print(f"|{row}|")
        print("+-------+")


def part_1(data, num_rocks):
    chamber = Chamber()

    jet_count = 0
    jet_stream = data[0]

    rock_count = 0
    while rock_count < num_rocks:
        rock = ROCKS[rock_count % len(ROCKS)]

        # determine the starting point of the rock
        # left edge: 2 units away from the left wall
        # bottom edge: 3 units above the highest rock
        rock = Rock([(i+2, j+chamber.highest_rock+3) for i, j in rock.points])

        rested = False
        while not rested:
            rock = chamber.move(rock, jet_stream[jet_count % len(jet_stream)])
            rested, rock = chamber.drop(rock)
            jet_count += 1

        # add rock to chamber.rocks
        chamber.rocks.update(rock.points)
        rock_count += 1

    return chamber.highest_rock


def part_2(data):
    chamber = Chamber()

    jet_count = 0
    jet_stream = data[0]

    move_rock_idx_map = {}

    rock_count = 0
    while True:
        r_idx = rock_count % len(ROCKS)
        j_idx = jet_count % len(jet_stream)

        if rock_count > 2022:
            if (r_idx, j_idx) not in move_rock_idx_map:
                move_rock_idx_map[(r_idx, j_idx)] = (chamber.highest_rock, rock_count)
            else:
                # find the cycle height once found
                cycle_height = chamber.highest_rock - move_rock_idx_map[(r_idx, j_idx)][0]
                cycle_rocks = rock_count - move_rock_idx_map[(r_idx, j_idx)][1]

                num_cycles = MAX_ROCKS // cycle_rocks
                return (cycle_height * num_cycles) + part_1(data, MAX_ROCKS % cycle_rocks)

        rock = ROCKS[r_idx]
        # determine the starting point of the rock
        # left edge: 2 units away from the left wall
        # bottom edge: 3 units above the highest rock
        rock = Rock([(i+2, j+chamber.highest_rock+3) for i, j in rock.points])
        # chamber.draw(rock)

        rested = False
        while not rested:
            rock = chamber.move(rock, jet_stream[jet_count % len(jet_stream)])
            rested, rock = chamber.drop(rock)
            jet_count += 1

        # add rock to chamber.rocks
        chamber.rocks.update(rock.points)
        rock_count += 1


if __name__ == '__main__':
    # print(f'EXAMPLE {part_2(EXAMPLE)}')
    print(f'Part 1 {part_1(lines, 2022)}')
    print(f'Part 2 {part_2(lines)}')
