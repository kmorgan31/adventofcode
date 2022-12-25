#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
    "Valve HH has flow rate=22; tunnel leads to valve GG",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
    "Valve JJ has flow rate=21; tunnel leads to valve II"
]


class Graph:

    def __init__(self, data):
        self.valves = []
        self.weights = {}
        self.edges = {}

        self.draw_graph(data)

    def draw_graph(self, data):
        for line in data:
            line = line.split()
            source = line[1]
            weight = int(line[4].split("=")[1].replace(";", ""))
            dests = list(map(lambda x: x.replace(",", ""), line[9:]))

            if weight:
                self.weights[source] = weight
            self.edges[source] = dests

    def get_dist(self, start):
        seen = {start}
        dist = {start: 0}
        
        q = [start]
        while q and any(v not in dist for v in self.weights):
            v = q.pop(0)
            for e in self.edges[v]:
                if e not in seen:
                    seen.add(e)
                    dist[e] = dist[v] + 1
                    q.append(e)
        return dist

    def get_paths(self, dist, mins, start="AA"):
        pressures = []
        paths = []

        stack = [(mins, 0, [start])]
        while stack:
            mins, pressure, path = stack.pop()
            cur_v = path[-1]

            new = []
            for next_v, d in dist[cur_v].items():
                if d > mins - 2 or next_v in path:
                    continue

                new_mins = mins - d - 1
                new_pressure = pressure + self.weights[next_v] * new_mins
                new.append((new_mins, new_pressure, path+[next_v]))

            if new:
                # add to stack
                stack.extend(new)
            else:
                pressures.append(pressure)
                paths.append(path[1:])
        return pressures, paths


def main(data, part=None):
    g = Graph(data)

    dist = {}
    # find the distance between a starting point and
    # all other points that release pressure
    for start in ("AA", *g.weights):
        dist[start] = {}
        d = g.get_dist(start)
        for v in g.weights:
            if v != start and v in d:
                dist[start][v] = d[v]

    if part == 1:
        # find the pressure released within 30mins along all paths from "AA"
        pressures, _ = g.get_paths(dist, 30)
        return max(pressures)

    if part == 2:
        # analyze pressures, paths
        # starting with ones that could release the most pressure
        x = list(zip(*g.get_paths(dist, 26)))
        p, paths = zip(*sorted(x, reverse=True))

        # find the point where the path doesn't overlap with the first path
        # which releases the most pressure
        x, y = 0, 1
        while y < len(paths) and any(i in paths[x] for i in paths[y]):
            y += 1

        pressure = p[x] + p[y]  # least pressure we could release
        for i in range(1, y):
            for j in range(i+1, y+1):
                # ignore overlapping paths
                if any(x in paths[j] for x in paths[i]):
                    continue
                pressure = max(pressure, p[i]+p[j])
        return pressure


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
