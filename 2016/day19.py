#!/usr/bin/python


from collections import deque


def part_1(num_elves):
    return int('0b' + bin(num_elves)[3:] + '1', 2)


def part_2(num_elves):
    left, right = deque(), deque()

    for i in range(1, num_elves+1):
        if i < (num_elves // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]


if __name__ == '__main__':
    # print(f'Example {part_1(5)}')
    print(f'Part 1 {part_1(3017957)}')
    print(f'Part 2 {part_2(3017957)}')
