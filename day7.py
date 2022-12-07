#!/usr/bin/python
import bisect

from aocd import lines

TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000


EXAMPLE = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = {}

    @property
    def size(self):
        total_file_size = sum(file.size for file in self.files)
        total_directory_size = sum(
            directory.size for directory in self.directories.values()
        )
        return total_file_size + total_directory_size

    def add_file(self, file):
        self.files.append(file)

    def add_directory(self, directory):
        self.directories[directory.name] = directory


class File:
    def __init__(self, name, size, parent=None):
        self.name = name
        self.parent = parent
        self.size = int(size)


def get_curr_node(curr_node, root, folder_name):
    # parse command
    if folder_name == "..":
        return curr_node.parent
    elif folder_name == "/":
        return root
    else:
        return curr_node.directories.get(folder_name)


def print_folder(folder, level=0, tab_size=2):
    spacing = " " * (level * tab_size)
    print(f'{spacing}{folder.name} (dir)')

    level += 1
    children_spacing = " " * (level * tab_size)
    for x in folder.files:
        print(f'{children_spacing}{x.name} (file: {x.size})')
    for x, y in folder.directories.items():
        print_folder(y, level=level)


def filesystem(data):
    root = Directory("/")
    curr_node = root

    for line in data:
        line = line.split()

        if line[0] == "$":
            if line[1] == "cd":
                curr_node = get_curr_node(curr_node, root, line[2])
            elif line[1] == "ls":
                pass

        elif line[0] == "dir" and not curr_node.directories.get(line[1]):
            # add directory
            curr_node.add_directory(Directory(line[1], curr_node))
        else:
            # add file (filesize + name) to parent directory
            curr_node.add_file(File(line[1], line[0], curr_node))

    return root


def calc_sizes(root):
    sizes = []

    to_visit = [root]
    while to_visit:
        curr_node = to_visit.pop()
        sizes.append(curr_node.size)
        to_visit.extend(curr_node.directories.values())
    return sizes


def part_1(sizes):
    return sum([size for size in sizes if size < 100000])


def part_2(sizes):
    current_unused_space = TOTAL_SPACE - sizes[-1]
    additional_required_space = SPACE_NEEDED - current_unused_space
    i = bisect.bisect_left(sizes, additional_required_space)
    return sizes[i]


def main(data, part=None):
    root = filesystem(data)
    # print_folder(root)

    sizes = sorted(calc_sizes(root))
    print(f'Part 1 {part_1(sizes)}')
    print(f'Part 2 {part_2(sizes)}')


if __name__ == '__main__':
    # main(EXAMPLE)
    main(lines)
