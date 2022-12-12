#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "addx 15",
    "addx -11",
    "addx 6",
    "addx -3",
    "addx 5",
    "addx -1",
    "addx -8",
    "addx 13",
    "addx 4",
    "noop",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx 5",
    "addx -1",
    "addx -35",
    "addx 1",
    "addx 24",
    "addx -19",
    "addx 1",
    "addx 16",
    "addx -11",
    "noop",
    "noop",
    "addx 21",
    "addx -15",
    "noop",
    "noop",
    "addx -3",
    "addx 9",
    "addx 1",
    "addx -3",
    "addx 8",
    "addx 1",
    "addx 5",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx -36",
    "noop",
    "addx 1",
    "addx 7",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "addx 6",
    "noop",
    "noop",
    "noop",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx 7",
    "addx 1",
    "noop",
    "addx -13",
    "addx 13",
    "addx 7",
    "noop",
    "addx 1",
    "addx -33",
    "noop",
    "noop",
    "noop",
    "addx 2",
    "noop",
    "noop",
    "noop",
    "addx 8",
    "noop",
    "addx -1",
    "addx 2",
    "addx 1",
    "noop",
    "addx 17",
    "addx -9",
    "addx 1",
    "addx 1",
    "addx -3",
    "addx 11",
    "noop",
    "noop",
    "addx 1",
    "noop",
    "addx 1",
    "noop",
    "noop",
    "addx -13",
    "addx -19",
    "addx 1",
    "addx 3",
    "addx 26",
    "addx -30",
    "addx 12",
    "addx -1",
    "addx 3",
    "addx 1",
    "noop",
    "noop",
    "noop",
    "addx -9",
    "addx 18",
    "addx 1",
    "addx 2",
    "noop",
    "noop",
    "addx 9",
    "noop",
    "noop",
    "noop",
    "addx -1",
    "addx 2",
    "addx -37",
    "addx 1",
    "addx 3",
    "noop",
    "addx 15",
    "addx -21",
    "addx 22",
    "addx -6",
    "addx 1",
    "noop",
    "addx 2",
    "addx 1",
    "noop",
    "addx -10",
    "noop",
    "noop",
    "addx 20",
    "addx 1",
    "addx 2",
    "addx 2",
    "addx -6",
    "addx -11",
    "noop",
    "noop",
    "noop"
]


class Circuit:

    def __init__(self, cycle=1):
        self.x = 1
        self.cycle = cycle
        self.queue = []
        self.crt = []

    def add(self, value):
        self.x += int(value)

    def execute(self, instruction):
        # do something before completing cycle
        if self.x-1 <= self.cycle % 40 <= self.x+1:
            self.crt.append("#")
        else:
            self.crt.append(".")

        if instruction[0] == 'addx':
            self.add(instruction[1])
        self.cycle += 1

    def queue_actions(self, instruction):
        # add action, value to queue
        # if addx, add noop/None + add action
        self.queue.append("None")
        if instruction[0] == 'addx':
            self.queue.append(instruction)

    def calculate_signal_strength(self):
        # print(f"{self.x} * {self.cycle} = {self.x * self.cycle}")
        return self.x * self.cycle

    def print_crt(self):
        count = 0
        while count < len(self.crt):
            print(self.crt[count:count+40])
            count += 40


def part_1(data):
    circuit = Circuit()

    for line in data:
        line = line.split()
        circuit.queue_actions(line)

    signal_strength = 0
    for action in circuit.queue:
        circuit.execute(action)

        if circuit.cycle % 40 == 20:
            signal_strength += circuit.calculate_signal_strength()

    return signal_strength


def part_2(data):
    circuit = Circuit(cycle=0)

    for line in data:
        line = line.split()
        circuit.queue_actions(line)

    for action in circuit.queue:
        circuit.execute(action)

    circuit.print_crt()


if __name__ == '__main__':
    # print(f'Example {part_1(EXAMPLE)}')
    # print(f'Example {part_2(EXAMPLE)}')
    print(f'Part 1 {part_1(lines)}')
    part_2(lines)
