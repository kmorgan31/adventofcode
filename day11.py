#!/usr/bin/python

import math


class Monkey:

    def __init__(self, items, operation, divisor, if_true, if_false):
        self.items = items
        self.num_inspections = 0
        self.operation = operation
        self.divisor = divisor
        self.if_true = if_true
        self.if_false = if_false


EXAMPLE = [
    Monkey(
        items=[79, 98],
        operation=lambda old: old * 19,
        divisor=23,
        if_true=2,
        if_false=3
    ),
    Monkey(
        items=[54, 65, 75, 74],
        operation=lambda old: old + 6,
        divisor=19,
        if_true=2,
        if_false=0
    ),
    Monkey(
        items=[79, 60, 97],
        operation=lambda old: old * old,
        divisor=13,
        if_true=1,
        if_false=3
    ),
    Monkey(
        items=[74],
        operation=lambda old: old + 3,
        divisor=17,
        if_true=0,
        if_false=1
    ),

]


MONKEYS = [
    Monkey(
        items=[66, 79],
        operation=lambda old: old * 11,
        divisor=7,
        if_true=6,
        if_false=7
    ),
    Monkey(
        items=[84, 94, 94, 81, 98, 75],
        operation=lambda old: old * 17,
        divisor=13,
        if_true=5,
        if_false=2
    ),
    Monkey(
        items=[85, 79, 59, 64, 79, 95, 67],
        operation=lambda old: old + 8,
        divisor=5,
        if_true=4,
        if_false=5
    ),
    Monkey(
        items=[70],
        operation=lambda old: old + 3,
        divisor=19,
        if_true=6,
        if_false=0
    ),
    Monkey(
        items=[57, 69, 78, 78],
        operation=lambda old: old + 4,
        divisor=2,
        if_true=0,
        if_false=3
    ),
    Monkey(
        items=[65, 92, 60, 74, 72],
        operation=lambda old: old + 7,
        divisor=11,
        if_true=3,
        if_false=4
    ),
    Monkey(
        items=[77, 91, 91],
        operation=lambda old: old * old,
        divisor=17,
        if_true=1,
        if_false=7
    ),
    Monkey(
        items=[76, 58, 57, 55, 67, 77, 54, 99],
        operation=lambda old: old + 6,
        divisor=3,
        if_true=2,
        if_false=1
    )
]


def main(monkeys, rounds, worry_divisor=3):

    lcm = math.prod([m.divisor for m in monkeys])

    for round in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                monkey.num_inspections += 1

                item = monkey.items.pop(0)
                worry = monkey.operation(item)

                # monkey gets bored. worry decreases
                worry = worry // worry_divisor

                # reduce worry by LCM of monkey test divisors
                worry = worry % lcm

                monkey_id = (
                    monkey.if_true if worry % monkey.divisor == 0
                    else monkey.if_false
                )
                monkeys[monkey_id].items.append(worry)

    num_inspections = sorted([m.num_inspections for m in monkeys], reverse=True)
    return num_inspections[0] * num_inspections[1]


if __name__ == '__main__':
    # print(f'Example: Part 1 {main(EXAMPLE, 20)}')
    # print(f'Example: Part 2 {main(EXAMPLE, 10000, worry_divisor=1)}')
    # print(f'Part 1 {main(MONKEYS, 20)}')
    print(f'Part 2 {main(MONKEYS, 10000, worry_divisor=1)}')
