#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data


EXAMPLE = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

EXAMPLE_2 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

MOVES = {
	"<": (0, -1) ,
	"^": (-1, 0),
	">": (0, 1),
	"v": (1, 0)
}


class Warehouse():

	def __init__(self, data, part):
		lines = data.split("\n")
		self.part = part
		self.parse_lines(lines)
		self.max_x, self.max_y = max(self.walls)

	def parse_lines(self, lines):
		self.moves = []
		self.walls = set()
		self.lboxes = set()
		self.rboxes = set()
		self.spaces = set()

		for x in range(len(lines)):
			for y in range(len(lines[x])):
				ny = y * self.part
				if lines[x][y] == "#":
					self.walls.add((x, ny))
					if self.part == 2:
						self.walls.add((x, ny+1))
				elif lines[x][y] == "O":
					self.lboxes.add((x, ny))
					if self.part == 2:
						self.rboxes.add((x, ny+1))
				elif lines[x][y] == ".":
					self.spaces.add((x, ny))
					if self.part == 2:
						self.spaces.add((x, ny+1))
				elif lines[x][y] == "@":
					self.robot = (x, ny)
					if self.part == 2:
						self.spaces.add((x, ny+1))
				elif lines[x][y] in ["<", ">", "^", "v"]:
					self.moves.append(lines[x][y])

	def move_box(self, move, sboxes, box):
		i, j = MOVES[move]

		bx, by = box
		nbx, nby = bx+i, by+j
		sboxes.add((nbx, nby))
		sboxes.remove(box)

		self.spaces.add(box)
		self.spaces.remove((nbx, nby))


	def move_robot(self, move, boxes):
		i, j = MOVES[move]

		# move boxes
		while boxes:
			if len(boxes) == 0:
				return

			box = boxes.pop()
			if self.part == 1:
				self.move_box(move, self.lboxes, box)
			elif self.part == 2:
				# move boxes in pairs
				bx, by = box
				if box in self.lboxes:
					left, right = (bx, by), (bx, by+1)
					boxes.remove(right)
				elif box in self.rboxes:
					left, right = (bx, by-1), (bx, by)
					boxes.remove(left)

				# import pdb; pdb.set_trace()
				if move in ["^", "v", "<"]:
					self.move_box(move, self.lboxes, left)
					self.move_box(move, self.rboxes, right)
				else:
					self.move_box(move, self.rboxes, right)
					self.move_box(move, self.lboxes, left)
	
		# move robot
		rx, ry = self.robot
		nrx, nry = rx+i, ry+j
		self.robot = (nrx, nry)

		self.spaces.add((rx, ry))
		self.spaces.remove(self.robot)
		

	def get_next_pos(self, move, pos):
		i, j = MOVES[move]
		return [(x+i, y+j) for x, y in pos]

	def can_move_robot(self, move, pos):
		# check if robot+1 to wall is a line of boxes
		# check if last_box + 1 is a wall or a space
		# check if pos+1 is a space, wall or box
		boxes = []
		i, j = MOVES[move]

		space = False
		if self.part == 1:
			for (nx, ny) in self.get_next_pos(move, pos):
				if (nx, ny) in self.lboxes:
					space, nboxes = self.can_move_robot(move, [(nx, ny)])
					boxes += [(nx, ny)] + nboxes
				elif (nx, ny) in self.spaces:
					space = True
					break
				elif (nx, ny) in self.walls:
					break

			# if can move, return list of boxes that will move; else empty list
			if space:
				return True, boxes
			return False, []

		elif self.part == 2:
			if all([(nx, ny) in self.spaces for (nx, ny) in self.get_next_pos(move, pos)]):
				return True, boxes
			if any([(nx, ny) in self.walls for (nx, ny) in self.get_next_pos(move, pos)]):
				return False, []

			nboxes = []
			for (nx, ny) in self.get_next_pos(move, pos):
				# get pair for box
				if (nx, ny) in self.lboxes:
					nboxes += [(nx, ny), (nx, ny+1)]
				elif (nx, ny) in self.rboxes:
					nboxes += [(nx, ny-1), (nx, ny)]

			for nbox in nboxes:
				if nbox not in boxes:
					boxes.append(nbox)

			if move in ["<", ">"]:
				space, nboxes = self.can_move_robot(move, [(nx, ny)])
				for nbox in nboxes:
					if nbox not in boxes:
						boxes.append(nbox)
			else:
				space, nboxes = self.can_move_robot(move, nboxes)
				for nbox in nboxes:
					if nbox not in boxes:
						boxes.append(nbox)

			# if can move, return list of boxes that will move; else empty list
			if space:
				return True, boxes
			return False, []

	def calculate_gps_coordinates(self):
		total = 0
		for box in self.lboxes:
			bx, by = box
			total += (100 * bx) + by
		return total

	def print(self):
		for x in range(self.max_x+1):
			line = ""
			for y in range(self.max_y+1):
				if (x, y) in self.walls:
					line += "#"
				elif (x, y) in self.lboxes:
					if self.part == 1:
						line += "O"
					elif self.part == 2:
						line += "["
				elif (x, y) in self.rboxes:
					line += "]"
				elif (x, y) in self.spaces:
					line += "."
				elif (x, y) == self.robot:
					line += "@"
			print(line)
		print("\n")


def main(data, part):
	warehouse = Warehouse(data, part)
	for move in warehouse.moves:
		can_move, boxes = warehouse.can_move_robot(move, [warehouse.robot])
		if can_move:
			# if list not empty, update robot + boxes
			warehouse.move_robot(move, boxes)

	# calculate gps coordinates
	return warehouse.calculate_gps_coordinates()


if __name__ == '__main__':
    print(f'Part 1 {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(data, 1)}')
    print(f'Part 2 {main(EXAMPLE_2, 2)}')
    print(f'Part 2 {main(data, 2)}')
