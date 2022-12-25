#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags"
]

EXAMPLE_2 = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags.",
]


def check_children(bags, children):
    if "shiny_gold" in children:
        return True

    return any(check_children(bags, bags[child]) for child in children)


def count_children(bags, bag):
    return (
        1 if not bags[bag] else
        sum(v * count_children(bags, k) for k, v in bags[bag].items())+1
    )


def get_bags(data):
    bags = {}
    for line in data:
        bag, children = line.split(" contain ")

        name = '_'.join(bag.split()[:2])

        values = {}
        for x in children.split(", "):
            child = x.split()
            if child[0].isdigit():
                values['_'.join(child[1:3])] = int(child[0])

        bags[name] = values
    return bags


def main(data, part=None):
    bags = get_bags(data)

    if part == 1:
        num_bags = 0
        for bag, children in bags.items():
            if bag == "shiny_gold":
                continue

            if check_children(bags, children):
                num_bags += 1
        return num_bags
    elif part == 2:
        return count_children(bags, "shiny_gold")-1


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE_2, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
