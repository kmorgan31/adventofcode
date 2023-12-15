#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5fc4d1838d6c26850845cb7f79b05413c2b6943f5e387aad806bbd2298cce594f8f0cd7053b0191c213323b1295f5491f6b5295c984461a77a

from aocd import lines

import re

EXAMPLE_1 = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet'
]

EXAMPLE_2 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]

NUMBERS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def word_to_num(x):
    return NUMBERS[x] if x in NUMBERS else x


def main(data, part=None):
    total = 0
    for line in data:
        if part == 1:
            nums_re = re.compile(r'\d')
        if part == 2:
            nums_re = re.compile(r'(?=(\d|%s))' % 'one|two|three|four|five|six|seven|eight|nine')

        nums = nums_re.findall(line)
        total += int(word_to_num(nums[0]) + word_to_num(nums[-1]))
    return total


if __name__ == '__main__':
    print(f'Day 1: Part 1 {main(EXAMPLE_1, 1)}')
    print(f'Day 1: Part 1 {main(lines, 1)}')
    print(f'Day 1: Part 2 {main(EXAMPLE_2, 2)}')
    print(f'Day 1: Part 2 {main(lines, 2)}')
