#!/usr/bin/python

from aocd import lines


def calculate_fuel(mass):
    return (int(mass)//3)-2


def main(data, part=None):
    total = 0
    for line in data:
        fuel = calculate_fuel(int(line))
        if part == 1:
            total += fuel
        if part == 2:
            while fuel > 0:
                total += fuel
                fuel = calculate_fuel(fuel)

    return total


if __name__ == '__main__':
    # print(f'EXAMPLE {main([1969], 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
