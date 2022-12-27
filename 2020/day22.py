#!/usr/bin/python

from aocd import lines

import re


EXAMPLE = [
    "Player 1:",
    "9",
    "2",
    "6",
    "3",
    "1",
    "",
    "Player 2:",
    "5",
    "8",
    "4",
    "7",
    "10",
]


class Player:

    def __init__(self, num, deck):
        self.num = num
        self.deck = deck

    @property
    def count(self):
        return len(self.deck)

    def calculate_score(self):
        return sum(num*i for num, i in zip(self.deck, range(self.count,-1,-1)))


class Game:

    def __init__(self, data):
        self.parse_players(data)
        self.game_num = 1

    def total_cards(self, players):
        return sum(player.count for player in players)

    def parse_players(self, data):
        self.players = []

        player_num, deck = 0, []
        for line in data:
            if not line:
                self.players.append(Player(player_num, deck))

                deck = []
                continue

            if ":" in line:
                player_num = int(re.findall(r'\d+', line)[0])
            else:
                deck.append(int(line))

        if deck:
            self.players.append(Player(player_num, deck))

    def find_winner(self, players):
        for p in players:
            if len(p.deck) == self.total_cards(players):
                return p

    def copy_player(self, player, num):
        return Player(player.num, player.deck[:num])

    def play(self):
        winner = None
        while not winner:
            p1 = self.players[0].deck.pop(0)
            p2 = self.players[1].deck.pop(0)

            if p1 > p2:
                self.players[0].deck.extend([p1, p2])
            elif p2 > p1:
                self.players[1].deck.extend([p2, p1])

            winner = self.find_winner(self.players)
        return winner.calculate_score()

    def play_recursive(self, players):
        previous_rounds = set()

        winner = None
        while not winner:
            round_state = tuple(players[0].deck)
            if round_state in previous_rounds:
                return players[0]
            else:
                previous_rounds.add(round_state)

            p1, p2 = players[0].deck.pop(0), players[1].deck.pop(0)
            if players[0].count >= p1 and players[1].count >= p2:
                sub_game_winner = self.play_recursive(
                    [self.copy_player(players[0], p1), self.copy_player(players[1], p2)]
                )
            else:
                sub_game_winner = players[0] if p1 > p2 else players[1]

            if sub_game_winner.num == players[0].num:
                players[0].deck.extend([p1, p2])
            elif sub_game_winner.num == players[1].num:
                players[1].deck.extend([p2, p1])

            winner = self.find_winner([players[0], players[1]])
        return winner


def main(data, part=None):
    game = Game(data)
    if part == 1:
        return game.play()
    elif part == 2:
        return game.play_recursive(game.players).calculate_score()


if __name__ == '__main__':
    # print(f'EXAMPLE 1 {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
