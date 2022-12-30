#!/usr/bin/python

from aocd import lines


import operator as op
from itertools import permutations


OPS_CODES = {
    1: op.add,
    2: op.mul
}


class Amp:

    def __init__(self, instructions, phase):
        self.instructions = instructions
        self.inputs = [phase]
        self.idx = 0

    @property
    def halted(self):
        return self.instructions[self.idx] == 99

    def get_value(self, val, mode):
        return self.instructions[val] if mode == 0 else val

    def run_instructions(self, a):
        self.inputs.append(a)

        while True:
            prog = str(self.instructions[self.idx]).zfill(5)
            ma, my, mx, op = list(map(int, [prog[0], prog[1], prog[2], prog[3:5]]))

            if OPS_CODES.get(op):
                x, y, z = self.instructions[self.idx+1:self.idx+4]
                self.instructions[z] = OPS_CODES[op](
                    self.get_value(x, mx), self.get_value(y, my)
                )
                self.idx += 4
            elif op == 3:
                self.instructions[self.instructions[self.idx+1]] = self.inputs.pop(0)
                self.idx += 2
            elif op == 4:
                output = self.get_value(self.instructions[self.idx+1], mx)
                self.idx += 2
                break
            elif op == 5:
                x, y = self.instructions[self.idx+1:self.idx+3]
                self.idx = (
                    self.get_value(y, my) if self.get_value(x, mx) != 0 else self.idx + 3
                )
            elif op == 6:
                x, y = self.instructions[self.idx+1:self.idx+3]
                self.idx = (
                    self.get_value(y, my) if self.get_value(x, mx) == 0 else self.idx + 3
                )
            elif op == 7:
                x, y, z = self.instructions[self.idx+1:self.idx+4]
                self.instructions[z] = (
                    1 if self.get_value(x, mx) < self.get_value(y, my) else 0
                )
                self.idx += 4
            elif op == 8:
                x, y, z = self.instructions[self.idx+1:self.idx+4]
                self.instructions[z] = (
                    1 if self.get_value(x, mx) == self.get_value(y, my) else 0
                )
                self.idx += 4
            elif op == 99:
                break
        return output


def main(data, part=None):
    max_output_signal = 0

    p_range = (0, 5) if part == 1 else (5, 10)
    for p in permutations(range(*p_range)):
        amps = [Amp(list(map(int, data[0].split(","))), j) for j in p]

        output_signal = 0
        if part == 1:
            for amp in amps:
                output_signal = amp.run_instructions(output_signal)
            max_output_signal = max(output_signal, max_output_signal)

        elif part == 2:
            while all(not amp.halted for amp in amps):
                for amp in amps:
                    output_signal = amp.run_instructions(output_signal)
            max_output_signal = max(output_signal, max_output_signal)

    return max_output_signal


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
