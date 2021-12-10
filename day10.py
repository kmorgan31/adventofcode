#!/usr/bin/python

import sys
import requests
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


def determine_question():
    return map(int, sys.argv[1].split('.'))


def fetch_data(day):
    cookie = '53616c7465645f5fa5d68c2c74333c3cf12f7d3fd1879c09c13156e540110a1ab1c384fc44a06720c841e41aa6ec5668'
    target_url = f"https://adventofcode.com/2021/day/{day}/input"
    session = requests.Session()
    return session.get(
        target_url, cookies={'session': cookie}
    ).text.strip().split('\n')


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


if __name__ == '__main__':
    day, part = determine_question()
    data = fetch_data(day)

    if 'test' in sys.argv:
        data = test_data

    opening_chars = ['(', '[', '{', '<']
    closing_chars = [')', ']', '}', '>']
    chunk_dict = dict(zip(opening_chars, closing_chars))

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

    print(corrupted_score)
    print(median(incomplete_scores))
