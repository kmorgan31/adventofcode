#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data
from collections import defaultdict


EXAMPLE = "0 1 10 99 999"
EXAMPLE_2 = "125 17"


def split(stone):
	mid = len(stone) // 2
	return stone[:mid], str(int(stone[mid:]))

def blink(stones):
	new_stones = defaultdict(int)
	for stone, count in stones.items():
		if stone == "0":
			new_stones["1"] += count
		elif len(stone) % 2 == 0:
			left, right = split(stone)
			new_stones[left] += count
			new_stones[right] += count
		else:
			new_stones[str(int(stone) * 2024)] += count
	return new_stones


def main(data, num):
	stones = defaultdict(int)
	for stone in data.split():
		stones[stone] += 1

	for i in range(num):
		stones = blink(stones)
	print(stones)
	return sum(stones.values())


if __name__ == '__main__':
    print(f'Example {main(EXAMPLE, 1)}')
    print(f'Example {main(EXAMPLE_2, 25)}')
    print(f'Part 1 {main(data, 25)}')
    print(f'Part 2 {main(data, 75)}')