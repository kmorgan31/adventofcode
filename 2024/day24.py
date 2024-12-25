#!/usr/bin/python
# AOC_SESSION: 53616c7465645f5f363b4a57ce0343b9d63abecac78165ff4bf4ef272149008a22a075dcb520ddbb77c4d956b17bad6cbedde3d42c2022f1f4cf68ceb5935a67

from aocd import data

import heapq

from collections import defaultdict


EXAMPLE = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

EXAMPLE_2 = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""


class Graph:

    def __init__(self, data):
        self.gates = {}
        self.outputs = {}
        self.swaps = []

        for line in data.splitlines():
            if ":" in line:
                ans = line.split(":")
                self.gates[ans[0]] = int(ans[1].strip(), base=2)
            if "->" in line:
                ans = line.split()
                inp1, op, inp2, out1 = ans[0], ans[1], ans[2], ans[4]
                self.outputs[out1] = (inp1, op, inp2)

    def explore(self, gate):
        if gate in self.gates:
            return self.gates[gate]

        inp1, op, inp2 = self.outputs[gate]
        if op == "AND":
            self.gates[gate] = self.explore(inp1) & self.explore(inp2)
        elif op == "OR":
            self.gates[gate] = self.explore(inp1) | self.explore(inp2)
        elif op == "XOR":
            self.gates[gate] = self.explore(inp1) ^ self.explore(inp2)
        return self.gates[gate]

    def set_num(self, letter, num):
        for i, x in enumerate(reversed(num)):
            gate = f"{letter}{str(i).zfill(2)}"
            self.gates[gate] = int(x, base=2)

    def get_num(self, letter):
        result = ""
        for g in sorted(self.gates.keys(), reverse=True):
            if not g.startswith(letter):
                continue
            result += str(self.gates[g])
        print(result)
        return int(result, 2)

    def run_program(self, letter):
        result = ""
        for g in sorted(self.outputs.keys(), reverse=True):
            if not g.startswith(letter):
                continue
            result += str(self.explore(g))
        return int(result, 2)

    def find_swap(self):
        for out, (inp1, op, inp2) in self.outputs.items():
            if op == "XOR" and not out.startswith("z") and self.gates[out] == 1:
                return out

    def swap(self, g1, g2):
        self.swaps += [g1, g2]
        self.outputs[g1], self.outputs[g2] = self.outputs[g2], self.outputs[g1]

    def find_output(self, x, o, y):
        for out, (inp1, op, inp2) in self.outputs.items():
            if (inp1, op, inp2) == (x, o, y) or (inp1, op, inp2) == (y, o, x):
                return out


def part_1(data):
    graph = Graph(data)
    return graph.run_program("z")


def part_2(data):
    # store gates
    gate_and = defaultdict(None)
    gate_xor = defaultdict(None)
    gate_z = defaultdict(None)
    gate_tmp = defaultdict(None)
    gate_carry = defaultdict(None)

    graph = Graph(data)
    graph.run_program("z")

    # initialize
    gate_and[0] = graph.find_output("x00", "AND", "y00")
    gate_xor[0] = graph.find_output("x00", "XOR", "y00")
    gate_z[0] = gate_xor[0]
    gate_carry[0] = gate_and[0]

    for i in range(1, 45):
        x = f"x{str(i).zfill(2)}"
        y = f"y{str(i).zfill(2)}"
        z = f"z{str(i).zfill(2)}"

        check = True
        while check:
            check = False

            gate_and[i] = graph.find_output(x, "AND", y)
            gate_xor[i] = graph.find_output(x, "XOR", y)

            inp1, op, inp2 = graph.outputs[z]
            if inp1 == gate_carry[i-1] and inp2 != gate_xor[i]:
                graph.swap(inp2, gate_xor[i])
                check = True
                continue
            if inp2 == gate_carry[i-1] and inp1 != gate_xor[i]:
                graph.swap(inp1, gate_xor[i])
                check = True
                continue

            # The output of the z gate should be z.
            gate_z[i] = graph.find_output(gate_xor[i], "XOR", gate_carry[i-1])
            if gate_z[i] != z:
                graph.swap(gate_z[i], z)
                check = True
                continue

            gate_tmp[i] = graph.find_output(gate_xor[i], "AND", gate_carry[i-1])
            gate_carry[i] = graph.find_output(gate_tmp[i], "OR", gate_and[i])

    assert len(graph.swaps) == 8
    return ",".join(sorted(graph.swaps))


if __name__ == '__main__':
    print(f'Part 1 {part_1(EXAMPLE_2)}')
    print(f'Part 1 {part_1(data)}')
    print(f'Part 2 {part_2(data)}')
