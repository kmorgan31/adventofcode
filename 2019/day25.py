#!/usr/bin/python

from aocd import lines

import re
from itertools import combinations

from intcode import Intcode


instructions = [
    "south",
    "take astronaut ice cream",
    "north",
    "east",
    "north",
    "take spool of cat6",
    "north",
    "take hypercube",
    "east",
    "take sand",
    "south",
    "take antenna",
    "north",
    "west",
    "south",
    "south",
    "take mouse",
    "south",
    "take mutex",
    "west",
    "take boulder",
    "south",
    "south",
    "south",
    "west",
    "south",
]

inventory = [
    "astronaut ice cream",
    "spool of cat6",
    "hypercube",
    "sand",
    "antenna",
    "mouse",
    "mutex",
    "boulder"
]


def check_inventory(intcode):
    intcode.give_ascii_input("inv")
    intcode.run_instructions()
    return '\n'.join(intcode.parse_ascii_output())


def try_lock(intcode):
    intcode.give_ascii_input("south")
    intcode.run_instructions()
    return '\n'.join(intcode.parse_ascii_output())


def drop_items(intcode, items):
    for item in items:
        intcode.give_ascii_input(f"drop {item}")
        intcode.run_instructions()


def take_items(intcode, items):
    for item in items:
        intcode.give_ascii_input(f"take {item}")
        intcode.run_instructions()


def main(data, part=None):
    intcode = Intcode(list(map(int, data.split(","))))

    intcode.run_instructions()
    while intcode.waiting and instructions:
        # give input
        intcode.give_ascii_input(instructions.pop(0))
        intcode.run_instructions()

    # try combinations of items
    prev_combination = inventory[:]
    for x in range(4, 8):
        for items in combinations(inventory, x):
            print(f"Trying: {items}")

            # drop items
            drop_items(intcode, prev_combination)

            # take items
            prev_combination = list(items)
            take_items(intcode, items)

            # check inventory
            check_inventory(intcode)

            # try lock
            response = try_lock(intcode)
            if "Security Checkpoint" not in response:
                return int(re.findall(r'\d+', response)[0])


if __name__ == '__main__':
    print(f'Part 1 {main(lines[0])}')
