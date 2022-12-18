#!/usr/bin/python

from aocd import lines

from itertools import combinations


EXAMPLE = [
    "2,2,2",
    "1,2,2",
    "3,2,2",
    "2,1,2",
    "2,3,2",
    "2,2,1",
    "2,2,3",
    "2,2,4",
    "2,2,6",
    "1,2,5",
    "3,2,5",
    "2,1,5",
    "2,3,5"
]


def are_touching(cube_a, cube_b):
    return sum(abs(a-b) for a, b in zip(cube_a, cube_b)) == 1


def surrounding_cubes(cube, min_xyz, max_xyz):
    x, y, z = cube
    surrounding_cubes = [
        (x+1, y, z),
        (x-1, y, z),
        (x, y+1, z),
        (x, y-1, z),
        (x, y, z+1),
        (x, y, z-1)
    ]

    return [
        (x, y, z) for x, y, z in surrounding_cubes
        if (
            min_xyz <= x <= max_xyz and
            min_xyz <= y <= max_xyz and
            min_xyz <= z <= max_xyz
        )
    ]


def main(data, part=None):
    cubes = []
    for line in data:
        cubes.append(tuple(map(int, line.split(","))))

    if part == 1:
        total_sides = 6 * len(cubes)
        for cube_a, cube_b in combinations(cubes, 2):
            if are_touching(cube_a, cube_b):
                total_sides -= 2
        return total_sides

    if part == 2:
        total_sides = 0
        cubes = set(cubes)

        min_xyz = min(min(cube) for cube in cubes) - 1
        max_xyz = max(max(cube) for cube in cubes) + 1

        nodes = [(min_xyz, min_xyz, min_xyz)]
        visited = {nodes[0]}
        while nodes:
            curr_cube = nodes.pop()
            for next_cube in surrounding_cubes(curr_cube, min_xyz, max_xyz):
                if next_cube in visited:
                    continue
                if next_cube in cubes:
                    total_sides += 1
                else:
                    visited.add(next_cube)
                    nodes.append(next_cube)
        return total_sides


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
