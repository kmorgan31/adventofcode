#!/usr/bin/python

from aocd import lines

from collections import defaultdict


EXAMPLE = [
    "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
    "trh fvjkl sbzzf mxmxvkd (contains dairy)",
    "sqjhc fvjkl (contains soy)",
    "sqjhc mxmxvkd sbzzf (contains fish)"
]


def parse_data(data):
    ingredient_lists = []
    for line in data:
        line = line.replace("(", "").replace(")", "")

        words, contains = line.split(" contains ")
        words = words.split()
        contains = contains.split(", ")

        ingredient_lists.append((words, contains))
    return ingredient_lists


def main(data, part=None):
    ingredient_lists = parse_data(data)

    allergens_dict = defaultdict(list)
    for ingredients, allergens in ingredient_lists:
        for a in allergens:
            allergens_dict[a].append(set(ingredients))

    # get ingredients with no allergens
    for k, v in allergens_dict.items():
        allergens_dict[k] = set.intersection(*v)

    # assign allergens to ingredients
    ingredients_found = set()
    known_allergen_ingredient = {}
    sorted_allergens = sorted(allergens_dict.keys(), key=lambda x: len(allergens_dict[x]))
    while sorted_allergens:
        allergen = sorted_allergens.pop(0)

        ingredient = allergens_dict[allergen].pop()
        known_allergen_ingredient[allergen] = ingredient
        ingredients_found.add(ingredient)

        # remove from fields
        del allergens_dict[allergen]

        # remove ingredient from other allergens_dict
        for a in sorted_allergens:
            if ingredient in allergens_dict[a]:
                allergens_dict[a].remove(ingredient)
            if len(allergens_dict[a]) == 0:
                del allergens_dict[a]

        # resort list to get next in line
        sorted_allergens = sorted(allergens_dict.keys(), key=lambda x: len(allergens_dict[x]))

    if part == 1:
        # count number of ingredients with no allergens appear in ingredients list
        return sum(
            [len(set(w) - ingredients_found) for w, c in ingredient_lists]
        )
    elif part == 2:
        return ','.join(v for k,v in sorted(known_allergen_ingredient.items()))


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
