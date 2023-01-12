#!/usr/bin/python

from aocd import lines


def main(data, num_players):
    players = []
    for i in range(num_players):
        players.append((0, 0))

    curr_player = 0
    visited = set([(0,0)])
    for char in data:
        x, y = players[curr_player % len(players)]
        if char == ">": y += 1
        if char == "v": x += 1
        if char == "<": y -= 1
        if char == "^": x -= 1

        # visit pos, update player pos
        visited.add((x,y))
        players[curr_player % len(players)] = (x,y)
        curr_player += 1

    return len(visited)


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines[0], 1)}')
    print(f'Part 2 {main(lines[0], 2)}')
