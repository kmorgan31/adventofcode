#!/usr/bin/python


EXAMPLE = ".^^.^.^^^^"
INPUT = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."


def get_tiles(row, i):
    ans = ""
    for x in range(i-1, i+2):
        ans += "." if x < 0 or x > len(row)-1 else row[x]
    return ans


def main(row, num_rows):

    safe_tiles = row.count('.')
    for r in range(num_rows-1):
        new_row = ""

        for i in range(len(row)):
            x, y, z = get_tiles(row, i)
            if not ((x == y and x != z) or (x != z and y == z)):
                new_row += "^"
            else:
                new_row += "."

        safe_tiles += new_row.count(".")
        row = new_row

    return safe_tiles


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 10)}')
    print(f'Part 1 {main(INPUT, 40)}')
    print(f'Part 2 {main(INPUT, 400000)}')
