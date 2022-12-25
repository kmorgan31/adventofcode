#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390"
]


def determine_score(curr_tree, trees):
    if not trees:
        return 0

    score = 0
    for x in trees:
        score += 1
        if x >= curr_tree:
            break
    return score


def part_1(data, part=None):
    row_size = len(data)
    col_size = len(data[0])

    t = [[int(y) for y in x] for x in data]

    count = 0
    for r in range(row_size):
        for c in range(col_size):
            curr_tree = t[r][c]

            treesLeft = [x for x in t[r][:c] if x >= curr_tree]
            treesRight = [x for x in t[r][c+1:] if x >= curr_tree]
            treesUp = [x[c] for i, x in enumerate(t) if x[c] >= curr_tree and i < r]
            treesDown = [x[c] for i, x in enumerate(t) if x[c] >= curr_tree and i > r]
            count += not (treesLeft and treesRight and treesUp and treesDown)

    return count


def part_2(data, part=None):
    row_size = len(data)
    col_size = len(data[0])

    t = [[int(y) for y in x] for x in data]

    max_score = 0
    for r in range(row_size):
        for c in range(col_size):
            curr_tree = t[r][c]

            treesLeft = [x for x in t[r][:c]]
            treesLeft.reverse()
            left_score = determine_score(curr_tree, treesLeft)

            treesRight = [x for x in t[r][c+1:]]
            right_score = determine_score(curr_tree, treesRight)

            treesUp = [x[c] for i, x in enumerate(t) if i < r]
            treesUp.reverse()
            up_score = determine_score(curr_tree, treesUp)

            treesDown = [x[c] for i, x in enumerate(t) if i > r]
            down_score = determine_score(curr_tree, treesDown)

            score = left_score * right_score * up_score * down_score
            max_score = max(max_score, score)

    return max_score


if __name__ == '__main__':
    # print(f'Part 1 {part_1(EXAMPLE)}')
    # print(f'Part 2 {part_2(EXAMPLE)}')
    print(f'Part 1 {part_1(lines)}')
    print(f'Part 2 {part_2(lines)}')
