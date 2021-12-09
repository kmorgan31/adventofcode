# #!/usr/bin/python

import sys
import requests


def determine_question():
    return map(int, sys.argv[1].split('.'))


def fetch_data(day):
    cookie = '53616c7465645f5fa5d68c2c74333c3cf12f7d3fd1879c09c13156e540110a1ab1c384fc44a06720c841e41aa6ec5668'
    target_url = f"https://adventofcode.com/2021/day/{day}/input"
    session = requests.Session()
    return session.get(
        target_url, cookies={'session': cookie}
    ).text.strip().split('\n')


def parse_cards(data):
    bingo_cards = []

    start = 0
    while start < len(data):
        bingo_cards.append([line.split() for line in data[start:start+5]])
        start += 6
    return bingo_cards


def check_win(card, drawn_nums):
    for row in card:
        if set(row).issubset(drawn_nums):
            return True

    for col in zip(*card):
        if set(col).issubset(drawn_nums):
            return True

    return False


def calculate_score(card, drawn):
    flat_list = [item for sublist in card for item in sublist]
    unmarked = set(flat_list) - set(drawn)
    return sum(map(int, unmarked)) * int(drawn[-1])


if __name__ == '__main__':
    day, part = determine_question()

    data = fetch_data(day)
    bingo_nums = data[0].split(',')
    bingo_cards = parse_cards(data[2:])

    drawn_nums = []
    for x in bingo_nums:
        drawn_nums.append(x)
        for card in bingo_cards:
            if check_win(card, drawn_nums):
                print(calculate_score(card, drawn_nums))
                bingo_cards.remove(card)
