#!/usr/bin/python

from aocd import lines


import operator as op
from itertools import permutations


OPS_CODES = {
    1: op.add,
    2: op.mul
}

EXAMPLE = ["3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"]

EXAMPLE_2 = ["3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"]


class Amp:

    def __init__(self, instructions, phase):
        self.instructions = instructions
        self.phase = phase
        self.idx = 0

    @property
    def halted(self):
        return self.instructions[self.idx] == 99

    def get_value(self, val, mode):
        return self.instructions[val] if mode == 0 else val

    def run_instructions(self, a):
        inputs = [self.phase, a]

        # if self.halted:
        #     return None

        while True:
            prog = str(self.instructions[self.idx]).zfill(5)
            ma, my, mx, op = list(map(int, [prog[0], prog[1], prog[2], prog[3:5]]))

            if OPS_CODES.get(op):
                x, y, z = self.instructions[self.idx+1:self.idx+4]
                op_sign = "+" if op == 1 else "*"
                # print(f"{self.get_value(x, mx)} {op_sign} {self.get_value(y, my)} => location {z}")
                self.instructions[z] = OPS_CODES[op](
                    self.get_value(x, mx), self.get_value(y, my)
                )
                self.idx += 4
            elif op == 3:
                # print(f"Value at location {self.instructions[self.idx+1]} set to {inputs[0]}")
                self.instructions[self.instructions[self.idx+1]] = inputs.pop(0)
                self.idx += 2
            elif op == 4:
                # if mx == 0:
                #     print(f"Print value at location {self.instructions[self.idx+1]} => {self.instructions[self.instructions[self.idx+1]]}")
                # else:
                #     print(f"Print value => {self.instructions[self.idx+1]}")

                output = self.get_value(self.instructions[self.idx+1], mx)
                self.idx += 2
                break
            elif op == 5:
                x, y = self.instructions[self.idx+1:self.idx+3]
                # import pdb; pdb.set_trace()
                self.idx = (
                    self.get_value(y, my) if self.get_value(x, mx) != 0 else self.idx + 3
                )
                # print(f"Jump to location {self.idx}")
            elif op == 6:
                x, y = self.instructions[self.idx+1:self.idx+3]
                self.idx = (
                    self.get_value(y, my) if self.get_value(x, mx) == 0 else self.idx + 3
                )
                # print(f"Jump to location {self.idx}")
            elif op == 7:
                x, y, z = self.instructions[self.idx+1:self.idx+4]
                self.instructions[z] = (
                    1 if self.get_value(x, mx) < self.get_value(y, my) else 0
                )
                # print(f"Value at location {z} if set to {self.instructions[z]}")
                self.idx += 4
            elif op == 8:
                x, y, z = self.instructions[self.idx+1:self.idx+4]
                self.instructions[z] = (
                    1 if self.get_value(x, mx) == self.get_value(y, my) else 0
                )
                # print(f"Value at location {z} if set to {self.instructions[z]}")
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
                    output = amp.run_instructions(output_signal)
                    # import pdb; pdb.set_trace()
                    if not amp.halted:
                        output_signal = output
            print(f"P {p}: {output_signal}")
            max_output_signal = max(output_signal, max_output_signal)

    return max_output_signal


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE_2, 2)}')
    # print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
