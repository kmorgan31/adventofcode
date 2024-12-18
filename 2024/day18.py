#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

import math
import heapq


EXAMPLE = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

def get_surrounding_points(x, y):
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]


def explore(corrupted, size):
    seen = set()
    best = math.inf

    queue = []
    heapq.heappush(queue, (0, (0, 0))) # score, pos

    while queue:
        score, pos = heapq.heappop(queue)
        if pos == (size, size) and score < best:
            best = score
        if pos in seen:
            continue

        # visit
        seen.add(pos)
        for nx, ny in get_surrounding_points(pos[0], pos[1]):
            if 0 <= nx <= size and 0 <= ny <= size and (nx, ny) not in corrupted:
                # import pdb; pdb.set_trace()
                heapq.heappush(queue, (score+1, (nx, ny)))
    return best

def print_map(corrupted, size):
    for x in range(size):
        line = ""
        for y in range(size):
            if (x, y) in corrupted:
                line += "#"
            else:
                line += "."
        print(line)


def main(data, part, size, test):
    corrupted = []

    start = (0, 0)
    end = (size, size)

    lines = data.split("\n")
    for i, line in enumerate(lines):
        y, x = list(map(int, line.split(",")))
        corrupted.append((x, y))
    
    steps = 0
    while True:
        steps = explore(corrupted[:test], size)
        if part == 1:
            return steps
        if steps == math.inf:
            return corrupted[:test][-1][::-1]
        test += 1


if __name__ == '__main__':
    print(f'Part 1 {main(EXAMPLE, 1, 6, 12)}')
    print(f'Part 1 {main(data, 1, 70, 1024)}')
    print(f'Part 2 {main(EXAMPLE, 2, 6, 12)}')
    print(f'Part 2 {main(data, 2, 70, 2500)}')
