#!/usr/bin/python

from aocd import lines

import re

EXAMPLE = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in"
]

REQUIRED_FIELDS = [
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
]


def print_passport(passport):
    print(passport)
    # print([(k, passport.get(k)) for k in REQUIRED_FIELDS + ["cid"]])


def check_validity(passport, part):

    def valid_height(hgt):
        if passport["hgt"][-2:] not in ["cm", "in"]:
            return False

        height, uom = int(passport["hgt"][:-2]), passport["hgt"][-2:]
        if uom == "cm" and not (150 <= height <= 193):
            return False
        if uom == "in" and not (59 <= height <= 76):
            return False
        return True

    if not all(field in passport for field in REQUIRED_FIELDS):
        return False
    if part == 1:
        return True

    # part 2
    # validate years
    if not (1920 <= int(passport["byr"]) <= 2002):
        return False
    if not (2010 <= int(passport["iyr"]) <= 2020):
        return False
    if not (2020 <= int(passport["eyr"]) <= 2030):
        return False
    # height
    if not valid_height(passport["hgt"]):
        return False

    # hair colour
    if not re.search(r"^#([0-9a-f]){6}$", passport["hcl"]):
        return False
    # eye colour
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    # passport id
    if not re.search(r"^\d{9}$", passport["pid"]):
        return False

    return True


def main(data, part=None):

    valid = 0

    passport = {}
    for line in data:
        if not line:
            # check for all keys
            if check_validity(passport, part):
                valid += 1

            # clear for next passport
            passport = {}
            continue

        for x in line.split():
            k, v = x.split(":")
            passport[k] = v

    if passport and check_validity(passport, part):
        valid += 1

    return valid


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE, 1)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
