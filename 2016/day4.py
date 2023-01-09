#!/usr/bin/python

from aocd import lines

from collections import Counter, defaultdict

EXAMPLE = [
    "aaaaa-bbb-z-y-x-123[abxyz]",
    "a-b-c-d-e-f-g-h-987[abcde]",
    "not-a-real-room-404[oarel]",
    "totally-real-room-200[decoy]"
]

ALPHABET = list('abcdefghijklmnopqrstuvwxyz')


def part_1(data):
    total = 0
    for line in data:
        line = line.split('-')
        sector_id, checksum = line[-1].split('[')
        checksum = checksum.replace(']', '')

        counter = Counter()
        for i in line[:-1]:
            for j in i:
                counter[j] += 1

        counter_reverse = defaultdict(list)
        for x, y in counter.most_common():
            counter_reverse[y] += x

        top_five = []
        most_common = sorted(counter_reverse.keys(), reverse=True)[:5]
        for mc in most_common:
            while len(counter_reverse[mc]) > 0 and len(top_five) < 5:
                i = sorted(counter_reverse[mc])[0]
                counter_reverse[mc].remove(i)
                top_five.append(i)

        if top_five == list(checksum):
            total += int(sector_id)
    return total


def part_2(data):
    for line in data:
        line = line.split('-')
        sector_id, _ = line[-1].split('[')

        name = []
        for i in line[:-1]:
            word = ""
            for j in i:
                word += ALPHABET[(ALPHABET.index(j) + int(sector_id)) % len(ALPHABET)]
            name.append(word)

        if ' '.join(name) == "northpole object storage":
            return sector_id


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 1)}')
    print(f'Part 1 {part_1(lines)}')
    print(f'Part 2 {part_2(lines)}')
