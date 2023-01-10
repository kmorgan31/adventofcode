#!/usr/bin/python

EXAMPLE = [
    "cpy 41 a",
    "inc a",
    "inc a",
    "dec a",
    "jnz a 2",
    "dec a",
]

INPUT = 1358


def get_surrounding_points(pos):
    x, y = pos
    return {
        (i,j) for i, j in {
            (x,y+1),
            (x,y-1),
            (x+1,y),
            (x-1,y)
        } if i >= 0 and j >= 0
    }


def is_space(pos):
    x, y = pos
    ans = (x*x + 3*x + 2*x*y + y + y*y) + INPUT
    return bin(ans)[2:].count('1') % 2 == 0


def main(part=None):
    visited = {}

    to_visit = [(1, 1, 0)]
    while to_visit:
        x, y, steps = to_visit.pop(0)
        visited[(x,y)] = steps

        for sp in get_surrounding_points((x,y)):
            if is_space(sp):
                if sp not in visited or visited[sp] > steps+1:
                    to_visit.append((sp[0], sp[1], steps+1))

    if part == 1:
        return visited[(31, 39)]
    if part == 2:
        return sum(True for x in visited if visited[x] <= 50)


if __name__ == '__main__':
    print(f'Part 1 {main(1)}')
    print(f'Part 2 {main(2)}')
