#!/usr/bin/python

# from aocd import lines

# import re

from copy import deepcopy
from itertools import combinations
# from collections import defaultdict

EXAMPLE = {
    0: {
        "G": [],
        "M": ["H", "L"]
    },
    1: {
        "G": ["H"],
        "M": [],
    },
    2: {
        "G": ["L"],
        "M": [],
    },
    3: {
        "G": [],
        "M": []
    }
}

INPUT = {}


def print_state(state, e=None):
    for i in range(3, -1, -1):
        line = [f"F{i}"]
        if e == i:
            line.append("E")
        else:
            line.append(".")

        for g in state[i]["G"]:
            line.append(f"{g}G")
        for m in state[i]["M"]:
            line.append(f"{m}M")
        print(' '.join(line))
    print()


def next_levels(e):
    # gives possible next levels for e
    next_levels = {e+1, e-1}
    return {x for x in next_levels if 0 <= x <= 3}


def check_validity(state):
    # only one XOR of M and G has entries, or neither, per level
    for level in range(4):
        gs = set(state[level]["G"]) - set(state[level]["M"])
        ms = set(state[level]["M"]) - set(state[level]["G"])

        if len(gs) == 0 and len(ms) == 0:
            # none unmatched
            continue
        if len(ms) > 0 and len(state[level]["G"]) == 0:
            # only Ms
            continue
        if len(gs) > 0 and len(state[level]["M"]) == 0:
            # only Gs
            continue
        if len(gs) > 0 and len(ms) == 0:
            # we can have unmatched Gs as long as all Ms are matched
            continue
        if len(gs) > 0 and len(ms) > 0 and gs != ms:
            # unmatched Gs and Ms
            return False
        if len(gs) == 0 and len(ms) > 0:
            # extra ms will be vaporized by G
            return False
    return True


def empty_elevator(state, contents):
    # empty elevator
    nstate = deepcopy(state)
    for level, mg, t in contents:
        # find where mg used to be and remove it
        for nl in next_levels(level):
            if mg in nstate[nl][t]:
                nstate[nl][t].remove(mg)

        # add mg to level
        nstate[level][t].append(mg)
    return nstate


def main(data, num_parts=None):
    elevator = (0, [])

    previous_states = []
    next_states = [(elevator, data, 0)]  # elevator (level, contents), state, steps
    while True:
        elevator, state, steps = next_states.pop(0)
        if len(state[3]) == num_parts:
            return steps

        elevel, econtents = elevator
        if econtents:
            nstate = empty_elevator(state, econtents)
            #  check if state if valid and hasn't been done before, if not, abort state
            if not check_validity(nstate) or nstate in previous_states:
                # don't wanna keep going back and forth
                continue
            else:
                state = nstate

        previous_states.append(deepcopy(state))
        print_state(state, e=elevel)
        # import pdb; pdb.set_trace()

        # get next levels from current level
        nlevels = next_levels(elevator[0])

        # determine what we can take
        # 1. we can take M if corresponding G is on next_level
        possible_moves = []
        for nl in nlevels:
            for m in state[elevel]["M"]:
                if m in state[nl]["G"]:
                    # matching generator; possible to move
                    possible_moves.append((nl, m, "M"))

        # 2. we can take G if M in next_level are matched, or unmatched M will be matched with G
        for nl in nlevels:
            for g in state[elevel]["G"]:
                unmatched = set(state[nl]["M"]) - set(state[nl]["G"])
                if len(unmatched) == 0 or (len(unmatched) == 1 and unmatched.pop() == g):
                    possible_moves.append((nl, g, "G"))

        if len(possible_moves) == 1:
            pm = possible_moves.pop()
            next_states.append(((pm[0], [pm]), deepcopy(state), steps+1))
        else:
            p_next_states = set()
            for p1, p2 in combinations(possible_moves, 2):
                if (p1[0] == p2[0] and p1[1] != p2[1] and p1[2] == p2[2]
                        and (p1, p2) not in p_next_states):
                    # both generators/mchips going to the same floor, they can go together
                    next_states.append(((p1[0], [p1, p2]), deepcopy(state), steps+1))
                    p_next_states.add((p1, p2))
                else:
                    # generators and mchips don't match or going to different level;
                    # they have to go separately
                    if p1 not in p_next_states:
                        next_states.append(((p1[0], [p1]), deepcopy(state), steps+1))
                        p_next_states.add(p1)
                    if p2 not in p_next_states:
                        next_states.append(((p2[0], [p2]), deepcopy(state), steps+1))
                        p_next_states.add(p2)

        # 4. we can take a pair of G and M
        # 4b. we can break up a pair that's already been made
        # if that leads to an invalid state, it will be cleaned up in the next iteration
        p_next_states = set()
        for m in state[elevel]["M"]:
            if m in state[elevel]["G"]:
                for nl in nlevels:
                    if ((nl, m, "G"), (nl, m, "M")) not in p_next_states:
                        next_states.append(((nl, [(nl, m, "G"), (nl, m, "M")]), state.copy(), steps+1))
                        p_next_states.add(((nl, m, "G"), (nl, m, "M")))
                    if ((nl, m, "G")) not in p_next_states:
                        next_states.append(((nl, [(nl, m, "G")]), state.copy(), steps+1))
                        p_next_states.add((nl, m, "G"))
                    if ((nl, m, "M")) not in p_next_states:
                        next_states.append(((nl, [(nl, m, "M")]), state.copy(), steps+1))
                        p_next_states.add((nl, m, "M"))

        # import pdb; pdb.set_trace()


if __name__ == '__main__':
    print(f'EXAMPLE {main(EXAMPLE, 4)}')
    # print(f'Part 1 {main(INPUT, 10)}')
    # print(f'Part 2 {main(lines, 2)}')
