#!/usr/bin/python

from aocd import lines

from collections import defaultdict

EXAMPLE = [
    "16",
    "10",
    "15",
    "5",
    "1",
    "11",
    "7",
    "19",
    "6",
    "12",
    "4"
]


def part_1(adapters):
    num_differences = defaultdict(int)

    for i in range(len(adapters)-1):
        num_differences[adapters[i+1] - adapters[i]] += 1
    return num_differences[1] * num_differences[3]


def dfs(pos, neighbours, visited):
    if pos in visited:
        return visited[pos]
    elif neighbours[pos]:
        visited[pos] = sum(dfs(n, neighbours, visited) for n in neighbours[pos])
        return visited[pos]
    else:
        return 1


def part_2(adapters):
    neighbours = dict([
        (x, [y for y in range(x+1, x+4) if y in adapters]) for x in adapters
    ])

    return dfs(0, neighbours, {})


def main(data, part=None):
    adapters = list(map(int, data))
    device_adapter = max(adapters) + 3
    all_adapters = [0] + sorted(adapters) + [device_adapter]

    if part == 1:
        return part_1(all_adapters)
    elif part == 2:
        return part_2(all_adapters)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
