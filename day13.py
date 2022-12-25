#!/usr/bin/python

from aocd import lines

test_data = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5'
]


class Grid():

    def __init__(self):
        self.points = []
        self.folds = []

    def parse_input(self, data):
        for line in data:
            if not line:
                continue

            line = line.split(',')
            if len(line) > 1:
                x, y = map(int, line)
                self.points.append((x, y))
            else:
                line = line[0].split('=')
                self.folds.append((line[0][-1], int(line[1])))

    def draw_grid(self):
        self.grid = []

        self.max_x = max([x for x, y in self.points]) + 1
        self.max_y = max([y for x, y in self.points]) + 1

        for x in range(self.max_y):
            self.grid.append(['.'] * self.max_x)

        # add points
        for x, y in self.points:
            self.grid[y][x] = '#'

    def fold_up(self, point, fold_y):
        # returns coords of new point
        # point moved up twice the distance from the fold
        x, y = point
        distance_from_fold = y - fold_y
        new_y = y-(distance_from_fold * 2)
        return (x, new_y)

    def fold_left(self, point, fold_x):
        # returns coords of new point
        # point moved left twice the distance from the fold
        x, y = point
        distance_from_fold = x - fold_x
        new_x = x-(distance_from_fold * 2)
        return (new_x, y)

    def print_grid(self):
        for line in self.grid:
            print(''.join(line))


def main(data, part):
    grid = Grid()
    grid.parse_input(data)

    if part == 1:
        grid.folds = [grid.folds[0]]

    for i, j in grid.folds:
        grid.draw_grid()
        points = set()
        for point in grid.points:
            if i == 'y' and point[1] > j:
                point = grid.fold_up(point, j)
            elif i == 'x' and point[0] > j:
                point = grid.fold_left(point, j)
            points.add(point)

        grid.points = points

    if part == 2:
        grid.draw_grid()
        grid.print_grid()

    return len(grid.points)


if __name__ == '__main__':

    # test
    print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 13: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
