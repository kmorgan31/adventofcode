#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.",
    "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."
]


ORE_TYPES = ["ore", "clay", "obsidian", "geode"]


class Blueprint:

    def __init__(self, robots):
        self.robots = robots


def get_blueprints(data):
    blueprints = []

    for line in data:
        blueprint_num, line = line.split(":")
        line = line.split(".")
        blueprints.append(
            Blueprint({
                "ore": (int(line[0].split()[4]), 0, 0, 0),
                "clay": (int(line[1].split()[4]), 0, 0, 0),
                "obsidian": (int(line[2].split()[4]), int(line[2].split()[7]), 0, 0),
                "geode": (int(line[3].split()[4]), 0, int(line[3].split()[7]), 0)
            })
        )
    return blueprints


def build_robots(bp, pack, robots):
    results = []
    for i, x in enumerate(list(reversed(ORE_TYPES))):

        # check if you can build any robots
        robot_cost = bp.robots[x]
        g_idx = len(ORE_TYPES)-i-1
        if all(pack[j] >= robot_cost[j] for j in range(len(ORE_TYPES))):
            new_robots = list(robots)
            new_robots[g_idx] += 1
            new_robots = tuple(new_robots)

            new_pack = tuple([pack[j] - robot_cost[j] for j in range(len(ORE_TYPES))])

            results.append((new_pack, new_robots))
    return results


def mine_ores(p, r):
    return tuple([p[i] + r[i] for i in range(len(ORE_TYPES))])


def state_quality(state):
    mins, pack, mined, robots = state
    return sum(mined[i] * 10**i for i in range(len(ORE_TYPES)))


def mine_bfs(blueprint, end):
    depth = 0
    max_geodes = 0

    # start state: mins, pack, mined, robots
    pq = [(0, (0,0,0,0), (0,0,0,0), (1,0,0,0))]
    while pq:
        # take the first item in the queue
        mins, pack, mined, robots = pq.pop(0)

        if mins > depth:
            pq.sort(key=state_quality, reverse=True)
            pq = pq[:30000]
            depth = mins

        if mins == end:
            max_geodes = max(mined[3], max_geodes)
            continue

        # we could build no robots
        np = mine_ores(pack, robots)
        nm = mine_ores(mined, robots)
        pq.append((mins+1, np, nm, robots))

        # determine what robots I could build
        new_states = build_robots(blueprint, pack, robots)
        for sp, sr in new_states:
            np = mine_ores(sp, robots)
            pq.append((mins+1, np, nm, sr))

    return max_geodes


def main(data, part, mins):
    blueprints = get_blueprints(data)

    if part == 1:
        total_quality_level = 0
        for i, bp in enumerate(blueprints):
            geodes = mine_bfs(bp, mins)
            total_quality_level += (i+1) * geodes
        return total_quality_level
    elif part == 2:
        total_quality_level = 1
        for i, bp in enumerate(blueprints):
            geodes = mine_bfs(bp, mins)
            print(f"Blueprint {i+1}: {geodes}")
            total_quality_level *= geodes
        return total_quality_level


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2, 32)}')
    print(f'Part 1 {main(lines, 1, 24)}')
    print(f'Part 2 {main(lines[:3], 2, 32)}')
