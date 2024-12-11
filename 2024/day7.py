#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

# EXAMPLE = "292: 11 6 16 20"
EXAMPLE = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

OPS = ["+", "*", "||"]

def print_line(ans, line, ops):
    ans = f"{ans} = "
    for x in range(len(ops)):
        ans += f'{line[x]} {OPS[int(ops[x])]}'
    ans += f'{line[-1]}'
    print(ans)


def get_ops(n, part, fill):
    binary_num = ''
    while n > 0:
        remainder = n % (part+1)
        binary_num = str(remainder) + binary_num
        n = n // (part+1)
    return (binary_num if binary_num else '0').zfill(fill)


def main(input_data, part):
    count = 0
    lines = input_data.split("\n")
    for line in lines:
        ans, rem = line.split(":")
        nums = list(map(int, rem.split()))

        num_ops = len(nums)-1
        for x in range((part+1)**num_ops):
            total = nums[0]
            ops = get_ops(x, part, num_ops)
            for y in range(len(ops)):
                if ops[y] == "0":
                    # '+'
                    total += nums[y+1]
                elif ops[y] == "1":
                    # "*"
                    total *= nums[y+1]
                elif ops[y] == "2":
                    new_total = f"{total}{nums[y+1]}"
                    total = int(new_total)

            # import pdb; pdb.set_trace()
            if total == int(ans):
                print_line(ans, nums, ops)
                count += int(ans)
                break
    return count


if __name__ == '__main__':
    # print(f'Part 1 {part_1(EXAMPLE)}')
    # print(f'Part 1 {part_1(data)}')
    # print(f'Part 2 {main(EXAMPLE, 2)}')
    print(f'Part 2 {main(data, 2)}')
