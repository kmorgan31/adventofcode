#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "deal into new stack",
    "cut -2",
    "deal with increment 7",
    "cut 8",
    "cut -4",
    "deal with increment 7",
    "cut 3",
    "deal with increment 9",
    "deal with increment 3",
    "cut -1",
]


def part_1(data, num_cards):

    deck = list(range(num_cards))

    for line in data:
        line = line.split()
        if line[0] == "deal":
            if line[-1].isdigit():
                # deal with increment x
                x = int(line[-1])
                ndeck = ["." for i in range(len(deck))]
                for i, j in enumerate(deck):
                    ndeck[(i*x) % len(deck)] = j
                deck = ndeck
            else:
                # deal into new stack
                # reverse deck
                deck = deck[::-1]

        elif line[0] == "cut":
            # cut x cards
            x = int(line[-1])
            deck = deck[x:] + deck[:x]

    return deck.index(2019)


def part_2(data):
    """ Modular Arithmetic"""
    L = 119315717514047
    N = 101741582076661
    P = 2020

    a, b = 1, 0
    for line in data:
        line = line.split()
        if line[0] == "deal":
            if line[-1].isdigit():
                # deal with increment x
                x = int(line[-1])
                a = a * x % L
                b = b * x % L
            else:
                # deal into new stack
                a = -a % L
                b = (L - 1 - b) % L

        elif line[0] == "cut":
            # cut x cards
            x = int(line[-1])
            b = (b - x) % L

    r = (b * pow(1-a, L-2, L)) % L

    return ((P - r) * pow(a, N*(L-2), L) + r) % L


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, 10)}')
    print(f'Part 1 {part_1(lines, 10007)}')
    print(f'Part 2 {part_2(lines)}')
