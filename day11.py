#!/usr/bin/python

from aocd import lines


test_data = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526'
]

BOARD_SIZE = 10
NUM_STEPS = 100


def parse_octopi_map(data):
    return [[m for m in map(int, list(line))] for line in data]


def get_surrounding_octopi(octopus):
    x, y = octopus
    get_surrounding_octopi = [
        (x-1, y-1),     # top left
        (x-1, y),       # left
        (x-1, y+1),     # bottom left
        (x, y-1),       # up
        (x, y+1),       # down
        (x+1, y-1),     # top right
        (x+1, y),       # right
        (x+1, y+1),     # bottom right
    ]
    return [
        (i, j) for i, j in get_surrounding_octopi
        if 0 <= i <= BOARD_SIZE-1 and 0 <= j <= BOARD_SIZE-1
    ]


def increase_all_octopi_energy_level(data):
    # increases all octopi by 1
    return [
        [int(data[y][x]) + 1 for x in range(BOARD_SIZE)]
        for y in range(BOARD_SIZE)
    ]


def determine_octopi_about_to_flash(data):
    # return list of octopi with level > 9 (about to flash)
    flash_points = []
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if int(data[x][y]) > 9:
                flash_points.append((x, y))
    return flash_points


def flash(octopi_map, curr_octopus, surrounding_points):
    # increased surrounding flashed points by 1
    # return any points that are going to flash
    to_flash = []
    for x, y in surrounding_points:
        if octopi_map[x][y] == 0:
            # recently reset, skip
            continue

        octopi_map[x][y] += 1
        if octopi_map[x][y] > 9:
            to_flash.append((x, y))

    # curr octopus loses all energy after flashing
    octopi_map[curr_octopus[0]][curr_octopus[1]] = 0

    return octopi_map, to_flash


def octopi_step(octopi_map):
    # returns total number of flashes in a step
    octopi_map = increase_all_octopi_energy_level(octopi_map)

    flashed = set()
    octopi_to_flash = determine_octopi_about_to_flash(octopi_map)
    while octopi_to_flash:
        curr_octopus = octopi_to_flash.pop(0)  # BFS
        if curr_octopus in flashed:
            continue

        # flash current octopi, get surrounding octopi
        octopi_map, new_octopi_to_flash = flash(
            octopi_map, curr_octopus, get_surrounding_octopi(curr_octopus)
        )

        # add new octopi to octopi_to_flash
        octopi_to_flash += new_octopi_to_flash

        # curr_octopus flashed
        flashed.add(curr_octopus)

    return len(flashed), octopi_map


def main(data, part):

    octopi_map = parse_octopi_map(data)

    count = 0
    flash_count = 0

    while True:
        count += 1
        num_flash, octopi_map = octopi_step(octopi_map)
        flash_count += num_flash

        if part == 1 and count == 100:
            return flash_count
        elif part == 2 and num_flash == 100:
            return count


if __name__ == '__main__':

    # test
    print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 11: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
