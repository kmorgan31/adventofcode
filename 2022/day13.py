#!/usr/bin/python

from aocd import lines

from itertools import zip_longest

EXAMPLE = [
    "[1,1,3,1,1]",
    "[1,1,5,1,1]",
    "",
    "[[1],[2,3,4]]",
    "[[1],4]",
    "",
    "[9]",
    "[[8,7,6]]",
    "",
    "[[4,4],4,4]",
    "[[4,4],4,4,4]",
    "",
    "[7,7,7,7]",
    "[7,7,7]",
    "",
    "[]",
    "[3]",
    "",
    "[[[]]]",
    "[[]]",
    "",
    "[1,[2,[3,[4,[5,6,7]]]],8,9]",
    "[1,[2,[3,[4,[5,6,0]]]],8,9]"
]


def compare_nones(x, y):
    if x is None and y is None:
        return None
    elif x is None:
        return True
    elif y is None:
        return False


def compare_values(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if x == y:
            return None
        else:
            return x < y
    if isinstance(x, list) and isinstance(y, list):
        for i, k in zip_longest(x, y):
            is_ordered = compare_values(i, k)
            if is_ordered is not None:
                return is_ordered
    elif isinstance(x, list) and isinstance(y, int):
        return compare_values(x, [y])
    elif isinstance(x, int) and isinstance(y, list):
        return compare_values([x], y)
    else:
        return compare_nones(x, y)


def part_1(data):
    packets = list(map(eval, filter(lambda a: a != "", data)))

    sum_idx = 0
    for idx in range(0, len(packets), 2):
        packet_1, packet_2 = packets[idx:idx+2]
        is_ordered = compare_values(packet_1, packet_2)
        if is_ordered:
            sum_idx += idx//2+1
    return sum_idx


def part_2(data):
    packets = list(map(eval, filter(lambda a: a != "", data)))

    # add divider packets
    divider_packets = [[[2]], [[6]]]
    packets.extend(divider_packets)

    # sort packets
    num_packets = len(packets)
    for i in range(num_packets):
        for j in range(0, num_packets - i - 1):
            is_ordered = compare_values(packets[j], packets[j+1])
            if not is_ordered:
                # swap packets
                packets[j], packets[j+1] = packets[j+1], packets[j]

    idx = 1
    for i, packet in enumerate(packets):
        if packet in divider_packets:
            idx *= i+1
    return idx


if __name__ == '__main__':
    # print(f'Part 1 {part_1(EXAMPLE)}')
    print(f'Part 1 {part_1(lines)}')
    print(f'Part 2 {part_2(lines)}')
