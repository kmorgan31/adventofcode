#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "root: pppw + sjmn",
    "dbpl: 5",
    "cczh: sllz + lgvd",
    "zczc: 2",
    "ptdq: humn - dvpt",
    "dvpt: 3",
    "lfqf: 4",
    "humn: 5",
    "ljgn: 2",
    "sjmn: drzm * dbpl",
    "sllz: 4",
    "pppw: cczh / lfqf",
    "lgvd: ljgn * ptdq",
    "drzm: hmdt - zczc",
    "hmdt: 32"
]

OPERATIONS = {
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '/': lambda x, y: x // y,
}

INV_OPERATIONS = {
    '-': "+",
    '*': "/",
    '+': "-",
    '/': "*",
}


class Monkey:

    def __init__(self, num=None, monkeys=None, op=None):
        self.num = num
        self.monkeys = monkeys
        self.op = op


def dfs(monkey_name, graph):
    if graph[monkey_name].num is not None:
        return graph[monkey_name].num

    elif graph[monkey_name].monkeys:
        nums = list(map(lambda x: dfs(x, graph), graph[monkey_name].monkeys))
        return OPERATIONS[graph[monkey_name].op](*nums) if all(nums) else None


def get_humn(monkey_name, graph, ans):
    if graph[monkey_name].num is not None:
        return graph[monkey_name].num

    elif graph[monkey_name].monkeys:
        monkey_l, monkey_r = graph[monkey_name].monkeys
        left, right = dfs(monkey_l, graph), dfs(monkey_r, graph)

        if left is None:
            return get_humn(
                monkey_l, graph,
                OPERATIONS[INV_OPERATIONS[graph[monkey_name].op]](ans, right)
            )
        elif right is None:
            if graph[monkey_name].op in ["+", "*"]:
                return get_humn(
                    monkey_r, graph,
                    OPERATIONS[INV_OPERATIONS[graph[monkey_name].op]](ans, left)
                )
            else:
                return get_humn(
                    monkey_r, graph,
                    OPERATIONS[graph[monkey_name].op](left, ans)
                )

    return ans


def main(data, part=None):

    monkeys = {}
    for line in data:
        name, x = line.split(": ")
        instruction = x.split()
        if instruction[0].isdigit():
            monkeys[name] = Monkey(num=int(instruction[0]))
        else:
            monkeys[name] = Monkey(
                monkeys=[instruction[0], instruction[2]], op=instruction[1]
            )

    if part == 1:
        return dfs("root", monkeys)

    if part == 2:
        monkeys["root"].op = "-"
        monkeys["humn"].num = None
        return get_humn("root", monkeys, 0)


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
