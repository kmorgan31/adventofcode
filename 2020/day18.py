#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "2 * 3 + (4 * 5)",
    "5 + (8 * 3 + 9 + 3 * 4 * 3)",
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
]

EXAMPLE_2 = [
    "1 + (2 * 3) + (4 * (5 + 6))"
]


def evaluate_1(line):
    ans = 0
    op = "+"

    i = 0
    while i < len(line):
        if line[i] == "(":
            sub_total, offset = evaluate_1(line[i+1:])
            ans = eval(f"{ans}{op}{sub_total}")
            i += offset+1
        elif line[i].isdigit():
            ans = eval(f"{ans}{op}{line[i]}")
        elif line[i] in ["+", "*"]:
            op = line[i]
        elif line[i] == ")":
            return ans, i
        i += 1
    return ans


def evaluate_2(line):
    while "(" in line:
        s, e = 0, 0
        for i in range(len(line)):
            if line[i] == "(":
                s = i
            elif line[i] == ")":
                e = i

                total = evaluate_2(line[s+1:e])
                line = line[:s] + [str(total)] + line[e+1:]
                break

    if "+" in line:
        while "+" in line:
            for x in range(len(line)):
                if line[x] == "+":
                    total = int(line[x-1]) + int(line[x+1])
                    line = line[:x-1] + [str(total)] + line[x+2:]
                    break

    return evaluate_1(line)


def main(data, part=None):
    total = 0
    for line in data:
        line = line.replace("(", "( ").replace(")", " )").split()
        total += (evaluate_1 if part == 1 else evaluate_2)(line)
    return total


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
