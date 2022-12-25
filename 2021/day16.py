#!/usr/bin/python

from aocd import lines
from math import prod

test_data = [
    'D2FE28',
    '38006F45291200',
    'EE00D40C823060',
    '8A004A801A8002F478',
    '620080001611562C8802118E34',
    'C0015000016115A2E0802F182340',
    'A0016C880162017C3686B18A3D4780'
]


class Processor():

    def __init__(self, bin_str):
        self.bitstr = bin_str
        self.total_version = 0
        self.pos = 0

    def get_n_bits(self, n):
        # more pos pointer n bits, return int of n bits
        bits_to_int = int(self.bitstr[self.pos:self.pos + n], 2)
        self.pos += n

        return bits_to_int

    def parse_packet(self):
        version = self.get_n_bits(3)
        self.total_version += version

        type_id = self.get_n_bits(3)
        if type_id == 4:
            return self.parse_literal_packet()

        subpackets = []
        length_type_id = self.get_n_bits(1)
        if length_type_id == 0:
            total_length = self.get_n_bits(15)
            expected_pos = self.pos + total_length
            while self.pos < expected_pos:
                subpackets.append(self.parse_packet())
        else:
            num_sub_packets = self.get_n_bits(11)
            for x in range(num_sub_packets):
                subpackets.append(self.parse_packet())

        return self.find_value_of_subpackets(type_id, subpackets)

    def find_value_of_subpackets(self, type_id, subpackets):
        if type_id == 0:
            return sum(subpackets)
        elif type_id == 1:
            return prod(subpackets)
        elif type_id == 2:
            return min(subpackets)
        elif type_id == 3:
            return max(subpackets)
        elif type_id == 5:
            return int(subpackets[0] > subpackets[1])
        elif type_id == 6:
            return int(subpackets[0] < subpackets[1])
        elif type_id == 7:
            return int(subpackets[0] == subpackets[1])

    def parse_literal_packet(self):
        value = ''

        flag = 1
        while flag != 0:
            flag = self.get_n_bits(1)

            # get chunk of next 4 bits, move pos pointer
            chunk = self.bitstr[self.pos:self.pos + 4]
            value += chunk
            self.pos += 4
        return int(value, 2)


def main(data, part):
    # add 1 to ensure leading 0 included
    data = bin(int('1' + data, 16))[3:]

    packet_processor = Processor(data)
    res = packet_processor.parse_packet()

    if part == 1:
        return packet_processor.total_version
    elif part == 2:
        return res


if __name__ == '__main__':

    # tests
    for i, td in enumerate(test_data):
        print(f'Test Data {i+1}: Part 1 {main(td, 1)}, Part 2 {main(td, 2)}')

    # question
    lines = lines[0]
    print(f'Day 16: Part 1 {main(lines, 1)}, Part 2 {main(lines, 2)}')
