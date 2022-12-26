#!/usr/bin/python

from aocd import lines

from math import prod
from collections import defaultdict


EXAMPLE = [
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50",
    "",
    "your ticket:",
    "7,1,14",
    "",
    "nearby tickets:",
    "7,3,47",
    "40,4,50",
    "55,2,20",
    "38,6,12"
]

EXAMPLE_2 = [
    "class: 0-1 or 4-19",
    "row: 0-5 or 8-19",
    "seat: 0-13 or 16-19",
    "",
    "your ticket:",
    "11,12,13",
    "",
    "nearby tickets:",
    "3,9,18",
    "15,1,5",
    "5,14,9"
]


def parse_input(data):
    group = 0

    rules = {}
    tickets = []
    for line in data:
        if not line:
            group += 1
            continue

        if group == 0:
            # parse conditions
            line = line.split(":")
            key = line[0]
            r = [
                (int(x), int(y))
                for x,y in map(lambda x: x.split("-"), line[1].split(" or "))
            ]
            rules[key] = r
        elif group == 1:
            # parse my ticket
            if "your ticket" in line:
                continue
            ticket = list(map(int, line.split(",")))
        elif group == 2:
            # parse other tickets
            if "nearby tickets" in line:
                continue
            tickets.append(list(map(int, line.split(","))))
    return rules, ticket, tickets


def get_valid_numbers(rules):
    valid_nums = set()
    for r in rules.values():
        valid_nums.update(*[set(range(x, y+1)) for x, y in r])
    return valid_nums


def main(data, part=None):
    rules, ticket, tickets = parse_input(data)

    # get numbers that fall within the ranges
    valid_numbers = get_valid_numbers(rules)

    total = 0
    valid_tickets = []
    for t in tickets:
        invalid_numbers = set(t) - valid_numbers
        if invalid_numbers:
            total += sum(invalid_numbers)
        else:
            valid_tickets.append(t)

    if part == 1:
        return total

    elif part == 2:
        fields = defaultdict(set)
        for i in range(len(ticket)):
            ticket_nums = [t[i] for t in valid_tickets]

            for k, r in rules.items():
                valid_numbers = get_valid_numbers({k: r})
                if len(set(ticket_nums) - valid_numbers) == 0:
                    fields[k].add(i)

        cols_used = set()
        rule_idx_map = {}

        sorted_rules = sorted(fields.keys(), key=lambda x: len(fields[x]))
        while sorted_rules:
            rule = sorted_rules.pop(0)
            if len(fields[rule]) == 1:
                # found only possibility
                col = fields[rule].pop()
                rule_idx_map[rule] = col
                cols_used.add(col)

                # remove from fields
                del fields[rule]
            else:
                # clean up the possible indexes for rule
                fields[rule] = fields[rule] - cols_used
                sorted_rules = sorted(fields.keys(), key=lambda x: len(fields[x]))

        return prod(
            ticket[i] for k, i in rule_idx_map.items() if "departure" in k
        )


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE_2, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
