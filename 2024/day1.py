#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

from collections import Counter


EXAMPLE = [
    [3, 4, 2, 1, 3, 3],
    [4, 3, 5, 3, 9, 3]
]

def lines():
    return data.split('\n')


def get_lists():
    left, right = [], []
    for line in lines():
        num1, num2 = line.split()
        left.append(int(num1))
        right.append(int(num2))
    return [left, right]


def main(input_data, part=None):
    total = 0

    left, right = [sorted(x) for x in input_data]

    if part == 1:
        for i in range(len(left)):
            total += abs(left[i] - right[i])
    elif part == 2:
        counted_right = Counter(right)
        for i in range(len(left)):
            total += left[i] * counted_right[left[i]]
    
    return total


if __name__ == '__main__':
    # print(f'Day 1: Part 1 {main(EXAMPLE, 1)}')
    # print(f'Day 1: Part 1 {main(get_lists(), 1)}')
    print(f'Day 1: Part 2 {main(EXAMPLE, 2)}')
    print(f'Day 1: Part 2 {main(get_lists(), 2)}')
