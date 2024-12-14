#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

import math

import re

EXAMPLE = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def robots(data):
	for line in data.split('\n'):
		px, py, vx, vy = [int(x) for x in re.findall('\-*\d+', line)]
		yield px, py, vx, vy


def correct_pos(pt, max_pos):
	return max_x - pt if pt < 0 else pt


def part_1(data, max_x, max_y):
	robot_pos = []
	for px, py, vx, vy in robots(data):
		vx100, vy100 = vx * 100, vy * 100
		px100, py100 = (px + vx100) % max_x, (py + vy100) % max_y
		px100, py100 = correct_pos(px100, max_x), correct_pos(py100, max_y)
		robot_pos.append((px100, py100))

	q = [0, 0, 0, 0]
	for rx, ry in robot_pos:
		if rx == max_x // 2 or ry == max_y // 2:
			continue

		q_idx = (int(rx > max_x // 2)) + (int(ry > max_x // 2) * 2)
		q[q_idx] += 1
	return q[0] * q[1] * q[2] * q[3]

def part_2(data, max_x, max_y):
	t = 0
	while True:
		t += 1
		robot_pos = set()
		valid = True

		for px, py, vx, vy in robots(data):
			vxt, vyt = vx * t, vy * t
			pxt, pyt = (px + vxt) % max_x, (py + vyt) % max_y
			pxt, pyt = correct_pos(pxt, max_x), correct_pos(pyt, max_y)
			if (pxt, pyt) in robot_pos:
				valid = False
				break
			robot_pos.add((pxt, pyt))

		if valid:
			return t


if __name__ == '__main__':
    # print(f'Part 1 {part_1(EXAMPLE, 11, 7)}')
    # print(f'Part 1 {part_1(data, 101, 103)}')
    print(f'Part 2 {part_2(data, 101, 103)}')