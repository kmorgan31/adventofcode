#!/usr/bin/python

from aocd import lines
from statistics import median


test_data = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]'
]


corrupted_points_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


incomplete_points_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def check_if_corrupted(line, chunk_dict):
    chunk_stack = []
    for x in line:
        if x in chunk_dict:
            # opening char, add to stack
            chunk_stack.append(x)
        elif chunk_stack:
            # closing char, check against chunk_stack
            if chunk_dict[chunk_stack[-1]] == x:
                # closing char found, pop opening char from stack
                chunk_stack.pop()
            else:
                # matching closing char not found, stack corrupted
                return corrupted_points_dict[x], chunk_stack
    return 0, chunk_stack


def main(data, part=0):
    opening_chars = ['(', '[', '{', '<']
    closing_chars = [')', ']', '}', '>']
    chunk_dict = dict(zip(opening_chars, closing_chars))

    corrupted_score = 0
    incomplete_scores = []

    for line in data:
        corrupted_points, chunk_stack = check_if_corrupted(line, chunk_dict)
        if corrupted_points:
            corrupted_score += corrupted_points
        elif chunk_stack:
            # find sequence to complete line
            line_points = 0
            while chunk_stack:
                # find the closing character and add points
                line_points = (
                    line_points * 5 +
                    incomplete_points_dict[chunk_dict[chunk_stack.pop()]]
                )

            # add line points to incomplete scores
            incomplete_scores.append(line_points)

    if part == 1:
        return corrupted_score
    elif part == 2:
        return median(incomplete_scores)


if __name__ == '__main__':

    # test
    print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 10: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
