#!/usr/bin/python

from aocd import lines


EXAMPLE = [
    "1=-0-2",
    "12111",
    "2=0=",
    "21",
    "2=01",
    "111",
    "20012",
    "112",
    "1=-1=",
    "1-12",
    "12",
    "1=",
    "122",
]

SNAFU_TO_NUM = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}

NUM_TO_SNAFU = {
    4: "-",
    3: "=",
    2: "2",
    1: "1",
    0: "0"
}


def snafu_to_num_converter(snafu):
    return sum([
        SNAFU_TO_NUM[snafu[-i-1]] * 5**i for i in range(len(snafu))
    ])


def num_to_snafa_converter(num):

    ans = ""
    while num > 0:
        # convert num to base_5
        n = num % 5
        num = num // 5

        if 2 < n < 5:
            # carry 1 if n is 3 or 4
            num += 1

        ans = NUM_TO_SNAFU[n] + ans
    return ans


def main(data, part=None):
    return num_to_snafa_converter(
        sum(snafu_to_num_converter(line) for line in data)
    )


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE)}')
    print(f'Part 1 {main(lines)}')
