#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data
import re


EXAMPLE = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def grid(input_data):
    return input_data.split('\n')


def get_words_pos_1(pos):
    x, y = pos
    return [
        [(x, y), (x-1, y-1), (x-2, y-2), (x-3, y-3)],     
        [(x, y), (x+1, y+1), (x+2, y+2), (x+3, y+3)],
        [(x, y), (x-1, y+1), (x-2, y+2), (x-3, y+3)],
        [(x, y), (x+1, y-1), (x+2, y-2), (x+3, y-3)],
        [(x, y), (x+1, y), (x+2, y), (x+3, y)],
        [(x, y), (x-1, y), (x-2, y), (x-3, y)],
        [(x, y), (x, y-1), (x, y-2), (x, y-3)],
        [(x, y), (x, y+1), (x, y+2), (x, y+3)],
    ]

def get_words_pos_2(pos):
    x, y = pos
    return (
        [(x-1, y-1), (x, y), (x+1, y+1)],     
        [(x-1, y+1), (x, y), (x+1, y-1)]
    )

def validate_pos(grid, pos):
    return -1 < pos[0] < len(grid) and -1 < pos[1] < len(grid[0])

def grid_letter(grid, pos):
    return grid[pos[0]][pos[1]]

def validate_word_1(grid, word):
    return ''.join([grid_letter(grid, z) for z in word]) == "XMAS"

def validate_word_2(grid, word):
    return ''.join([grid_letter(grid, z) for z in word]) == "MAS" or ''.join([grid_letter(grid, z) for z in word]) == "SAM"


def main(input_data, part=None):
    total = 0

    crossword = grid(input_data)
    for x in range(len(crossword)):
        for y in range(len(crossword[0])):
            if part == 1:
                if crossword[x][y] != 'X':
                    continue

                for word in get_words_pos_1((x, y)):
                    if not all([validate_pos(crossword, z) for z in word]):
                        continue

                    if validate_word_1(crossword, word):
                        total += 1
            elif part == 2:
                if crossword[x][y] != 'A':
                    continue

                word1, word2 = get_words_pos_2((x, y))
                if not all([validate_pos(crossword, z) for z in word1 + word2]):
                    continue

                if validate_word_2(crossword, word1) and validate_word_2(crossword, word2):
                    total += 1
        
    return total


if __name__ == '__main__':
    print(f'Day 4: Part 1 {main(EXAMPLE, 1)}')
    print(f'Day 4: Part 1 {main(data, 1)}')
    print(f'Day 4: Part 2 {main(EXAMPLE, 2)}')
    print(f'Day 4: Part 2 {main(data, 2)}')
