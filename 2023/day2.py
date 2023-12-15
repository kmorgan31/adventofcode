#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5fc4d1838d6c26850845cb7f79b05413c2b6943f5e387aad806bbd2298cce594f8f0cd7053b0191c213323b1295f5491f6b5295c984461a77a

from aocd import lines

import re

EXAMPLE = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    # "Game 1: 1 blue, 8 green; 14 green, 15 blue; 3 green, 9 blue; 8 green, 8 blue, 1 red; 1 red, 9 green, 10 blue"
]

R = 12
G = 13
B = 14


def determine_pull_color_amounts(pull):
    dct = {'red': 0, 'green': 0, 'blue': 0}

    colors = pull.split()
    for x in range(0, len(colors)-1, 2):
        color = re.sub(r"[^a-z0-9]", '', colors[x+1])
        dct[color] = int(colors[x])
    return dct


def part_1(data):
    total = 0
    for i, line in enumerate(data):
        valid = True

        pulls = line.split(':')[1].lstrip().split(";")
        for pull in pulls:
            pdct = determine_pull_color_amounts(pull)

            if pdct['red'] > R or pdct['blue'] > B or pdct['green'] > G:
                valid = False
                break

        if valid:
            total += i + 1

    return total


def part_2(data):
    sum_power = 0
    for line in data:
        game = {'red': 0, 'green': 0, 'blue': 0}

        pulls = line.split(':')[1].lstrip().split(";")
        for pull in pulls:
            pdct = determine_pull_color_amounts(pull)

            game['red'] = max(game['red'], pdct['red'])
            game['green'] = max(game['green'], pdct['green'])
            game['blue'] = max(game['blue'], pdct['blue'])

        sum_power += game['red'] * game['green'] * game['blue']
    return sum_power


if __name__ == '__main__':
    # print(f'Day 2: Part 1 {part_1(lines)}')
    # print(f'Day 1: Part 1 {main(lines, 1)}')
    print(f'Day 2: Part 2 {part_2(lines)}')
    # print(f'Day 1: Part 2 {main(lines, 2)}')
