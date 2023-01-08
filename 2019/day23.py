#!/usr/bin/python

from aocd import lines

from intcode import Intcode


class Node:
    def __init__(self, intcode, address):
        self.intcode = intcode
        self.messages = []      # queue
        self.intcode.run_instructions(address)

    def create_packet_from_queue(self):
        # creates packet with first two items in queue
        return [self.messages.pop(0), self.messages.pop(0)]

    def prepare_packet(self):
        # return destination, x and y for a packet in output
        return (
            self.intcode.output.pop(0),
            self.intcode.output.pop(0),
            self.intcode.output.pop(0)
        )


class Network:

    def __init__(self, data):
        self.nodes = [
            Node(Intcode(list(map(int, data.split(",")))), x)
            for x in range(50)
        ]
        self.nat = None
        self.prev = None

    def send_to_node(self, dest, x, y):
        self.nodes[dest].messages.extend([x, y])

    def check_nat(self):
        return self.prev and self.prev[1] == self.nav[1]

    def update_nat(self):
        self.prev = self.nat


def main(data, part=None):
    network = Network(data)

    while True:
        idle = True
        for i, node in enumerate(network.nodes):
            # receive packet
            if node.messages:
                idle = False
                node.intcode.run_instructions(node.create_packet_from_queue())
            else:
                node.intcode.run_instructions(-1)

            # send packet
            while node.intcode.output:
                dest, x, y = node.prepare_packet()
                if dest == 255:
                    network.nat = (x, y)

                    if part == 1:
                        return y

                    break
                # add x, y to dest node's queue
                network.send_to_node(dest, x, y)

        if idle and network.nat:
            # restart activity
            nx, ny = network.nat
            network.send_to_node(0, nx, ny)

            if network.check_nat():
                return ny
            else:
                network.update_nat()


if __name__ == '__main__':
    print(f'Part 1 {main(lines[0], 1)}')
    print(f'Part 2 {main(lines[0], 2)}')
