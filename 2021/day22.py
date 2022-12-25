#!/usr/bin/python

from aocd import lines


test_data_1 = [
    'on x=10..12,y=10..12,z=10..12',
    'on x=11..13,y=11..13,z=11..13',
    'off x=9..11,y=9..11,z=9..11',
    'on x=10..10,y=10..10,z=10..10'
]

test_data_2 = [
    'on x=-20..26,y=-36..17,z=-47..7',
    'on x=-20..33,y=-21..23,z=-26..28',
    'on x=-22..28,y=-29..23,z=-38..16',
    'on x=-46..7,y=-6..46,z=-50..-1',
    'on x=-49..1,y=-3..46,z=-24..28',
    'on x=2..47,y=-22..22,z=-23..27',
    'on x=-27..23,y=-28..26,z=-21..29',
    'on x=-39..5,y=-6..47,z=-3..44',
    'on x=-30..21,y=-8..43,z=-13..34',
    'on x=-22..26,y=-27..20,z=-29..19',
    'off x=-48..-32,y=26..41,z=-47..-37',
    'on x=-12..35,y=6..50,z=-50..-2',
    'off x=-48..-32,y=-32..-16,z=-15..-5',
    'on x=-18..26,y=-33..15,z=-7..46',
    'off x=-40..-22,y=-38..-28,z=23..41',
    'on x=-16..35,y=-41..10,z=-47..6',
    'off x=-32..-23,y=11..30,z=-14..3',
    'on x=-49..-5,y=-3..45,z=-29..18',
    'off x=18..30,y=-20..-8,z=-3..13',
    'on x=-41..9,y=-7..43,z=-33..15'
]


def get_cube_edges(ranges):
    def split_range(a):
        a = a.split("=")[1]
        return map(int, a.split(".."))

    x, y, z = ranges.split(",")
    x_min, x_max = split_range(x)
    y_min, y_max = split_range(y)
    z_min, z_max = split_range(z)

    return x_min, x_max, y_min, y_max, z_min, z_max


class Cube():

    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max

    def get_size(self):
        return (
            (self.x_max - self.x_min + 1) *
            (self.y_max - self.y_min + 1) *
            (self.z_max - self.z_min + 1)
        )


class Grid():

    def __init__(self):
        self.on_grid = []

    def cube_issubset(self, cube, new_cube):
        # returns if cube is encompassed by new_cube
        return (
            new_cube.x_min <= cube.x_min and new_cube.x_max >= cube.x_max and
            new_cube.y_min <= cube.y_min and new_cube.y_max >= cube.y_max and
            new_cube.z_min <= cube.z_min and new_cube.z_max >= cube.z_max
        )

    def cube_overlap(self, cube, new_cube):
        return (
            new_cube.x_min <= cube.x_max and new_cube.x_max >= cube.x_min and
            new_cube.y_min <= cube.y_max and new_cube.y_max >= cube.y_min and
            new_cube.z_min <= cube.z_max and new_cube.z_max >= cube.z_min
        )

    def process_new_cube(self, action, new_cube):
        # check grid against new ranges

        processing = True
        while processing:
            for idx in reversed(range(len(self.on_grid))):
                cube = self.on_grid[idx]

                # if new line ranges encompass existing cube, removing existing cube
                if self.cube_issubset(cube, new_cube):
                    del self.on_grid[idx]
                    break

                # if new_cube doesn't overlap with cube, continue
                if not self.cube_overlap(cube, new_cube):
                    continue

                # check all sides of intersection, if overlap, split cube
                
                if new_cube.x_min in range(cube.x_min+1, cube.x_max+1):
                    self.on_grid[idx] = Cube(
                        cube.x_min, new_cube.x_min-1, cube.y_min, cube.y_max, cube.z_min, cube.z_max
                    )
                    self.on_grid.append(Cube(
                        new_cube.x_min, cube.x_max, cube.y_min, cube.y_max, cube.z_min, cube.z_max
                    ))
                    break
                if new_cube.x_max in range(cube.x_min, cube.x_max):
                    self.on_grid[idx] = Cube(
                        new_cube.x_max+1, cube.x_max, cube.y_min, cube.y_max, cube.z_min, cube.z_max
                    )
                    self.on_grid.append(Cube(
                        cube.x_min, new_cube.x_max, cube.y_min, cube.y_max, cube.z_min, cube.z_max
                    ))
                    break

                if new_cube.y_min in range(cube.y_min+1, cube.y_max+1):
                    self.on_grid[idx] = Cube(
                        cube.x_min, cube.x_max, cube.y_min, new_cube.y_min-1, cube.z_min, cube.z_max
                    )
                    self.on_grid.append(Cube(
                        cube.x_min, cube.x_max, new_cube.y_min, cube.y_max, cube.z_min, cube.z_max
                    ))
                    break
                if new_cube.y_max in range(cube.y_min, cube.y_max):
                    self.on_grid[idx] = Cube(
                        cube.x_min, cube.x_max, new_cube.y_max+1, cube.y_max, cube.z_min, cube.z_max
                    )
                    self.on_grid.append(Cube(
                        cube.x_min, cube.x_max, cube.y_min, new_cube.y_max, cube.z_min, cube.z_max
                    ))
                    break

                if new_cube.z_min in range(cube.z_min+1, cube.z_max+1):
                    self.on_grid[idx] = Cube(
                        cube.x_min, cube.x_max, cube.y_min, cube.y_max, cube.z_min, new_cube.z_min-1
                    )
                    self.on_grid.append(Cube(
                        cube.x_min, cube.x_max, cube.y_min, cube.y_max, new_cube.z_min, cube.z_max
                    ))
                    break
                if new_cube.z_max in range(cube.z_min, cube.z_max):
                    self.on_grid[idx] = Cube(
                        cube.x_max, cube.x_max, cube.y_min, cube.y_max, new_cube.z_max+1, cube.z_max
                    )
                    self.on_grid.append(Cube(
                        cube.x_min, cube.x_max, cube.y_min, cube.y_max, cube.z_min, new_cube.z_max
                    ))
                    break
            else: processing = False

        if action == 'on':
            self.on_grid.append(new_cube)

    def total_on(self):
        total_on = 0
        for cube in self.on_grid:
            total_on = cube.get_size()
        return total_on


def main(data, part):

    if part == 1:
        grid = {}
        for line in data:
            action, ranges = line.split()
            cube = Cube(*get_cube_edges(ranges))
            if (cube.x_min < -50 or cube.x_max > 50 or
                    cube.y_min < -50 or cube.y_max > 50 or
                    cube.z_min < -50 or cube.z_max > 50):
                continue

            for x in range(cube.x_min, cube.x_max+1):
                for y in range(cube.y_min, cube.y_max+1):
                    for z in range(cube.z_min, cube.z_max+1):
                        grid[(x, y, z)] = action

        return list(grid.values()).count('on')

    elif part == 2:
        grid = Grid()

        for line in data:
            action, ranges = line.split()
            new_cube = Cube(*get_cube_edges(ranges))
            grid.process_new_cube(action, new_cube)

        return grid.total_on()


if __name__ == '__main__':

    # tests
    # print(f'Test Data: Part 1 {main(test_data_2, 1)}, Part 2 {main(test_data_2, 2)}')

    # question
    print(f'Day 21: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
