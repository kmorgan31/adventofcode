#!/usr/bin/python

from aocd import lines

from itertools import permutations

EXAMPLE = [
    "Alice would gain 54 happiness units by sitting next to Bob.",
    "Alice would lose 79 happiness units by sitting next to Carol.",
    "Alice would lose 2 happiness units by sitting next to David.",
    "Bob would gain 83 happiness units by sitting next to Alice.",
    "Bob would lose 7 happiness units by sitting next to Carol.",
    "Bob would lose 63 happiness units by sitting next to David.",
    "Carol would lose 62 happiness units by sitting next to Alice.",
    "Carol would gain 60 happiness units by sitting next to Bob.",
    "Carol would gain 55 happiness units by sitting next to David.",
    "David would gain 46 happiness units by sitting next to Alice.",
    "David would lose 7 happiness units by sitting next to Bob.",
    "David would gain 41 happiness units by sitting next to Carol.",
]


def main(data, part=None):
    happiness_dct = {}
    guests = set()

    for line in data:
        line = line.split()
        g1, g2 = line[0], line[-1][:-1]

        guests.add(g1)
        happiness = int(line[3]) if line[2] == "gain" else -int(line[3])
        happiness_dct[(g1, g2)] = happiness

    if part == 2:
        # add Me to dct
        for g in guests:
            happiness_dct[("Me", g)] = 0
            happiness_dct[(g, "Me")] = 0
        guests.add("Me")

    max_happiness = 0
    for ordering in permutations(guests):
        # first guest added to the end since its a circular table
        ordering = list(ordering)
        ordering.append(ordering[0])

        happiness = 0
        for i in range(len(ordering)-1):
            happiness += (
                happiness_dct[(ordering[i], ordering[i+1])] +
                happiness_dct[(ordering[i+1], ordering[i])]
            )

        max_happiness = max(max_happiness, happiness)
    return max_happiness


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
