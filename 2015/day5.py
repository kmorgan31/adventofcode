#!/usr/bin/python

from aocd import lines


def is_nice_1(word):
    if any(x in word for x in ["ab", "cd", "pq", "xy"]):
        return False
    if sum(word.count(x) for x in "aeiou") < 3:
        return False
    if not any(word[i] == word[i+1] for i in range(len(word)-1)):
        return False
    return True


def is_nice_2(word):
    found = False
    for i in range(0, len(word)-1):
        if word[i:i+2] in word[i+2:]:
            found = True
            break
    if not found: return False
    found = False
    for i in range(0, len(word)-2):
        x, y, z = word[i:i+3]
        if x == z:
            found = True
            break
    if not found: return False
    return True


def main(data, part=None):
    num_nice = 0
    for word in data:
        if part == 1 and is_nice_1(word):
            num_nice += 1
        elif part == 2 and is_nice_2(word):
            num_nice += 1
    return num_nice


if __name__ == '__main__':
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
