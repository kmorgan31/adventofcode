#!/usr/bin/python

from aocd import lines
from collections import defaultdict, Counter


test_data = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end'
]

test_data_2 = [
    'dc-end',
    'HN-start',
    'start-kj',
    'dc-start',
    'dc-HN',
    'LN-dc',
    'HN-end',
    'kj-sa',
    'kj-HN',
    'kj-dc'
]


paths = []


class Cave():

    def __init__(self, part):
        self.part = part
        self.cave_map = defaultdict(list)
        self.path_with_small_caves_count = 0
        self.path_count = 0

    def create_cave_map(self, data):
        # returns dict of caves and their next connected caves
        for line in data:
            x, y = line.split('-')
            self.cave_map[x].append(y)
            self.cave_map[y].append(x)

    def _get_paths(self, cave, path=[]):
        # add current cave to path
        path.append(cave)

        if cave == 'end':
            self.path_count += 1
            if not (''.join(path).isupper()):
                # path includes at least one small cave
                self.path_with_small_caves_count += 1
        else:
            for next_cave in self.cave_map[cave]:
                if self.can_enter_cave(next_cave, path):
                    self._get_paths(next_cave, path)

        # take step back to explore other paths
        path.pop()

    def can_enter_cave(self, cave, path):
        if self.part == 1:
            return cave.isupper() or cave not in path
        elif self.part == 2:
            if cave.islower() and cave in path:
                if cave == 'start' or cave == 'end':
                    return False

                path_count_map = Counter(path)
                if any(k.islower() and v == 2 for k, v in path_count_map.items()):
                    return False
            return True


def main(data, part):

    caves = Cave(part)
    caves.create_cave_map(data)

    caves._get_paths('start')
    if part == 1:
        return caves.path_with_small_caves_count
    elif part == 2:
        return caves.path_count


if __name__ == '__main__':

    # test
    print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 12: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
