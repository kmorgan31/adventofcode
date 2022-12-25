#!/usr/bin/python

from aocd import lines


def split_data(data, idx):
    zero_list, one_list = [], []

    for entry in data:
        if entry[idx] == '0':
            zero_list.append(entry)
        else:
            one_list.append(entry)
    return zero_list, one_list


def determine_oygen_rate(data, idx):
    zero_list, one_list = split_data(data, idx)
    greater_list = zero_list if len(zero_list) > len(one_list) else one_list

    if len(greater_list) == 1:
        return greater_list[0]
    else:
        return determine_oygen_rate(greater_list, idx+1)


def determine_co2_rate(data, idx):
    zero_list, one_list = split_data(data, idx)
    lesser_list = zero_list if len(zero_list) <= len(one_list) else one_list

    if len(lesser_list) == 1:
        return lesser_list[0]
    else:
        return determine_co2_rate(lesser_list, idx+1)


def determine_gamma_rate(data, idx, byte_length):
    if idx == byte_length:
        return ''

    zero_list, one_list = split_data(data, idx)
    if len(zero_list) > len(one_list):
        return '0' + determine_gamma_rate(data, idx+1, byte_length)
    else:
        return '1' + determine_gamma_rate(data, idx+1, byte_length)


def flip_bits(num):
    dct = {'1': '0', '0': '1'}
    return ''.join([dct[x] for x in num])


def part_1(data):
    byte_length = len(data[0])
    gamma_rate = determine_gamma_rate(data, 0, byte_length)

    epsilon_rate = int(flip_bits(gamma_rate), 2)
    gamma_rate = int(gamma_rate, 2)
    return gamma_rate * epsilon_rate


def part_2(data):
    oxygen_rate = int(determine_oygen_rate(data, 0), 2)
    co2_rate = int(determine_co2_rate(data, 0), 2)
    return oxygen_rate * co2_rate


if __name__ == '__main__':
    byte_length = len(lines[0])
    print(f'Day 3: Part 1 {part_1(lines)}, Part 2 {part_2(lines)}')

