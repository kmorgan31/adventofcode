#!/usr/bin/python


from aocd import lines

EXAMPLE = [
    "5-8",
    "0-2",
    "4-7"
]


def is_valid(ip, blacklists):
    for x, y in blacklists:
        if x <= ip <= y:
            break
    else:
        if ip < 2**32:
            return True
    return False


def main(data, part=None):

    blacklists = sorted([
        tuple(map(int, line.split('-'))) for line in data
    ])

    starting_ips = [y+1 for x, y in blacklists]
    valid_ips = [ip for ip in starting_ips if is_valid(ip, blacklists)]
    if part == 1:
        return valid_ips[0]

    total = 0
    for ip in valid_ips:
        while is_valid(ip, blacklists):
            total += 1
            ip += 1
    return total


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 10)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
