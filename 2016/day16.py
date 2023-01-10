#!/usr/bin/python


EXAMPLE = "10000"
INPUT = "00101000101111010"


def get_checksum(num):
    checksum = ""
    for i in range(0, len(num)-1, 2):
        x, y = num[i:i+2]
        checksum += "1" if x == y else "0"

    if len(checksum) % 2 == 0:
        return get_checksum(checksum)
    return checksum


def main(data, disk_size):
    while len(data) < disk_size:
        cpy = ''.join('0' if i == '1' else '1' for i in data[::-1])
        data = f"{data}0{cpy}"
    return get_checksum(data[:disk_size])


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 20)}')
    print(f'Part 1 {main(INPUT, 272)}')
    print(f'Part 2 {main(INPUT, 35651584)}')
