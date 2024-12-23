#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

EXAMPLE = "123"


EXAMPLE_2 = """1
10
100
2024"""


def mix(secret, num):
    return secret ^ num

def prune(secret):
    return secret % 16777216

def get_next_secret(secret):
    secret = prune(mix(secret, secret << 6))
    secret = prune(mix(secret, secret >> 5))
    return prune(mix(secret, secret << 11))


def main(data, part):
    seeds = list(map(int, data.splitlines()))

    sequences = {}

    total = 0
    for i, seed in enumerate(seeds):
        prices = [seed%10]
        changes = []

        for x in range(2000):
            seed = get_next_secret(seed)

            prices.append(seed%10)
            changes.append(prices[-1] - prices[-2])
        total += seed

        if part == 1:
            continue

        # part 2
        seen = set()
        for p in range(4, len(changes)):
            seq = tuple(changes[p-3:p+1])
            if seq not in sequences and seq not in seen:
                # add the price for that sequence of 4 changes
                sequences[seq] = prices[p+1]
            elif seq not in seen:
                # seen in another monkey, but not this one
                sequences[seq] += prices[p+1]
            seen.add(seq)

    if part == 1:
        return total
    elif part == 2:
        return max(sequences.values())


if __name__ == '__main__':
    print(f'Part 1 {main(EXAMPLE, 10)}')
    print(f'Part 1 {main(EXAMPLE_2, 2000)}')
    print(f'Part 1 {main(data, 1)}')
    print(f'Part 2 {main(data, 2)}')
