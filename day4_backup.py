# #!/usr/bin/python

from aocd import lines


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
            return row

    for col in zip(*card):
        if set(col).issubset(drawn_nums):
            return col

    return False


def calculate_score(card, drawn):
    flat_list = [item for sublist in card for item in sublist]
    unmarked = set(flat_list) - set(drawn)
    return sum(map(int, unmarked)) * int(drawn[-1])


def drawer(drawn_nums):
    drawn = []
    for num in drawn_nums:
        drawn.append(num)
        yield drawn


def check_board(drawn_nums, board):
    for row in board:
        matched_nums = set(row).intersection(drawn_nums)
        if len(matched_nums) == len(row):
            return True

    for column in list(zip(*board)):
        matched_nums = set(column).intersection(drawn_nums)
        if len(matched_nums) == len(column):
            return True

    return False


def check_boards(bingo_cards, bingo_nums):
    unmatched_cards = bingo_cards
    for drawn_nums in drawer(bingo_nums):
        for card in unmatched_cards:
            if check_win(card, drawn_nums):
                unmatched_cards.remove(card)
                print(calculate_score(card, drawn_nums))
                yield card, drawn_nums

        if len(unmatched_cards) == 0:
            break;


if __name__ == '__main__':
    bingo_nums = lines[0].split(',')
    bingo_cards = parse_cards(lines[2:])

    winning_cards = [match for match in check_boards(bingo_cards, bingo_nums)]
