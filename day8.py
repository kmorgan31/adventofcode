#!/usr/bin/python

import sys
import requests
from itertools import permutations


def determine_question():
    return map(int, sys.argv[1].split('.'))


def fetch_data(day):
    cookie = '53616c7465645f5fa5d68c2c74333c3cf12f7d3fd1879c09c13156e540110a1ab1c384fc44a06720c841e41aa6ec5668'
    target_url = f"https://adventofcode.com/2021/day/{day}/input"
    session = requests.Session()
    return session.get(
        target_url, cookies={'session': cookie}
    ).text.strip().split('\n')


signal_patterns = {
    "abcefg": '0',
    "cf": '1',
    "acdeg": '2',
    "acdfg": '3',
    "bcdf": '4',
    "abdfg": '5',
    "abdefg": '6',
    "acf": '7',
    "abcdefg": '8',
    "abcdfg": '9'
}


def transform(mapping, digit):
    # converts jumbled digit to correct digit
    return ''.join(sorted(transform([mapping[y] for y in digit])))


def decode_signal(mapping, digits):
    # finds matching numbers for each transformed digit  in digits
    return [
        signal_patterns.get(transform(mapping, x)) for x in digits
    ]


if __name__ == '__main__':
    day, part = determine_question()
    data = fetch_data(day)

    count = 1
    num_count = 0
    sum_output_value = 0
    for line in data:
        input_signal, output_signal = line.split('|')
        input_digits = input_signal.split()
        output_digits = output_signal.split()

        num_count += sum(len(x) in [2, 3, 4, 7] for x in output_digits)

        for permutation in permutations(list("abcdefg")):
            mapping = dict(zip("abcdefg", permutation))

            # check that all the output_digits can be found in the chosen mapping
            input_signal = decode_signal(mapping, input_digits)
            if all(input_signal):
                output_signal = decode_signal(mapping, output_digits)
                sum_output_value += int(''.join(output_signal))
                break

    print(num_count)
    print(sum_output_value)
