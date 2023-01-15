#!/usr/bin/python

from aocd import lines

import functools
from itertools import product

test_data = [
    'Player 1 starting position: 4',
    'Player 2 starting position: 8'
]


class Player():

    def __init__(self, num, start_pos):
        self.num = num
        self.pos = int(start_pos)-1
        self.score = 0
        self.wins = 0

    def turn(self, game):
        # move pawn
        die_nums = []
        for x in range(3):
            die_nums.append(game.roll_die())

        self.pos = (self.pos + sum(die_nums)) % 10

        # update score
        self.score += self.pos + 1

        # self.print(die_nums)

    def print(self, die_nums):
        print(f'Player {self.num} rolls {die_nums[0]}+{die_nums[1]}+{die_nums[2]} New pos {self.pos+1} Score {self.score}')


class Die():

    def __init__(self, sides):
        self.die_num = 0
        self.times_die_rolled = 0
        self.sides_of_die = sides


class Game():

    def __init__(self, players):
        self.players = players
        self.dices = []
        self.board = ['.' * 10]

    def add_die(self, die):
        self.dices.append(die)

    def roll_die(self):
        self.die_num += 1
        self.times_die_rolled += 1
        if self.die_num > self.sides_of_die:
            self.die_num = self.die_num % self.sides_of_die
        return self.die_num

    def play(self, end_score):
        while True:
            player = self.players.pop(0)
            player.turn(self)
            if player.score >= end_score:
                return player, self.players[0]
            else:
                self.players.append(player)


@functools.lru_cache(maxsize=None)
def part_2(p1, s1, p2, s2):
    w1 = w2 = 0
    for m1, m2, m3 in product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        p1_copy = (p1 + m1 + m2 + m3) % 10 if (p1 + m1 + m2 + m3) % 10 else 10
        s1_copy = s1 + p1_copy
        if s1_copy >= 21:
            w1 += 1
        else:
            w2_copy, w1_copy = part_2(p2, s2, p1_copy, s1_copy)
            w1 += w1_copy
            w2 += w2_copy
    return w1, w2


def main(data, part):
    p1 = Player(1, data[0].split(': ')[-1])
    p2 = Player(2, data[1].split(': ')[-1])
    game = Game([p1, p2])

    if part == 1:
        game.add_die(Die(100))
        end_score = 1000

        winner, loser = game.play(end_score)
        return game.times_die_rolled * loser.score
    elif part == 2:
        w1, w2 = part_2(p1.pos+1, p1.score, p2.pos+1, p2.score)
        return max([w1, w2])


if __name__ == '__main__':

    # tests
    # print(f'Test Data: Part 1 {main(test_data, 1)}, Part 2 {main(test_data, 2)}')

    # question
    print(f'Day 21: Part 1 {main(lines, 1)}')
    print(f'Day 21: Part 2 {main(lines, 2)}')
