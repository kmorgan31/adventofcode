#!/usr/bin/python

from aocd import lines

from intcode import Intcode


def convert_instructions(program):
    instructions = []
    for p in program:
        instructions.extend([ord(x) for x in p])
        instructions.append(10)
    return instructions


def parse_output(output):
    line = ""
    for o in output:
        x = chr(o)
        if x == '\n':
            print(line)
            line = ""
        else:
            line += x


def main(data, part=None):
    intcode = Intcode(list(map(int, data.split(","))))

    if part == 1:
        # (!A or !B or !C) and D
        completed_program = [
            'NOT A T',
            'NOT B J',
            'OR T J',
            'NOT C T',
            'OR T J',
            'AND D J',
            'WALK'
        ]
    else:
        # (!A or !B or !C) and D and (E or H)
        completed_program = [
            'NOT A T',
            'NOT B J',
            'OR T J',
            'NOT C T',
            'OR T J',
            'AND D J',
            'NOT E T',
            'NOT T T',
            'OR H T',
            'AND T J',
            'RUN'
        ]

    intcode.run_instructions()
    if intcode.waiting:
        return intcode.run_instructions(convert_instructions(completed_program))[-1]


if __name__ == '__main__':
    print(f'Part 1 {main(lines[0], 1)}')
    print(f'Part 2 {main(lines[0], 2)}')
