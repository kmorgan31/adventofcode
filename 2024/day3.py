#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data
import re


EXAMPLE = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

EXAMPLE_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def main(input_data, part=None):
    total = 0

    if part == 1:
        matches_re = re.compile(r'mul\((-?\d+),\s*(-?\d+)\)')

        matches = matches_re.findall(input_data)
        for num1, num2 in matches:
            total += int(num1) * int(num2)
    elif part == 2:
        
        matches_re = re.compile(r"mul\((-?\d+),\s*(-?\d+)\)|do\(\)|don't\(\)")

        matches = matches_re.finditer(input_data)
        for match in matches:
            if match.group() == "do()":
                include = True
            elif match.group() == "don't()":
                include = False
            else:
                num1, num2 = match.groups()
                total += int(num1) * int(num2)
        
    return total


if __name__ == '__main__':
    print(f'Day 3: Part 1 {main(EXAMPLE, 1)}')
    print(f'Day 3: Part 1 {main(data, 1)}')
    print(f'Day 3: Part 2 {main(EXAMPLE_2, 2)}')
    print(f'Day 3: Part 2 {main(data, 2)}')
