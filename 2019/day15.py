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

    def copy(self):
        copy = Intcode(self.instructions)
        copy.inputs = self.inputs
        copy.idx = self.idx
        copy.relative_base = self.relative_base
        copy.extra_memory = self.extra_memory.copy()
        return copy

    def add_input(self, inp):
        if inp is not None:
            self.inputs.append(inp)

    def fetch(self, idx):
        return (
            self.instructions[idx] if idx < len(self.instructions)
            else self.extra_memory.get(idx, 0)
        )

    def fetch_args(self, num):
        return [self.fetch(i) for i in range(self.idx+1, self.idx+num+1)]

    def read(self, val, mode):
        if mode == 1:
            return val, f"{val}"
        elif mode == 2:
            val += self.relative_base

        return self.fetch(val), f"location at {val}: {self.fetch(val)}"

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

        while not self.halted:
            prog = str(self.instructions[self.idx]).zfill(5)
            mz, my, mx, op = list(map(int, [prog[0], prog[1], prog[2], prog[3:5]]))

            # import pdb; pdb.set_trace()
            if OPS_CODES.get(op):
                x, y, z = self.fetch_args(3)
                op_sign = "+" if op == 1 else "*"

                arg_x, lx = self.read(x, mx)
                arg_y, ly = self.read(y, my)
                arg_z, lz = self.read(z, mz)

                print(f"{op} Write {lx} {op_sign} {ly} to {lz}")
                self.write(z, OPS_CODES[op](arg_x, arg_y), mz)
                self.idx += 4
            elif op == 3:
                # pdb.set_trace()
                if not len(self.inputs):
                    print(f"{op} Waiting")
                    self.waiting = True
                    return self.output

                x = self.fetch_args(1)[0]

                arg_x, lx = self.read(x, mx)
                print(f"{op} Write {arg_x} to {lx}")

                self.waiting = False
                self.write(arg_x, self.inputs.pop(0), mx)
                self.idx += 2
            elif op == 4:
                # pdb.set_trace()
                x = self.fetch_args(1)[0]

                arg_x, lx = self.read(x, mx)
                print(f"{op} Print value at {lx}")

                self.output.append(arg_x)
                self.idx += 2
                # break
            elif op == 5:
                # pdb.set_trace()
                x, y = self.fetch_args(2)

                arg_x, lx = self.read(x, mx)
                arg_y, ly = self.read(y, my)
                if arg_x != 0:
                    print(f"{op} Set index from {self.idx} to {ly}")
                else:
                    print(f"{op} Set index from {self.idx} to {self.idx + 3}")

                self.idx = (arg_y if arg_x != 0 else self.idx + 3)
            elif op == 6:
                # pdb.set_trace()
                x, y = self.fetch_args(2)

                arg_x, lx = self.read(x, mx)
                arg_y, ly = self.read(y, my)
                if arg_x == 0:
                    print(f"{op} Set index from {self.idx} to {ly}")
                else:
                    print(f"{op} Set index from {self.idx} to {self.idx + 3}")

                self.idx = (arg_y if arg_x == 0 else self.idx + 3)
            elif op == 7:
                # pdb.set_trace()
                x, y, z = self.fetch_args(3)

                arg_x, lx = self.read(x, mx)
                arg_y, ly = self.read(y, my)
                arg_z, lz = self.read(z, mz)
                if arg_x < arg_y:
                    print(f"{op} Write 1 to {lz}")
                else:
                    print(f"{op} Write 0 to {lz}")

                self.write(z, 1 if arg_x < arg_y else 0, mz)
                self.idx += 4
            elif op == 8:
                # pdb.set_trace()
                x, y, z = self.fetch_args(3)

                arg_x, lx = self.read(x, mx)
                arg_y, ly = self.read(y, my)
                arg_z, lz = self.read(z, mz)
                if arg_x == arg_y:
                    print(f"{op} Write 1 to {lz}")
                else:
                    print(f"{op} Write 0 to {lz}")

                self.write(z, 1 if arg_x == arg_y else 0, mz)
                self.idx += 4
            elif op == 9:
                # pdb.set_trace()
                x = self.fetch_args(1)[0]

                arg_x, lx = self.read(x, mx)
                print(f"{op} Update relative_base from {self.relative_base} to {lx}")

                self.relative_base += self.read(arg_x, mx)
                self.idx += 2
            # elif op == 99:
            #     # import pdb; pdb.set_trace()
            #     print(f"{op} Halting")
            #     break

        print(f"Halting at index {self.idx}")
        return self.output


def get_surrounding_points(pos):
    x, y = pos
    return [
        (x-1, y),
        (x, y+1),
        (x+1, y),
        (x, y-1)
    ]


def bfs(intcode):
    visited = {}
    to_visit = [((0, 0), 0, intcode)]

    # steps = 0
    while to_visit:
        pos, step, intcode = to_visit.pop()
        visited[pos] = "1"

        # get possible locations to visit
        for d, sp in enumerate(get_surrounding_points(pos)):
            if sp not in visited:
                intcode2 = intcode.copy()
                status = intcode2.run_instructions(d)
                import pdb; pdb.set_trace()
                if status == 0:
                    # wall, cannot be visited next
                    # pre-emptively add to visited
                    visited[sp] = "0"
                if status == 1:
                    # space to be visited, increase step
                    to_visit.add((sp, step+1, intcode2))
                if status == 2:
                    # oxygen location found
                    return (sp, step+1)
                    # return steps
        # steps += 1


def main(data, part=None):
    intcode = Intcode(list(map(int, data[0].split(","))))
    oxygen_pos, step = bfs(intcode)

    return abs(oxygen_pos[0]) + abs(oxygen_pos[1])


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    # print(f'Part 2 {main(lines, 2)}')
