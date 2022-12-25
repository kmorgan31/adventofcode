#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "1",
    "2",
    "-3",
    "3",
    "-2",
    "0",
    "4"
]


def order_by_col(lst, col=None):
    lst = sorted(lst, key=lambda x: x[col])
    print([x[2] for x in lst])


def get_ny(curr_idx, val, n):
    offset = abs(val) % (n-1)
    offset = -offset if val < 0 else offset

    ny = curr_idx + offset
    if ny >= n:
        return ny % n + 1
    elif ny == 0:
        return 0 if offset >= 0 else n
    return ny


def mix(idx_val):
    n = len(idx_val)
    for idx in range(n):
        _, curr_idx, val = sorted(idx_val, key=lambda x: x[0])[idx]
        if val == 0:
            # nothing moves for 0
            continue

        idx_val = sorted(idx_val, key=lambda x: x[1])

        # pop the item at curr_idx
        _, y, z = idx_val.pop(curr_idx)
        ny = get_ny(y, z, n)

        # insert val at the correct pos
        idx_val.insert(ny, (idx, ny, z))

        # update idx of all entries
        for x in range(n):
            ox, ix, vx = idx_val[x]
            idx_val[x] = (ox, x, vx)
    return idx_val


def main(data, part=None):

    if part == 1:
        decryption_key = 1
        mix_num = 1
    elif part == 2:
        decryption_key = 811589153
        mix_num = 10

    nums = [int(line)*decryption_key for line in data]
    idx_val = [(i, i, val) for i, val in enumerate(nums)]

    for x in range(mix_num):
        idx_val = mix(idx_val)

    total = 0
    zero_idx = [x[2] for x in idx_val].index(0)
    for i in [1000, 2000, 3000]:
        idx = (i + zero_idx) % len(nums)
        total += idx_val[idx][2]
    return total


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
