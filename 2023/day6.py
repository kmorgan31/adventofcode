#!/usr/bin/python


EXAMPLE_1 = [
    [7, 15, 30],
    [9, 40, 200]
]
EXAMPLE_2 = [
    [71530],
    [940200]
]

INPUT_1 = [
    [44, 89, 96, 91],
    [277, 1136, 1890, 1768]
]
INPUT_2 = [
    [44899691],
    [277113618901768]
]


def main(data, part=None):
    times, distances = data

    score = 1
    min_t, max_t = float("inf"), 0
    for x in range(len(times)):

        ways = 0
        for t in range(1, int(times[x])):
            t_remaining = int(times[x]) - t
            distance_travelled = t_remaining * t
            if distance_travelled > int(distances[x]):
                # print(f"Race {x+1}: Held {t} seconds, travelled for {distance_travelled}")
                ways += 1
                min_t, max_t = min(min_t, t), max(max_t, t)
        score *= ways
    if part == 1:
        return score
    elif part == 2:
        return max_t - min_t + 1


if __name__ == '__main__':
    print(f'Day 6: Part 1 {main(INPUT_1, part=1)}')
    print(f'Day 6: Part 2 {main(INPUT_2, part=2)}')
