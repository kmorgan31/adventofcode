#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "0: 4 1 5",
    "1: 2 3 | 3 2",
    "2: 4 4 | 5 5",
    "3: 4 5 | 5 4",
    "4: 'a'",
    "5: 'b'",
    "",
    "ababbb",
    "bababa",
    "abbbab",
    "aaabbb",
    "aaaabbb",
]


def parse_data(data):
    i = 0

    rules = {}
    messages = []
    for line in data:
        if not line:
            i += 1
            continue

        if i == 0:
            # parse rules
            rule_id, options = line.split(': ')
            # import pdb; pdb.set_trace()
            if not options[0].isdigit():
                rule = options[1]
            else:
                rule = []
                for o in options.split("|"):
                    rule.append(tuple(map(int, o.split())))

            rules[int(rule_id)] = rule

        elif i == 1:
            # parse messages
            messages.append(line)
    return rules, messages


def match(rules, m, rule=0, idx=0):
    if idx == len(m):
        # message too long
        return []

    rule = rules[rule]
    if isinstance(rule, str):
        if m[idx] == rule:
            return [idx + 1]
        return []

    matches = []
    for option in rule:
        sub_matches = [idx]

        for sub_rule in option:
            new_matches = []
            for i in sub_matches:
                new_matches += match(rules, m, sub_rule, i)
            sub_matches = new_matches

        matches += sub_matches

    return matches


def main(data, part=None):
    rules, messages = parse_data(data)

    if part == 2:
        rules[8] = [(42,), (42,8)]
        rules[11] = [(42, 31), (42,11,31)]

    valid = 0
    for m in messages:
        if len(m) in match(rules, m):
            valid += 1
    return valid


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    # print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
