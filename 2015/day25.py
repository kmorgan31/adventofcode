#!/usr/bin/python


def main(x, y):

    row = 2
    num = 20151125
    while True:
        for j in range(1, row+1):
            i = row+1 - j

            num = (num * 252533) % 33554393
            if i == x and j == y:
                return num

        row += 1


if __name__ == '__main__':
    print(f'Part 1 {main(2981, 3075)}')
