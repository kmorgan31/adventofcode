#!/usr/bin/python

from aocd import lines

import re


EXAMPLE = [
    "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
]

RACE_TIME = 2503


class Deer:

    def __init__(self, name, distance, time, rest):
        self.name = name
        self.distance = distance
        self.time = time
        self.rest = rest
        self.points = 0
        self.total_distance = 0

    def state(self, t):
        return (
            "fly" if t % (self.time + self.rest) < self.time
            else "rest"
        )

    def fly(self, t):
        # moves reindeer by t seconds
        self.total_distance += t * self.distance

    def add_point(self):
        self.points += 1


def part_1(data):
    max_distance = 0
    for line in data:
        deer = Deer(
            line.split()[0], *map(int, re.findall(r'\d+', line))
        )

        t = 0
        while t < RACE_TIME:
            # deer runs
            elapsed = min(deer.time, RACE_TIME-t)
            deer.fly(elapsed)

            t += elapsed
            if t < RACE_TIME:
                # deer rests
                elapsed = min(deer.rest, RACE_TIME-t)
                t += elapsed
        max_distance = max(max_distance, deer.total_distance)
    return max_distance


def part_2(data):
    # initialize deers
    deers = [
        Deer(line.split()[0], *map(int, re.findall(r'\d+', line)))
        for line in data
    ]

    for i in range(RACE_TIME):
        for deer in deers:
            if deer.state(i) == "fly":
                deer.fly(1)

        # award points
        max_distance = max([d.total_distance for d in deers])
        for d in deers:
            if d.total_distance == max_distance:
                d.add_point()

    return max([d.points for d in deers])


if __name__ == '__main__':
    # print(f'Example {part_1(EXAMPLE, 1000)}')
    print(f'Part 1 {part_1(lines, 2503)}')
    print(f'Part 2 {part_2(lines, 2503)}')
