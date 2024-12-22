#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data


EXAMPLE = """029A
980A
179A
456A
379A"""


def main(data, n_robots):
    total = 0
    for code in data.splitlines():
        total += complexity(code, n_robots) * int(code[:-1])
    return total

def complexity(code, n_robots):
    # directional keyboard
    KEY_COORDS = {c: (x, y) for y, row in enumerate([" ^A", "<v>"]) for x, c in enumerate(row)}
    
    distances = {(0, ki, kf): 1 for ki in KEY_COORDS for kf in KEY_COORDS} # score, start, end
    paths = lambda l, ks: sum(distances[(l, ki, kf)] for ki, kf in zip('A' + ks, ks))

    for layer in range(1, n_robots+1):
        if layer == n_robots:
            # numerical keyboard
            KEY_COORDS = {c: (x, y) for y, row in enumerate(["789", "456", "123", " 0A"]) for x, c in enumerate(row)}
        for ki, (xi, yi) in KEY_COORDS.items():
            for kf, (xf, yf) in KEY_COORDS.items():
                move_horizontal = ('>' if xf > xi else '<') * abs(xf - xi)
                move_vertical = ('^' if yf < yi else 'v') * abs(yf - yi)
                fewest_horizontal_first = paths(layer-1, move_horizontal + move_vertical + 'A') if (xf, yi) != KEY_COORDS[' '] else float('inf')
                fewest_vertical_first = paths(layer-1, move_vertical + move_horizontal + 'A') if (xi, yf) != KEY_COORDS[' '] else float('inf')
                distances[(layer, ki, kf)] = min(fewest_horizontal_first, fewest_vertical_first)
    return paths(layer, code)


if __name__ == '__main__':
    print(f'Part 1 {main(EXAMPLE, 3)}')
    print(f'Part 1 {main(data, 3)}')
    print(f'Part 2 {main(data, 26)}')
