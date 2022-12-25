#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]

char_to_height = {
    'S': 'a',
    'E': 'z'
}


class Grid():
    # Graph
    def __init__(self, data):
        self.grid = []
        self.grid_height = len(data)
        self.grid_width = len(data[0])

        self.visited = []
        self.unvisited = []

    def create_grid(self, data):
        for i in range(self.grid_height):
            line = data[i]
            for j in range(self.grid_width):
                self.unvisited.append((i, j))
            self.grid.append(line)

    def set_start_node(self):
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                if self.grid[i][j] == "E":
                    self.start = (i, j)

    def set_end_nodes(self, end):
        self.end_nodes = []
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                if self.grid[i][j] in end:
                    self.end_nodes.append((i, j))

    def calculate_distance(self):
        self.distance = dict(
            zip(self.unvisited, [999]*(self.grid_height*self.grid_width))
        )
        self.distance[self.start] = 0

    def get_surrounding_nodes(self, node):
        x, y = node
        surrounding_nodes = [
            (x-1, y),       # left
            (x, y-1),       # up
            (x, y+1),       # down
            (x+1, y),       # right
        ]

        res = []
        for i, j in surrounding_nodes:
            if not (0 <= i <= self.grid_height-1 and 0 <= j <= self.grid_width-1):
                continue
            if (
                ord(char_to_height.get(self.grid[i][j], self.grid[i][j])) -
                ord(char_to_height.get(self.grid[x][y], self.grid[x][y]))
            ) < -1:
                continue
            res.append((i, j))
        return res

    def visit(self, curr_node):
        for node in self.get_surrounding_nodes(curr_node):
            if node not in self.visited:
                if self.distance[curr_node] + 1 < self.distance[node]:
                    self.distance[node] = self.distance[curr_node] + 1
        self.unvisited.remove(curr_node)
        self.visited.append(curr_node)


def main(data, end="S"):
    grid = Grid(data)

    grid.create_grid(data)
    grid.set_start_node()
    grid.set_end_nodes(end)

    grid.calculate_distance()
    while not set(grid.end_nodes).issubset(set(grid.visited)):
        curr_node = min(grid.unvisited, key=grid.distance.get)
        grid.visit(curr_node)

    return grid.distance[min(grid.end_nodes, key=grid.distance.get)]


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE, end=["a","S"])}')
    print(f'Part 1 {main(lines, end=["S"])}')
    print(f'Part 2 {main(lines, end=["a", "S"])}')
