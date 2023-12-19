#!/usr/bin/python

from aocd import lines

from collections import Counter, defaultdict

import math

EXAMPLE = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483"
]

HAND_TYPES = [
    "five_kind",
    "four_kind",
    "full",
    "three_kind",
    "two_pair",
    "one_pair",
    "high_card"
]

CARD_VALUE = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10
}


def determine_hand_type(hand, part):
    counter = Counter(hand)

    if part == 2:
        # if joker present, replace with most common card
        joker = counter["J"]
        if 0 < joker < 5:
            del counter["J"]
            counter[counter.most_common(1)[0][0]] += joker

    if counter.most_common()[0][1] == 5:
        return "five_kind"
    elif counter.most_common()[0][1] == 4:
        return "four_kind"
    elif counter.most_common()[0][1] == 3:
        return "full" if counter.most_common()[1][1] == 2 else "three_kind"
    elif counter.most_common()[0][1] == 2:
        return "two_pair" if counter.most_common()[1][1] == 2 else "one_pair"
    else:
        return "high_card"


def main(data, part=None):
    hands = defaultdict(list)

    if part == 2:
        CARD_VALUE["J"] = 1

    for line in data:
        hand, bid = line.split()
        print(f'Hand {hand}')

        hand_type = determine_hand_type(hand, part)
        hands[hand_type].append(
            ([CARD_VALUE[h] if h in CARD_VALUE else int(h) for h in hand], int(bid))
        )

    rank = 1
    winnings = 0
    for hand_type in HAND_TYPES[::-1]:
        if not hands[hand_type]:
            continue

        hands[hand_type].sort()
        print(f"Current rank: {rank}")
        print(f"Hand type: {hand_type}: {hands[hand_type]}\n")
        for hand_entry in hands[hand_type]:
            if 1 in hand_entry[0]:
                print(f"Hand {hand_entry[0]} -> winning: {hand_entry[1] * rank}")
            winnings += hand_entry[1] * rank
            rank += 1
    return winnings


if __name__ == '__main__':
    # print(f'Day 7: Part 1 {main(EXAMPLE, part=1)}')
    print(f'Day 7: Part 2 {main(lines, part=2)}')
