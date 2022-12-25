#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b"
]


def get_score(group, part):
    if part == 1:
        return len(set.union(*group))
    elif part == 2:
        return len(set.intersection(*group))


def main(data, part=None):
    total = 0

    group = []
    for line in data:
        if not line:
            total += get_score(group, part)

            # reset group
            group = []
            continue

        group.append(set(line))

    if group:
        total += get_score(group, part)

    return total


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
