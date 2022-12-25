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
    bingo_nums = lines[0].split(',')
    bingo_cards = parse_cards(lines[2:])

    drawn_nums = []
    winning_scores = []
    for x in bingo_nums:
        drawn_nums.append(x)
        for card in bingo_cards:
            if check_win(card, drawn_nums):
                winning_scores.append(calculate_score(card, drawn_nums))
                bingo_cards.remove(card)

    print(f'Day 4: Part 1 {winning_scores[0]}, Part 2 {winning_scores[-1]}')
