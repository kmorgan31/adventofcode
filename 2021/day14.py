#!/usr/bin/python

from aocd import lines
from collections import defaultdict, Counter

test_data = [
    'NNCB',
    '',
    'CH -> B',
    'HH -> N',
    'CB -> H',
    'NH -> C',
    'HB -> C',
    'HC -> B',
    'HN -> C',
    'NN -> C',
    'BH -> H',
    'NC -> B',
    'NB -> B',
    'BN -> B',
    'BB -> N',
    'BC -> B',
    'CC -> N',
    'CN -> C'
]


def parse_input(data):
    inserts = {}
    template = data[0]

    for line in data[2:]:
        x, y = line.split(' -> ')
        inserts[x] = y

    return template, inserts


def main(data, part):
    if part == 1:
        num_steps = 10
    elif part == 2:
        num_steps = 40

    template, inserts = parse_input(data)

    # create dict of pairs from template
    pairs = defaultdict(int)
    for x in range(len(template)-1):
        pairs[template[x:x+2]] += 1

    for x in range(num_steps):
        new_pairs = defaultdict(int)
        for pair in pairs:
            new_let = inserts[pair]

            # add pairs with new_let to new_pairs
            new_pairs[pair[0]+new_let] += pairs[pair]
            new_pairs[new_let+pair[1]] += pairs[pair]

        # update pairs with new_pairs
        pairs = new_pairs.copy()

    # count letters in pairs
    letter_count = defaultdict(int)
    for k, v in pairs.items():
        letter_count[k[0]] += v
        letter_count[k[1]] += v

    # since new_let is doubled on each entry, we have to divide by 2
    # increase the first and last letter by 1, so we can divide by 2
    letter_count[template[0]] += 1
    letter_count[template[-1]] += 1

    letters = Counter(letter_count).most_common()
    return (letters[0][1] - letters[-1][1])/2


if __name__ == '__main__':

    # test
    print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 13: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
