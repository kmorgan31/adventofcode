#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "cpy 41 a",
    "inc a",
    "inc a",
    "dec a",
    "jnz a 2",
    "dec a",
]


def main(data, part=None):
    registers = {x: 0 for x in ["a", "b", "c", "d"]}

    if part == 2:
        registers["c"] = 1

    i = 0
    while i < len(data):
        line = data[i].split()
        action, nums = line[0], line[1:]

        if action == "cpy":
            val = int(nums[0]) if nums[0].isdigit() else registers[nums[0]]
            registers[nums[1]] = val
        if action == "inc":
            registers[nums[0]] += 1
        if action == "dec":
            registers[nums[0]] -= 1
        if action == "jnz":
            val = int(nums[0]) if nums[0].isdigit() else registers[nums[0]]
            if val != 0:
                i += int(nums[1])
                continue
        i += 1
    return registers['a']


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    # print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
