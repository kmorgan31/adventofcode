#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

import re


EXAMPLE = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def claws(data):
	lines = data.split('\n')

	claws = []
	for i in range(0, len(lines)//4 + 1):
	    a = tuple([int(x) for x in re.findall('\d+', lines[i*4])])
	    b = tuple([int(x) for x in re.findall('\d+', lines[i*4+1])])
	    p = tuple([int(x) for x in re.findall('\d+', lines[i*4+2])])
	    yield a, b, p


def main(data, part=None):
	total = 0
	for a, b, p in claws(data):
		ax, ay = a
		bx, by = b
		px, py = p

		if part == 2:
			px += 10000000000000
			py += 10000000000000

		solution_a, solution_b = None, None
		if (bx * py - by * px) / (bx * ay - by * ax) == (bx * py - by * px) // (bx * ay - by * ax):
			solution_a = (bx * py - by * px) // (bx * ay - by * ax)
			if (py - solution_a * ay) / by == (py - solution_a * ay) // by:
				solution_b = (py - solution_a * ay) // by
		if solution_a is None or solution_b is None:
			total += 0
		else:
			total += solution_a * 3 + solution_b
	return total


if __name__ == '__main__':
    print(f'Part 1 {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(data, 1)}')
    print(f'Part 2 {main(EXAMPLE, 2)}')
    print(f'Part 2 {main(data, 2)}')