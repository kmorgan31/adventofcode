#!/usr/bin/python

from aocd import lines

import operator as op


OPS_CODES = {
    1: op.add,
    2: op.mul
}

FACING = list(range(4))


class Intcode:

    def __init__(self, instructions, inputs=None):
        self.instructions = instructions
        self.inputs = inputs or []
        self.idx = 0
        self.relative_base = 0
        self.extra_memory = {}

    @property
    def halted(self):
        return self.fetch(self.idx) == 99

    def fetch(self, idx):
        return (
            self.instructions[idx] if idx < len(self.instructions)
            else self.extra_memory.get(idx, 0)
        )

    def fetch_args(self, num):
        return [self.fetch(i) for i in range(self.idx+1, self.idx+num)]

    def read(self, val, mode):
        if mode == 1:
            return val
        elif mode == 2:
            val += self.relative_base

        return self.fetch(val)

    def write(self, z, val, mode):
        if mode == 2:
            z += self.relative_base

        (
            self.instructions if z < len(self.instructions)
            else self.extra_memory
        )[z] = val

    def run_instructions(self, i=None):
        if i is not None:
            self.inputs.append(i)
        self.output = []

        while self.idx < len(self.instructions):
            prog = str(self.instructions[self.idx]).zfill(5)
            mz, my, mx, op = list(map(int, [prog[0], prog[1], prog[2], prog[3:5]]))

            if OPS_CODES.get(op):
                x, y, z = self.fetch_args(4)
                self.write(
                    z,
                    OPS_CODES[op](self.read(x, mx), self.read(y, my)),
                    mz
                )
                self.idx += 4
            elif op == 3:
                if not len(self.inputs):
                    break

                self.write(
                    self.fetch_args(2)[0], self.inputs.pop(0), mx
                )
                self.idx += 2
            elif op == 4:
                self.output.append(self.read(self.fetch_args(2)[0], mx))
                self.idx += 2
                # break
            elif op == 5:
                # pdb.set_trace()
                x, y = self.fetch_args(3)
                self.idx = (
                    self.read(y, my) if self.read(x, mx) != 0 else self.idx + 3
                )
            elif op == 6:
                # pdb.set_trace()
                x, y = self.fetch_args(3)
                self.idx = (
                    self.read(y, my) if self.read(x, mx) == 0 else self.idx + 3
                )
            elif op == 7:
                x, y, z = self.fetch_args(4)
                self.write(
                    z, 1 if self.read(x, mx) < self.read(y, my) else 0, mz
                )
                self.idx += 4
            elif op == 8:
                x, y, z = self.fetch_args(4)
                self.write(
                    z, 1 if self.read(x, mx) == self.read(y, my) else 0, mz
                )
                self.idx += 4
            elif op == 9:
                self.relative_base += self.read(self.fetch_args(2)[0], mx)
                self.idx += 2
            elif op == 99:
                break

        return self.output


def print_panels(panels):
    xvals = [x[0] for x in panels]
    yvals = [x[1] for x in panels]

    for x in range(min(xvals), max(xvals)+1):
        print(''.join(
            str(panels.get((x, y), 0)) for y in range(min(yvals), max(yvals)+1))
        )


def main(data, part=None):
    intcode = Intcode(list(map(int, data[0].split(","))))

    x, y, f = 0, 0, 0
    panels = {(x, y): part-1}
    while not intcode.halted:
        # get current colour. If unknown, the panel is black (0)
        colour = panels.get((x, y), 0)

        # get new colour based on current colour, using intcode
        new_colour, turn = intcode.run_instructions(colour)

        # add panel and colour to dict
        panels[(x, y)] = new_colour

        # move robot
        f = FACING[(f-1 if turn == 0 else f+1) % len(FACING)]
        if f == 0:
            x -= 1
        elif f == 1:
            y += 1
        elif f == 2:
            x += 1
        elif f == 3:
            y -= 1

    if part == 1:
        return len(panels)
    elif part == 2:
        # print panels
        print_panels(panels)


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
