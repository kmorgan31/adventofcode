#!/usr/bin/python

from aocd import lines

STACKS = [
    ["Z", "N"],         # 1
    ["M", "C", "D"],    # 2
    ["P"]               # 3
]

QUESTION = [
    ["Q", "S", "W", "C", "Z", "V", "F", "T"],       # 1
    ["Q", "R", "B"],                                # 2
    ["B", "Z", "T", "Q", "P", "M", "S"],             # 3
    ["D", "V", "F", "R", "Q", "H"],                 # 4
    ["J", "G", "L", "D", "B", "S", "T", "P"],       # 5
    ["W", "R", "T", "Z"],                           # 6
    ["H", "Q", "M", "N", "S", "F", "R", "J"],       # 7
    ["R", "N", "F", "H", "W"],                      # 8
    ["J", "Z", "T", "Q", "P", "R", "B"]             # 9
]

EXAMPLE = [
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2"
]


def main(stacks, data, part=None):
    count = 0

    for line in data:
        line = line.split()
        if not line or line[0] != "move":
            continue

        num_boxes, source, dest = int(line[1]), int(line[3]), int(line[5])

        if part == 1:
            for x in range(num_boxes):
                box = stacks[source-1].pop()
                stacks[dest-1].append(box)
        elif part == 2:
            stacks[source-1], boxes = stacks[source-1][:-num_boxes], stacks[source-1][-num_boxes:]
            stacks[dest-1].extend(boxes)

    return ''.join([x[-1] for x in stacks])


if __name__ == '__main__':
    # print(f'Example {main(STACKS, EXAMPLE, 2)}')
    print(f'Part 1 {main(QUESTION, lines, 1)}')
    print(f'Part 2 {main(QUESTION, lines, 2)}')
