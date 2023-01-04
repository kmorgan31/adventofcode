#!/usr/bin/python

from aocd import lines


def get_surrounding_points(pos):
    x, y = pos
    return [
        (x, y-1),
        (x, y+1),
        (x-1, y),
        (x+1, y)
    ]


def part_2(cave, pos):
    x, y = pos

    cave.starts = []

    # add walls
    cave.grid[(x, y)] = "#"
    for npos in ((x, y-1), (x+1, y), (x, y+1), (x-1, y)):
        cave.grid[npos] = "#"

    # add starts
    for npos in ((x+1, y-1), (x+1, y+1), (x-1, y+1), (x-1, y-1)):
        cave.starts.append(npos)
        cave.grid[npos] = "@"

    return cave


class KeyPath:

    def __init__(self, pos, steps, doors):
        self.pos = pos
        self.steps = steps
        self.doors = doors


class Cave:

    def __init__(self, data):
        self.grid = {}
        self.keys = {}
        self.doors = {}
        self.starts = []
        self.parse_data(data)

    def parse_data(self, data):
        for y, line in enumerate(data):
            for x, l in enumerate(line):
                pos = (x, y)
                self.grid[pos] = l

                if l == "@":
                    self.starts.append(pos)
                elif l.islower():
                    self.keys[l] = pos
                elif l.isupper():
                    self.doors[l.lower()] = pos

    def print_cave(self):
        min_x = min(x for x, _ in self.grid)
        min_y = min(y for _, y in self.grid)
        max_x = max(x for x, _ in self.grid)
        max_y = max(y for _, y in self.grid)

        grid_str = "\n".join(
            ("".join(self.grid[(x, y)] for x in range(min_x, max_x + 1)))
            for y in range(min_y, max_y + 1)
        )
        print(f"{grid_str}\n")

    def shortest_path(self, start, end):
        path = None
        doors = set()
        visited = set()

        q = [(0, start, set())]         # steps, curr_pos, doors
        while q:
            steps, pos, doors = q.pop(0)
            visited.add(pos)

            if pos == end:
                return steps, doors

            if self.grid[pos].isupper():
                doors = doors.copy()
                doors.add(self.grid[pos].lower())

            for sp in get_surrounding_points(pos):
                if self.grid.get(sp, "#") != "#" and sp not in visited:
                    q.append((steps+1, sp, doors))

        return path, doors

    def find_key_paths(self):
        key_paths = {k: {} for k in self.keys}

        for i, start in enumerate(self.starts):
            key_paths[f"@{i}"] = {}

            for k, kpos in self.keys.items():
                steps, doors = self.shortest_path(start, kpos)
                if steps is not None:
                    key_paths[f"@{i}"][k] = KeyPath(kpos, steps, doors)

                for dest, dpos in self.keys.items():
                    if dest != k and k not in key_paths[dest]:
                        steps, doors = self.shortest_path(kpos, dpos)
                        if steps is not None:
                            key_paths[k][dest] = KeyPath(dpos, steps, doors)
                            key_paths[dest][k] = KeyPath(kpos, steps, doors)

        return key_paths

    def find_keys(
        self, key_paths, bots, bot_id="@0", key="@0", found=None, cache={}
    ):
        if found is None:
            found = set(x for x in key_paths if x[0] == "@")

        bots[bot_id] = key

        if len(found) == len(key_paths):
            return 0, [key]

        cache_key = (
            "".join(sorted(bots.values())) +
            "".join(sorted(set(key_paths.keys()) - found))
        )
        if cache_key not in cache:
            paths = []

            for bot, bot_key in bots.items():
                for k in key_paths[bot]:
                    if k in found:
                        continue
                    elif key_paths[bot_key][k].doors - found:
                        continue

                    ksteps, kpaths = self.find_keys(
                        key_paths,
                        bots.copy(),
                        bot,
                        k,
                        found | {k},
                        cache
                    )
                    paths.append(
                        (key_paths[bot_key][k].steps + ksteps, [key] + kpaths)
                    )
            cache[cache_key] = min(paths)

        return cache[cache_key]


def main(data, part=None):

    cave = Cave(data)

    if part == 2:
        cave = part_2(cave, cave.starts.pop())

    keypaths = cave.find_key_paths()
    steps, keypath = cave.find_keys(
        keypaths,
        {f"@{i}": f"@{i}" for i in range(len(cave.starts))}
    )
    return steps


if __name__ == '__main__':
    # print(f'Part 1 {part_2(EXAMPLE[0])}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
