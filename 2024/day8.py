#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

import itertools
from collections import defaultdict


EXAMPLE = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

class Grid:

	def __init__(self, data):
		self.antinodes = set()

		lines = data.split("\n")
		self.max_x = len(lines)
		self.max_y = len(lines[0])
		self.get_frequencies(lines)

	def get_frequencies(self, lines):
		self.frequencies = defaultdict(list)
		self.flip_frequencies = {}
		
		for x in range(self.max_x):
			for y in range(self.max_y):
				if lines[x][y] != ".":
					self.frequencies[lines[x][y]].append((x, y))
					self.flip_frequencies[(x, y)] = lines[x][y]

	def print(self, label):
		print(label)
		for x in range(self.max_x):
			res = ""
			for y in range(self.max_y):
				if (x, y) in self.flip_frequencies:
					res += self.flip_frequencies[(x, y)]
				elif (x, y) in self.antinodes:
					res += "#"
				else:
					res += "."
			print(res)
		print("\n")

def main(data, part=None):
	

	grid = Grid(data)
	# grid.print("Initial")
	for freq, nodes in grid.frequencies.items():
		combinations = itertools.combinations(nodes, 2)
		for (x1, y1), (x2, y2) in combinations:
			# print(f"Antennas: {(x1, y1)} & {(x2, y2)}")
			# determine distance between nodes
			dx, dy = x2-x1, y2-y1

			# determine antinodes same distance from nodes within grid
			nx1, ny1 = x1 - dx, y1 - dy
			nx2, ny2 = x2 + dx, y2 + dy
			
			while 0 <= nx1 < grid.max_x and 0 <= ny1 < grid.max_y and (nx1, ny1) not in nodes:
				grid.antinodes.add((nx1, ny1))
				if part == 1:
					break
				nx1, ny1 = nx1 - dx, ny1 - dy

			while 0 <= nx2 < grid.max_x and 0 <= ny2 < grid.max_y and (nx2, ny2) not in nodes:
				grid.antinodes.add((nx2, ny2))
				if part == 1:
					break
				nx2, ny2 = nx2 + dx, ny2 + dy
	grid.print("Final")
	if part == 1:
		return(len(grid.antinodes))
	else:
		antennas = set(grid.antinodes) | set(grid.flip_frequencies.keys())
		return(len(antennas))



if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, 1)}')
    # print(f'Part 1 {main(data, 1)}')
    # print(f'Part 2 {main(EXAMPLE, 2)}')
    print(f'Part 2 {main(data, 2)}')