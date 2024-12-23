#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

import heapq

from collections import defaultdict


EXAMPLE = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


class Graph:

    def __init__(self, data):
        lines = data.splitlines()
        self.parse_edges(lines)

    def parse_edges(self, lines):
        self.edges = defaultdict(list)
        for line in lines:
            x, y = line.split("-")
            self.edges[x].append(y)
            self.edges[y].append(x)

    def get_triangles(self, start):
        queue = []
        heapq.heappush(queue, (0, start, [start]))

        results = []
        while queue:
            score, node, path = heapq.heappop(queue)
            if score == 3:
                if node == start:
                    results.append(tuple(path[:-1]))
                continue

            # visit
            for nnode in self.edges[node]:
                if nnode == start or nnode not in path:
                    heapq.heappush(queue, (score+1, nnode, path + [nnode]))
        return results

    def check_chain(self, chain):
        # check that all nodes are joined to each other
        found = True
        while chain:
            node = chain.pop()
            if set(chain) - set(self.edges[node]) != set():
                found = False
                break
        return found


def main(data, part):
    graph = Graph(data)

    t_count = 0
    triangles = []
    for node in graph.edges.keys():
        results = graph.get_triangles(node)
        for result in results:
            if set(result) not in triangles:
                triangles.append(set(result))
                if any(r.startswith("t") for r in result):
                    t_count += 1
    if part == 1:
        return t_count
    
    longest = []
    for i, t in enumerate(triangles):
        if not graph.check_chain(t.copy()):
            continue

        # add nodes not already in triangle
        rem_nodes = set(graph.edges.keys()) - t

        nchain = list(t)
        while rem_nodes:
            node = rem_nodes.pop()

            if not graph.check_chain(nchain + [node]):
                continue

            nchain += [node]
            if len(nchain) > len(longest):
                longest = nchain

    return ','.join(sorted(longest))


if __name__ == '__main__':
    print(f'Part 1 {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(data, 1)}')
    print(f'Part 2 {main(EXAMPLE, 2)}')
    print(f'Part 2 {main(data, 2)}')
