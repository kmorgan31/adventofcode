#!/usr/bin/python

from itertools import combinations


class Item:

    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


class Player:

    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def equip(self, items):
        for i in items:
            self.damage += i.damage
            self.armor += i.armor

    def get_attacked(self, player):
        # given player attacks current player; reduces damage by at least 1 hp
        damage = player.damage - self.armor
        self.hp -= max(damage, 1)


SHOP = {
    "weapons": [
        Item("dagger", 8, 4, 0),
        Item("shortsword", 10, 5, 0),
        Item("warhammer", 25, 6, 0),
        Item("longsword", 40, 7, 0),
        Item("greataxe", 74, 8, 0),
    ],
    "armor": [
        Item("leather", 13, 0, 1),
        Item("chainmail", 31, 0, 2),
        Item("splintmail", 53, 0, 3),
        Item("bandedmail", 75, 0, 4),
        Item("platemail", 102, 0, 5),
        Item("no armor", 0, 0, 0),
    ],
    "rings": [
        Item("damage +1", 25, 1, 0),
        Item("damage +2", 50, 2, 0),
        Item("damage +3", 100, 3, 0),
        Item("defense +1", 20, 0, 1),
        Item("defense +2", 40, 0, 2),
        Item("defense +3", 80, 0, 3),
        Item("no ring 1", 0, 0, 0),
        Item("no ring 2", 0, 0, 0),
    ]
}


def play(players):

    i = 0
    winner = None
    while not winner:
        # player i attacks player i+1
        players[(i+1)%2].get_attacked(players[i%2])
        if players[(i+1)%2].hp <= 0:
            winner = players[i%2]
        i += 1
    return winner.name == "Player"


def main(part):

    min_cost = 999999
    max_cost = 0
    for w in SHOP["weapons"]:
        for a in SHOP["armor"]: # pick 0 - 1 armour
            for r1, r2 in combinations(SHOP["rings"], 2): # pick 0 - 2 rings
                player = Player("Player", 100, 0, 0)
                boss = Player("Boss", 100, 8, 2)

                # buy and equip items
                items = [w, a, r1, r2]
                player.equip(items)
                # print([x.name for x in items])

                cost = sum([i.cost for i in items])
                if play([player, boss]):
                    min_cost = min(min_cost, cost)
                else:
                    max_cost = max(max_cost, cost)

    return min_cost if part == 1 else max_cost


if __name__ == '__main__':
    print(f'Part 1 {main(1)}')
    print(f'Part 2 {main(2)}')
