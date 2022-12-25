#!/usr/bin/python

from aocd import lines

import functools


# class Instruction():

#     def __init__(self, name, value):
#         self.name = name
#         self.value = value


# class ALU():

#     def __init__(self):
#         self.w = 0
#         self.x = 0
#         self.y = 0
#         self.z = 0

#     def inp(self, a, b):
#         setattr(self, a.name, a.value)

#     def add(self, a, b):
#         # a, b - Instruction
#         setattr(self, a.name, a.value + b.value)

#     def mul(self, a, b):
#         # a, b - Instruction
#         setattr(self, a.name, a.value * b.value)

#     def div(self, a, b):
#         # a, b - Instruction
#         setattr(self, a.name, a.value // b.value)

#     def mod(self, a, b):
#         # a, b - Instruction
#         setattr(self, a.name, a.value % b.value)

#     def eql(self, a, b):
#         # a, b - Instruction
#         value = 1 if a.value == b.value else 0
#         setattr(self, a.name, value)

#     def print(self, line):
#         print(f'Line: {line}, W: {self.w} X: {self.x} Y: {self.y}, Z: {self.z}')

class ALU():

    def __init__(self):
        self.add_x = []
        self.div_z = []
        self.add_y = []

    def parse_instructions_per_digit(self, data):
        # pick important instructions, add values to arrays
        for num, line in enumerate(data):
            line = line.split()
            if len(line) == 2:
                continue

            op, a, b = line
            if op == 'add' and a == 'x' and b != 'z':
                self.add_x.append(int(b))
            elif op == 'div' and a == 'z':
                self.div_z.append(int(b))
            elif op == 'add' and a == 'y' and num % 18 == 15:
                self.add_y.append(int(b))

    def calc_max_z(self):
        self.max_z = [
            26**len([x for x in range(len(self.div_z)) if self.div_z[x]==26 and x >= i])
            for i in range(len(self.div_z))
        ]

    def process_digit(self, idx, z, w):
        # idx - position in model number
        # w - value at position in model number
        # z - running value
        x = self.add_x[idx] + (z % 26)
        z = z // self.div_z[idx]
        if x != w:
            z *= 26
            z += w + self.add_y[idx]
        return z

    @functools.lru_cache(maxsize=None)
    def run_monad(self, idx, z1):
        if idx == 14:
            # end of model number
            if z1 == 0:
                # import pdb; pdb.set_trace()
                return [""]
            return []

        if z1 > self.max_z[idx]:
            # stop early
            # import pdb; pdb.set_trace()
            return []

        x = self.add_x[idx] + (z1 % 26)
        w_lst = list(range(1, 10))
        if x in range(1, 10):
            w_lst = [x]

        res = []
        for i in w_lst:
            z2 = self.process_digit(idx, z1, i)
            nxt = self.run_monad(idx+1, z2)
            for j in nxt:
                res.append(str(i) + j)
        return res


def main(data, part=None):
    alu = ALU()
    alu.parse_instructions_per_digit(data)
    alu.calc_max_z()

    valid_nums = [int(x) for x in alu.run_monad(0, 0)]

    return max(valid_nums), min(valid_nums)


if __name__ == '__main__':

    # tests
    # print(f'Test Data: Part 1 {main(test_data_2, 1)}, Part 2 {main(test_data_2, 2)}')

    # question
    max_num, min_num = main(lines)
    print(f'Day 21: Part 1 {max_num}, Part 2 {min_num}')
