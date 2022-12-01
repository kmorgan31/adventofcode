#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    '1000',
    '2000',
    '3000',
    '',
    '4000',
    '',
    '5000',
    '6000',
    '',
    '7000',
    '8000',
    '9000',
    '',
    '10000'
]


def main(data, part=None):
    elf_calories = []
    current_calories = 0

    for line in data:
        if line:
            current_calories += int(line)
        else:
            elf_calories.append(current_calories)
            current_calories = 0
    elf_calories.append(current_calories)

    if part == 1:
        return sorted(elf_calories, reverse=True)[0]
    elif part == 2:
        return sum(sorted(elf_calories, reverse=True)[:3])


if __name__ == '__main__':
    # print(f'Day 1: Part 1 {main(lines, 1)}')
    # print(f'Day 1: Part 2 {main(EXAMPLE, 2)}')
    print(f'Day 1: Part 2 {main(lines, 2)}')
