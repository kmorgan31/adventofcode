#!/usr/bin/python

if __name__ == '__main__':
    # simplification of what's happening in the input
    target = 15 * 170
    n = 1
    while n < target:
        if n % 2 == 0:
            n = n*2 + 1
        else:
            n *= 2

    print(f'Part 1 {n - target}')
