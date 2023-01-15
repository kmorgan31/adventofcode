#!/usr/bin/python

from aocd import lines

from copy import deepcopy
from itertools import combinations


EXAMPLE = [
    ["HM", "LM"],
    ["HG"],
    ["LG"],
    []
]

"""
A: promethium
B: cobalt
C: curium
D: ruthenium
E: plutonium
"""
INPUT = [
    ["AG", "AM"],
    ["BG", "CG", "DG", "EG"],
    ["BM", "CM", "DM", "EM"],
    []
]


def check_level_parts(parts):
    ms = [part for part in parts if "M" in parts]
    gs = [part for part in parts if "G" in parts]

    unmatched_ms = set(ms) - set(gs)
    unmatched_gs = set(gs) - set(ms)

    if len(unmatched_ms) > 0 and len(gs) > 0 and len(unmatched_gs) == 0:
        # extra ms after matching GMs; pair will fry unmatched Ms
        return False
    if len(unmatched_ms) > 0 and len(unmatched_gs) > 0:
        # unmatched Gs and Ms
        return False
    return True


def check_valid_move(floors, elevel, n_elevel, econtents):
    # can the elevator move the elevator contents (1 or 2)
    # from floor `elevel` to floor `n_elevel`?

    # get parts on n_elevel
    nelevel_parts = list(floors[n_elevel])

    # add parts to list
    nelevel_parts += econtents

    # check that level is valid
    if not check_level_parts(nelevel_parts):
        return False

    elevel_parts = list(floors[elevel])
    # ensure the parts being moved were coming from the correct floor
    if any(part not in elevel_parts for part in econtents):
        return False

    # remove parts from current floor
    for part in econtents:
        elevel_parts.remove(part)

    # ensure removing part doesn't cause an unmatched M
    if not check_level_parts(elevel_parts):
        return False

    return True


def make_move(floors, elevel, n_elevel, econtents, steps):
    nfloors = deepcopy(floors)

    # check that move is valid
    if not check_valid_move(nfloors, elevel, n_elevel, econtents):
        return False

    # do move
    for p in econtents:
        nfloors[n_elevel].append(p)
        nfloors[elevel].remove(p)

    # sort nlevel part
    nfloors[n_elevel] = sorted(nfloors[n_elevel])

    # track state of nelevel + nfloors
    floors_state = [
        n_elevel,       # elevator new level
        [0, 0, 0],      # unmatched Ms, matched Ms, unmatched Gs
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for i, floor in enumerate(nfloors):
        for part in floor:
            if part[1] == "M":
                if part[0] + "G" not in floor:
                    floors_state[i+1][0] += 1
                else:
                    floors_state[i+1][2] += 1
            else:
                if part[0] + "M" not in floor:
                    floors_state[i+1][1] += 1

    return [nfloors, n_elevel, floors_state, steps+1]


def print_floors(floors, steps):
    print(f"Steps: {steps}")
    for f in floors[::-1]:
        print(f)
    print()


def main(floors, total_num_parts):
    seen = []
    moves = []
    print_floors(floors, 0)

    # do initial step - moving items from F1 to F2, either in singles or in pairs
    for part in floors[0]:
        move = make_move(floors, 0, 1, [part], 0)
        if move is not False and move[2] not in seen:
            moves.append(move)
            seen.append(move[2])

    for p1, p2 in combinations(floors[0], 2):
        move = make_move(floors, 0, 1, [p1, p2], 0)
        if move is not False and move[2] not in seen:
            moves.append(move)
            seen.append(move[2])

    while moves:
        floors, elevel, state, steps = moves.pop(0)
        # print_floors(floors, steps)
        if len(floors[3]) == total_num_parts:
            # top floor has all parts
            return steps

        for p1 in floors[elevel]:
            if elevel < 3:
                # move single parts up
                move = make_move(floors, elevel, elevel+1, [p1], steps)
                if move is not False and move[2] not in seen:
                    moves.append(move)
                    seen.append(move[2])

                # move pairs of parts up
                for p1, p2 in combinations(floors[elevel], 2):
                    move = make_move(floors, elevel, elevel+1, [p1, p2], steps)
                    if move is not False and move[2] not in seen:
                        moves.append(move)
                        seen.append(move[2])

            if elevel > 1 and all(len(floors[x]) == 0 for x in range(1, elevel)):
                # lower levels are all empty, don't move anything down
                continue

            if elevel > 0:
                # move single parts down
                move = make_move(floors, elevel, elevel-1, [p1], steps)
                if move is not False and move[2] not in seen:
                    moves.append(move)
                    seen.append(move[2])

                # move pairs of parts down
                for p1, p2 in combinations(floors[elevel], 2):
                    move = make_move(floors, elevel, elevel-1, [p1, p2], steps)
                    if move is not False and move[2] not in seen:
                        moves.append(move)
                        seen.append(move[2])


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 4)}')
    print(f'Part 1 {main(INPUT, 10)}')
    # print(f'Part 2 {main(lines, 2)}')
