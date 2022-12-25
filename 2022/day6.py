#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
]


def main(data, part=None):
    count = 0
    line = data[0]

    if part == 1:
        marker_size = 4
    elif part == 2:
        marker_size = 14

    while count < len(line)-marker_size:
        marker = line[count: count+marker_size]
        if len(set(marker)) == marker_size:
            return count+marker_size
        else:
            count += 1


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 2)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
