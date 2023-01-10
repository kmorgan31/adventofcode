#!/usr/bin/python


from hashlib import md5

EXAMPLE = "abc"
INPUT = "qzyelonm"


def first_triplet(hash):
    for i in range(len(hash)-2):
        if len(set(hash[i:i+3])) == 1:
            return hash[i]


def first_quintuplet(hash):
    for i in range(len(hash)-4):
        if len(set(hash[i:i+5])) == 1:
            return hash[i]


def stretch_word(word, stretch_key):
    hashed = md5(word.encode()).hexdigest()
    for y in range(stretch_key):
        hashed = md5(hashed.encode()).hexdigest()
    return hashed


def main(data, stretch_key):
    hashes = {
        i: stretch_word(data + str(i), stretch_key) for i in range(1000)
    }

    i, num_keys = 0, 0
    while True:
        cur = hashes[i % 1000]
        hashes[i % 1000] = stretch_word(data + str(i+1000), stretch_key)

        t = first_triplet(cur)

        qts = set()
        for hashed in hashes.values():
            qt = first_quintuplet(hashed)
            if qt:
                qts.add(qt)

        if t and t in qts:
            num_keys += 1
            print(f"Key: {num_keys} - val: {i}")
            if num_keys == 64:
                return i

        i += 1


if __name__ == '__main__':
    # print(f'Example {part_2(EXAMPLE)}')
    print(f'Part 1 {main(INPUT, 0)}')
    print(f'Part 2 {main(INPUT, 2016)}')
