#!/usr/bin/python

EXAMPLE = list(map(int,"389125467"))
INPUT = list(map(int,"186524973"))


def print_ans(cups):
    return ''.join(
        map(str, [cups[(i+cups.index(1))%len(cups)] for i in range(len(cups))])
    )[1:]


def part_1(cups, rounds):
    current_cup = cups[0]
    min_cup, max_cup = min(cups), max(cups)

    for i in range(rounds):
        # pick up cups
        x, y, z = cups.pop(1), cups.pop(1), cups.pop(1)

        # get destination cup
        destination_cup = current_cup - 1
        while destination_cup < min_cup or destination_cup in (x, y, z):
            destination_cup = (
                destination_cup - 1 if destination_cup > min_cup else max_cup
            )

        # insert picked up cups after destination cup idx
        destination_cup_idx = cups.index(destination_cup)
        cups.insert(destination_cup_idx+1, x)
        cups.insert(destination_cup_idx+2, y)
        cups.insert(destination_cup_idx+3, z)

        # get new current
        current_cup = cups[cups.index(current_cup) + 1]

        # move the cups around so current cup moved to the front
        while cups.index(current_cup) > 0:
            cups.append(cups.pop(0))

    return print_ans(cups)


def part_2(cups, rounds):
    current_cup = cups[0]
    min_cup, max_cup = min(cups), max(cups)

    next_cup_dict = dict(zip(cups, cups[1:] + [cups[0]]))

    for i in range(rounds):
        # pick up cups
        x = next_cup_dict[current_cup]
        y = next_cup_dict[x]
        z = next_cup_dict[y]

        # get destination cup
        destination_cup = current_cup - 1
        while destination_cup < min_cup or destination_cup in (x, y, z):
            destination_cup = (
                destination_cup - 1 if destination_cup > min_cup else max_cup
            )

        # insert picked up cups after destination cup idx
        next_cup_dict[current_cup] = next_cup_dict[z]
        next_cup_dict[z] = next_cup_dict[destination_cup]
        next_cup_dict[destination_cup] = x

        # get new current
        current_cup = next_cup_dict[current_cup]

    c = next_cup_dict[1]
    d = next_cup_dict[c]
    return c * d


def main(cups, part=None):
    if part == 1:
        return part_1(cups, 100)
    elif part == 2:
        cups = cups + list(range(len(cups)+1, 1000000+1))
        return part_2(cups, 10000000)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(INPUT, 1)}')
    print(f'Part 2 {main(INPUT, 2)}')
