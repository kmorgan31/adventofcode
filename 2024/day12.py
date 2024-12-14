#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

import itertools
from collections import defaultdict


EXAMPLE = """AAAA
BBCD
BBCC
EEEC"""

EXAMPLE_2 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""



def main(data, part=None):
	garden = [list(line) for line in data.split("\n")]
	max_x = len(garden)
	max_y = len(garden[0])

	def same_region(i, j, plant):
		return 0 <= i < max_x and 0 <= j < max_y and garden[i][j] == plant

	def get_surrounding_pos(x, y):
		return [
			(x+1, y),
			(x-1, y),
			(x, y+1),
			(x, y-1)
		]

	def get_corners(x, y, plant):
		NW, W, SW, N, S, NE, E, SE = [
	        same_region(x+a, y+b, plant)
	        for a in range(-1, 2) 
	        for b in range(-1, 2) 
	        if a or b
	    ]
		return sum([
			N and W and not NW, 
			N and E and not NE, 
			S and W and not SW, 
			S and E and not SE, 
			not (N or W),
			not (N or E),
			not (S or W),
			not (S or E)
		])


	def find_region_1(pos):
		fence = 0
		region = set()
		plant = garden[pos[0]][pos[1]]

		queue = [pos]
		while queue:
			i, j = queue.pop()
			if (i, j) in region:
				continue
			if not same_region(i, j, plant):
				fence += 1
				continue

			# visit
			region.add((i, j))
			for w, z in get_surrounding_pos(i, j):
				if (w, z) not in region:
					queue.append((w, z))

		return region, len(region) * fence

	def find_region_2(pos):
		fence = 0
		region = set()
		plant = garden[pos[0]][pos[1]]

		queue = [pos]
		while queue:
			i, j = queue.pop()

			# visit
			region.add((i, j))
			for w, z in get_surrounding_pos(i, j):
				if same_region(w, z, plant) and (w, z) not in region and (w, z) not in queue:
					queue.append((w, z))

		corners = sum(get_corners(x, y, plant) for x, y in region)
		return region, len(region) * corners


	total = 0
	visited = set()
	for x in range(max_x):
		for y in range(max_y):
			if (x, y) not in visited:
				if part == 1:
					region, cost = find_region_1((x, y))
				elif part == 2:
					region, cost = find_region_2((x, y))
				visited |= region
				total += cost

	return total


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, 1)}')
    # print(f'Part 1 {main(EXAMPLE_2, 1)}')
    # print(f'Part 1 {main(data, 1)}')
    print(f'Part 2 {main(EXAMPLE, 2)}')
    print(f'Part 2 {main(EXAMPLE_2, 2)}')
    print(f'Part 2 {main(data, 2)}')