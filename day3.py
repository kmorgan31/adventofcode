#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

values = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def part_1(data):
    total = 0

    for line in data:
        mid = (len(line)//2)
        first, second = set(line[:mid]), set(line[mid:])
        common = first & second

        letter = common.pop()
        value = values.index(letter)+1
        total += value

    return total


def part_2(data):
    total = 0

    chunk = 0
    while chunk < len(data):
        group = data[chunk:chunk+3]

        common = set(group[0]) & set(group[1]) & set(group[2])
        letter = common.pop()
        value = values.index(letter)+1
        total += value

        chunk += 3
    return total


if __name__ == '__main__':
    print(f'Day 1: Part 1 {part_1(lines)}')
    # print(f'Day 1: Part 2 {main(EXAMPLE, 1)}')
    print(f'Day 1: Part 2 {part_2(lines)}')
