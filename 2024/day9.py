#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data


EXAMPLE = "2333133121414131402"
	

def main(data, part=None):
	disk = []

	blocks = []
	free_spaces = []
	
	id_num = 0
	for idx in range(len(data)):
		if idx % 2 == 0:
			# block information
			block = [id_num] * int(data[idx])
			blocks.append((len(disk), block))
			id_num += 1
		else:
			# free space information
			block = ["."] * int(data[idx])
			free_spaces.append((len(disk), block))
		disk.extend(block)
	# print(f"Disk: {disk}")

	if part == 1:
		idx = 0
		while idx < len(disk)-1:
			if disk[idx] == ".":
				# replace with data from end
				last = disk.pop()
				disk[idx] = last
			else:
				idx += 1
	elif part == 2:
		for x, block in reversed(blocks):
			found = False
			for idx, (y, space) in enumerate(free_spaces):
				if y >= x:
					# free space after block being considered
					break
				if len(space) >= len(block):
					found = True
					break

			if found:
				remaining_space = ["."] * (len(space)-len(block))
				replacement_space = ["."] * (len(block))
				# overwrite space in disk with block
				disk = disk[:y] + block + remaining_space + disk[y+len(space):x] + replacement_space + disk[x+len(block):]
				# update free_spaces at idx
				free_spaces[idx] = (y + len(block), remaining_space)
	# print(f"Disk: {disk}")

	checksum = 0
	for idx, block in enumerate(disk):
		if block == ".":
			continue
		checksum +=  block * idx
	return checksum


if __name__ == '__main__':
    print(f'Part 1 {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(data, 1)}')
    print(f'Part 2 {main(EXAMPLE, 2)}')
    print(f'Part 2 {main(data, 2)}')