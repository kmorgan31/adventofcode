#!/usr/bin/python

from aocd import lines

import re


EXAMPLE = [
    "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
    "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
]

RACE_TIME = 2503


class Ingredient:

    def __init__(self, name, capacity, durability, flavour, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavour = flavour
        self.texture = texture
        self.calories = calories


def get_total(ingredients, attribute, nums):
    return sum(
        getattr(ingredients[i], attribute) * nums[i]
        for i in range(len(ingredients))
    )


def main(data, part=None):
    ingredients = [
        Ingredient(line.split()[0], *map(int, re.findall(r'-?\d+', line)))
        for line in data
    ]

    best_score = 0
    for x in range(99):
        for y in range(99):
            for z in range(99):
                rem = 100 - (x + y + z)
                nums = [x, y, z, rem]
                if sum(nums) > 100:
                    continue

                capacity = max(0, get_total(ingredients, "capacity", nums))
                durability = max(0, get_total(ingredients, "durability", nums))
                flavour = max(0, get_total(ingredients, "flavour", nums))
                texture = max(0, get_total(ingredients, "texture", nums))
                calories = max(0, get_total(ingredients, "calories", nums))

                if part == 2 and calories != 500:
                    continue

                if any(x == 0 for x in [capacity, durability, flavour, texture]):
                    continue

                best_score = max(best_score, capacity * durability * flavour * texture)

    return best_score


if __name__ == '__main__':
    # print(f'Example {part_1(EXAMPLE)}')
    # print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
