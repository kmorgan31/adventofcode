#!/usr/bin/python

from collections import defaultdict

EXAMPLE = [0,3,6]
INPUT = [6,13,1,15,2,0]


def main(data, end_idx):
    last_spoken = data[-1]

    last_spoken_dct = defaultdict(int)
    second_last_spoken_dct = defaultdict(int)
    for t, x in enumerate(data):
        last_spoken_dct[x] = t+1

    t = len(data)+1
    while t <= end_idx:
        if second_last_spoken_dct[last_spoken] == 0:
            # spoken <= 1 time
            last_spoken = 0
        else:
            last_spoken = (
                last_spoken_dct[last_spoken] - second_last_spoken_dct[last_spoken]
            )

        # print(f"Turn: {t} Spoken: {last_spoken}")
        second_last_spoken_dct[last_spoken] = last_spoken_dct[last_spoken]
        last_spoken_dct[last_spoken] = t
        t += 1

    return last_spoken


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 30000000)}')
    print(f'Part 1 {main(INPUT, 2020)}')
    print(f'Part 2 {main(INPUT, 30000000)}')
