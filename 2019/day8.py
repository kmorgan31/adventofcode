#!/usr/bin/python

from aocd import lines

from collections import Counter


def print_image(layers):
    for i, layer in enumerate(layers):
        print(f"Layer {i+1}")
        for img in layer:
            print(img)
        print("\n")


def apply_layers(image):
    # get the corresponding pixel on each layer
    for x in range(6):
        line = ""
        for y in range(25):
            pixels = [image[z][x][y] for z in range(100)]

            if "0" not in pixels and "1" in pixels:
                line += "1"
            elif "1" not in pixels and "0" in pixels:
                line += "0"
            elif pixels.index("0") < pixels.index("1"):
                line += "0"
            else:
                line += "1"
        print(line)


def calculate_score(layer):
    counter = Counter(sum(layer, []))
    return (counter['0'], counter['1'] * counter['2'])


def main(line, part=None):
    img_size = 25*6
    num_layers = len(line) // img_size

    image = []
    for x in range(num_layers):
        pixels = line[x*img_size:(x+1)*img_size]
        image.append([
            list(pixels[(i*25):(i+1)*25]) for i in range(6)
        ])

    if part == 1:
        return min(
            [calculate_score(layer) for layer in image], key=lambda x: x[0]
        )
    elif part == 2:
        apply_layers(image)


if __name__ == '__main__':
    # print(f'Part 1 {main(EXAMPLE_2, 2)}')
    # print(f'Part 1 {main(lines[0], 1)}')
    print(f'Part 2 {main(lines[0], 2)}')
