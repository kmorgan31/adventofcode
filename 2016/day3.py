#!/usr/bin/python

from aocd import lines


def is_triangle(n1, n2, n3):
    return n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1


def get_nums(data):
    nums1, nums2, nums3 = [], [], []
    for line in data:
        n1, n2, n3 = list(map(int, line.split()))
        nums1.append(n1)
        nums2.append(n2)
        nums3.append(n3)
    return nums1 + nums2 + nums3


def main(data, part=None):
    count = 0
    if part == 1:
        for line in data:
            nums = list(map(int, line.split()))
            if is_triangle(*nums):
                count += 1

    elif part == 2:
        nums = get_nums(data)

        i = 0
        while i < len(nums):
            if is_triangle(*nums[i:i+3]):
                count += 1
            i += 3

    return count


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
