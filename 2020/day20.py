#!/usr/bin/python

from aocd import lines

import re
from collections import defaultdict
from math import prod


# OPP_DIR = {
#     "top": "bottom",
#     "bottom": "top",
#     "right": "left",
#     "left": "right"
# }

EXAMPLE = [
    "Tile 2311:",
    "..##.#..#.",
    "##..#.....",
    "#...##..#.",
    "####.#...#",
    "##.##.###.",
    "##...#.###",
    ".#.#.#..##",
    "..#....#..",
    "###...#.#.",
    "..###..###",
    "",
    "Tile 1951:",
    "#.##...##.",
    "#.####...#",
    ".....#..##",
    "#...######",
    ".##.#....#",
    ".###.#####",
    "###.##.##.",
    ".###....#.",
    "..#.#..#.#",
    "#...##.#..",
    "",
    "Tile 1171:",
    "####...##.",
    "#..##.#..#",
    "##.#..#.#.",
    ".###.####.",
    "..###.####",
    ".##....##.",
    ".#...####.",
    "#.##.####.",
    "####..#...",
    ".....##...",
    "",
    "Tile 1427:",
    "###.##.#..",
    ".#..#.##..",
    ".#.##.#..#",
    "#.#.#.##.#",
    "....#...##",
    "...##..##.",
    "...#.#####",
    ".#.####.#.",
    "..#..###.#",
    "..##.#..#.",
    "",
    "Tile 1489:",
    "##.#.#....",
    "..##...#..",
    ".##..##...",
    "..#...#...",
    "#####...#.",
    "#..#.#.#.#",
    "...#.#.#..",
    "##.#...##.",
    "..##.##.##",
    "###.##.#..",
    "",
    "Tile 2473:",
    "#....####.",
    "#..#.##...",
    "#.##..#...",
    "######.#.#",
    ".#...#.#.#",
    ".#########",
    ".###.#..#.",
    "########.#",
    "##...##.#.",
    "..###.#.#.",
    "",
    "Tile 2971:",
    "..#.#....#",
    "#...###...",
    "#.#.###...",
    "##.##..#..",
    ".#####..##",
    ".#..####.#",
    "#..#.#..#.",
    "..####.###",
    "..#.#.###.",
    "...#.#.#.#",
    "",
    "Tile 2729:",
    "...#.#.#.#",
    "####.#....",
    "..#.#.....",
    "....#..#.#",
    ".##..##.#.",
    ".#.####...",
    "####.#.#..",
    "##.####...",
    "##..#.##..",
    "#.##...##.",
    "",
    "Tile 3079:",
    "#.#.#####.",
    ".#..######",
    "..#.......",
    "######....",
    "####.#..#.",
    ".#...#.##.",
    "#.#####.##",
    "..#.###...",
    "..#.......",
    "..#.###..."
]


class Tile:

    def __init__(self, tile_id, grid):
        self.tile_id = tile_id
        self.grid = grid
        self.neighbours = {}
        self.get_edges()

    def get_edges(self):
        self.edges = {
            "top": ''.join([self.grid[0][y] for y in range(10)]),
            "bottom": ''.join([self.grid[9][y] for y in range(10)]),
            "right": ''.join([self.grid[x][9] for x in range(10)]),
            "left": ''.join([self.grid[x][0] for x in range(10)])
        }


def parse_data(data):
    tile_id, tile = None, []

    tiles = {}
    for line in data:

        if not line:
            # create tile
            tiles[tile_id] = Tile(tile_id, tile)

            # reset
            tile_id, tile = None, []
            continue

        if "Tile" in line:
            tile_id = int(re.findall(r'\d+', line)[0])
        else:
            tile.append(list(line))
    if tile:
        tiles[tile_id] = Tile(tile_id, tile)
    return tiles


def get_neighbours(tiles_edges, tile):
    neighbours = set()
    edges = list(tile.edges.items()) + [edge[::-1] for edge in tile.edges.items()]
    for _, e in edges:
        neighbours.update(tiles_edges[e])
    return neighbours


def main(data, part=None):
    tiles = parse_data(data)

    tiles_edges = defaultdict(set)
    for tile in tiles.values():
        for k, edge in tile.edges.items():
            tiles_edges[edge].add(tile.tile_id)
            tiles_edges[edge[::-1]].add(tile.tile_id)

    if part == 1:
        # find the tiles that only join to 2 other tiles
        corners = []
        for tile in tiles.values():
            if len(get_neighbours(tiles_edges, tile) - {tile.tile_id}) == 2:
                corners.append(tile.tile_id)
        return prod(corners)

#     elif part == 2:
        

# def part_2(tiles_edges, tiles):
#     visited = set()

#     def dfs(pos, last=None):
#         visited.add(pos)

#         if not last:
#             pos = (0, 0)
#         else:
#             pos = get_position()

    
#     dfs(tiles[0].tile_id)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    # print(f'Part 2 {main(lines, 2)}')
