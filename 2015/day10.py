#!/usr/bin/python


EXAMPLE = "1"
INPUT = "3113322113"


def main(word, rounds):

    for x in range(rounds):
        nums = []

        current_num, count = None, 0
        for i in range(len(word)):
            if word[i] != current_num:
                if count > 0:
                    nums.append((count, current_num))

                current_num, count = word[i], 1
            else:
                count += 1
        if count > 0:
            nums.append((count, current_num))

        word = ''.join([f"{n[0]}{n[1]}" for n in nums])
    return len(word)


if __name__ == '__main__':
    # print(f'Example {main(EXAMPLE, 5)}')
    print(f'Part 1 {main(INPUT, 40)}')
    print(f'Part 2 {main(INPUT, 50)}')
