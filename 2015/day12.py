#!/usr/bin/python

from aocd import lines

import json


def is_number(num):
    try:
        return int(num)
    except:
        pass


def get_sum_list(lst, part=None):
    total = 0
    for x in lst:
        if isinstance(x, dict):
            total += get_sum_dict(x, part=part)
        elif isinstance(x, list):
            total += get_sum_list(x, part=part)
        elif is_number(x):
            total += int(x)
    return total


def get_sum_dict(dct, part=None):
    total = 0

    if part == 2 and "red" in dct.values():
        return 0

    for k, v in dct.items():
        if isinstance(v, dict):
            total += get_sum_dict(v, part=part)
        elif isinstance(v, list):
            total += get_sum_list(v, part=part)
        elif is_number(v):
            total += int(v)
    return total


def main(data, part=None):
    return get_sum_dict(json.loads(data), part)


if __name__ == '__main__':
    print(f'Part 1 {main(lines[0], 1)}')
    print(f'Part 2 {main(lines[0], 2)}')
