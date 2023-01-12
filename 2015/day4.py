#!/usr/bin/python

from hashlib import md5

INPUT = "iwrupvqb"


def main(data, num_zeroes):
    i = 0
    while True:
        word = data + str(i)
        hashed = md5(word.encode("utf-8")).hexdigest()
        if hashed.startswith('0'*num_zeroes):
            return i
        i += 1


if __name__ == '__main__':
    # print(f'Example {part_2(EXAMPLE)}')
    print(f'Part 1 {main(INPUT, 5)}')
    print(f'Part 2 {main(INPUT, 6)}')
