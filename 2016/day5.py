#!/usr/bin/python

from hashlib import md5

EXAMPLE = "abc"
INPUT = "reyedfim"


def part_1(data):
    i = 0

    password = ""
    while len(password) < 8:
        word = data + str(i)
        hashed = md5(word.encode("utf-8")).hexdigest()
        if hashed.startswith('00000'):
            password += hashed[5]
        i += 1

    return ''.join(password)


def part_2(data):
    i = 0

    password = ["."] * 8
    while any(x == "." for x in password):
        word = data + str(i)
        hashed = md5(word.encode("utf-8")).hexdigest()
        if hashed.startswith('00000'):
            pos = hashed[5]
            if pos.isdigit() and int(pos) < 8 and password[int(pos)] == ".":
                password[int(pos)] = hashed[6]
                print(password)
        i += 1

    return ''.join(password)


if __name__ == '__main__':
    # print(f'Example {part_2(EXAMPLE)}')
    print(f'Part 1 {part_1(INPUT)}')
    print(f'Part 2 {part_2(INPUT)}')
