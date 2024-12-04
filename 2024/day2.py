#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data


EXAMPLE = [
    '7 6 4 2 1',
    '1 2 7 8 9',
    '9 7 6 2 1',
    '1 3 2 4 5',
    '8 6 4 4 1',
    '1 3 6 7 9'
]


def reports():
    return data.split('\n')

def differences(levels):
    return set([(int(levels[i]) - int(levels[i+1])) for i in range(len(levels)-1)])

def is_safe(levels):
    return len(differences(levels).difference({1, 2, 3})) == 0 or len(differences(levels).difference({-1, -2, -3})) == 0

def is_skip_safe(levels):
    for idx in range(len(levels)):
        safe = is_safe(levels[:idx] + levels[idx+1:])
        if safe:
            return True

    return False


def main(input_data, part=None):
    safe_count = 0

    for line in input_data:
        levels = list(map(int, line.split()))

        safe = is_safe(levels)
        if part == 2 and safe == False:
            safe = is_skip_safe(levels)

        if safe == True:
            safe_count += 1
            
    return safe_count


if __name__ == '__main__':
    print(f'Day 1: Part 1 {main(EXAMPLE, 1)}')
    print(f'Day 1: Part 1 {main(reports(), 1)}')
    print(f'Day 1: Part 2 {main(EXAMPLE, 2)}')
    print(f'Day 1: Part 2 {main(reports(), 2)}')
