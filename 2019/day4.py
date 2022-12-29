#!/usr/bin/python

from collections import Counter


INPUT = [136818, 685979]


def main(data, part=None):
    total = 0
    for i in range(data[0], data[1]+1):
        num = str(i)
        counter = Counter(num)
        if any(num[j] > num[j+1] for j in range(5)):
            continue
        if (
            part == 1 and any(x >= 2 for x in counter.values()) or
            part == 2 and any(x == 2 for x in counter.values())
        ):
            total += 1
    return total


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(INPUT, 1)}')
    print(f'Part 2 {main(INPUT, 2)}')
