#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    'A Y',
    'B X',
    'C Z'
]

SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

WINS = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

DRAWS = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

LOSES = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

OUTCOMES = {
    'Z': WINS,
    'Y': DRAWS,
    'X': LOSES
}


def main(data, part=None):
    total_points = 0
    for line in data:
        first, second = line.split()

        if part == 1:
            points = SCORES[second]
            if WINS[first] == second:
                points += 6
            elif DRAWS[first] == second:
                points += 3
            total_points += points
        elif part == 2:
            player = OUTCOMES[second][first]
            points = SCORES[player]
            if second == 'Z':
                points += 6
            elif second == 'Y':
                points += 3
            total_points += points

    return total_points


if __name__ == '__main__':
    # print(f'Day 1: Part 1 {main(lines, 1)}')
    # print(f'Day 1: Part 2 {main(EXAMPLE, 2)}')
    print(f'Day 1: Part 2 {main(lines, 2)}')
