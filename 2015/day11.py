#!/usr/bin/python


INPUT = "vzbxkghb"

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def increment_password(word):
    word = list(word)

    i = len(word)-1
    while i >= 0:
        j = ALPHABET[(ALPHABET.index(word[i])+1) % len(ALPHABET)]
        word[i] = j
        if j != "a":
            break
        i -= 1

    return "".join(word[-8:])


def get_password(word):

    while True:
        if set(["i", "o", "l"]) & set(word):
            word = increment_password(word)
            continue

        i = 0
        found = False
        while i < len(ALPHABET)-2:
            if ALPHABET[i:i+3] in word:
                found = True
                break
            i += 1
        if not found:
            word = increment_password(word)
            continue

        i = 0
        pairs = []
        while i < len(word)-1:
            if word[i] == word[i+1]:
                pairs.append(word[i])
                i += 2
            else:
                i += 1
        if len(set(pairs)) < 2:
            word = increment_password(word)
            continue

        return word


if __name__ == '__main__':
    print(f'Part 1 {get_password(INPUT)}')      # vzbxxyzz
    print(f'Part 2 {get_password(increment_password("vzbxxyzz"))}')
