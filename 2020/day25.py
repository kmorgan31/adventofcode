#!/usr/bin/python


EXAMPLE = [5764801, 17807724]
INPUT = [3469259, 13170438]


def main(data):
    # find loop_size that converts subject_num (7) to one of the public keys
    v, lp = 1, 0
    while v != data[0]:
        v = v * 7 % 20201227
        lp += 1

    # get the 
    return pow(data[1], lp, 20201227)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE)}')
    print(f'Part 1 {main(INPUT)}')
    # print(f'Part 2 {main(lines, 2)}')
