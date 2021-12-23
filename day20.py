#!/usr/bin/python

from aocd import lines


test_data = [
    '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#',
    '',
    '#..#.',
    '#....',
    '##..#',
    '..#..',
    '..###'
]


class PixelBoard():

    def __init__(self, data):
        self.algorithm = data[0]
        self.image = [list(line) for line in data[2:]]
        self.image_size_x = len(self.image)
        self.image_size_y = len(self.image[0])
        self.default_pixel_value = None

    def determine_default_pixel_value(self):
        # pixel square of '.' will default to algorithm[0]
        if self.default_pixel_value == '.':
            self.default_pixel_value = self.algorithm[0]
        elif self.default_pixel_value == '#':
            self.default_pixel_value = self.algorithm[-1]
        else:
            self.default_pixel_value = '.'

    def extend_image(self):
        # adds padding of 2 pixels on all sides to given pixel image
        self.image_size_x = self.image_size_x + 4
        self.image_size_y = self.image_size_y + 4
        empty_line = [[self.default_pixel_value] * self.image_size_y]

        return (
            empty_line +
            empty_line +
            [
                [self.default_pixel_value, self.default_pixel_value] +
                x +
                [self.default_pixel_value, self.default_pixel_value]
                for x in self.image
            ] +
            empty_line +
            empty_line
        )

    def process_image(self, nth):
        self.image = self.extend_image()

        new_image = []
        for x in range(self.image_size_x):
            image_line = []
            for y in range(self.image_size_y):
                image_line.append(self.get_index_value((x, y)))
            new_image.append(image_line)
        return new_image

    def get_index_value(self, pixel):
        char_to_num = {
            '#': '1',
            '.': '0'
        }

        x, y = pixel
        pixel_square = [
            (x-1, y-1),     # top left
            (x-1, y),       # up
            (x-1, y+1),     # top right
            (x, y-1),       # left
            (x, y),         # center
            (x, y+1),       # right
            (x+1, y-1),     # bottom left
            (x+1, y),       # down
            (x+1, y+1),     # bottom right
        ]

        # convert pixels to binary
        binary_num = ''
        for i, k in pixel_square:
            if 0 <= i <= self.image_size_x-1 and 0 <= k <= self.image_size_y-1:
                binary_num += char_to_num[self.image[i][k]]
            else:
                binary_num += char_to_num[self.default_pixel_value]

        # convert binary to index
        idx = int(binary_num, 2)
        return self.algorithm[idx]

    def num_lit(self):
        count = 0
        for line in self.image:
            for x in line:
                if x == '#':
                    count += 1
        return count

    def print(self):
        for line in self.image:
            print(line)


def main(data, part):
    pixel_board = PixelBoard(data)

    if part == 1:
        num_enhancements = 2
    elif part == 2:
        num_enhancements = 50

    for x in range(num_enhancements):
        pixel_board.determine_default_pixel_value()
        pixel_board.image = pixel_board.process_image(x)

    return pixel_board.num_lit()


if __name__ == '__main__':

    # tests
    print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 20: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
