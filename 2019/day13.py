#!/usr/bin/python

from aocd import lines

import operator as op


OPS_CODES = {
    1: op.add,
    2: op.mul
}


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

    def add_input(self, inp):
        if inp is not None:
            self.inputs.append(inp)

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
        self.add_input(i)
        self.output = []

        while self.idx < len(self.instructions):
            prog = str(self.instructions[self.idx]).zfill(5)
            mz, my, mx, op = list(map(int, [prog[0], prog[1], prog[2], prog[3:5]]))

            # import pdb; pdb.set_trace()
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
                    self.waiting = True
                    break

                self.waiting = False
                self.write(
                    self.fetch_args(2)[0], self.inputs.pop(0), mx
                )
                self.idx += 2
            elif op == 4:
                self.output.append(self.read(self.fetch_args(2)[0], mx))
                self.idx += 2
                # break
            elif op == 5:
                x, y = self.fetch_args(3)
                self.idx = (
                    self.read(y, my) if self.read(x, mx) != 0 else self.idx + 3
                )
            elif op == 6:
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


def main(data, part=None):

    if part == 1:
        intcode = Intcode(list(map(int, data[0].split(","))))
        screen_instructions = intcode.run_instructions()

        i = 0
        block_count = 0
        while i in range(len(screen_instructions)):
            x, y, tile_id = screen_instructions[i:i+3]
            block_count += tile_id == 2
            i += 3

        return block_count

    # add quarters
    intcode = Intcode(list(map(int, data[0].split(","))))
    intcode.instructions[0] = 2

    score = 0
    paddle_x, ball_x = 0, 0

    output = intcode.run_instructions()
    while not intcode.halted:
        # print(f"Score: {score}")
        # if not intcode.halted:

        i = 0
        while i in range(len(output)):
            x, y, tile_id = output[i:i+3]

            paddle_x = x if tile_id == 3 else paddle_x
            ball_x = x if tile_id == 4 else ball_x
            score = tile_id if x == -1 and y == 0 else score
            i += 3

        if intcode.waiting:
            # supply input and rerun from current place
            if ball_x > paddle_x:
                inp = 1
            elif ball_x < paddle_x:
                inp = -1
            else:
                inp = 0
            # print(f"Joystick: {inp}")

            output = intcode.run_instructions(inp)

    if output:
        i = 0
        while i in range(len(output)):
            x, y, tile_id = output[i:i+3]
            paddle_x = x if tile_id == 3 else paddle_x
            ball_x = x if tile_id == 4 else ball_x
            score = tile_id if x == -1 and y == 0 else score
            i += 3

    return score


if __name__ == '__main__':
    # print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
