#!/usr/bin/python

from aocd import lines

EXAMPLE = [
    "cpy 2 a",
    "tgl a",
    "tgl a",
    "tgl a",
    "cpy 1 a",
    "dec a",
    "dec a"
]


def split_instruction(line):
    line = line.split()
    return line[0], line[1:]


def is_number(num):
    try:
        int(num)
    except:
        return False
    return True


def can_multiply(data, i):
    if (
        data[i-1].startswith("cpy") and
        data[i+1].startswith("dec") and
        data[i+2].startswith("jnz") and
        data[i+3].startswith("dec") and
        data[i+4].startswith("jnz")
    ):
        cx, cy = split_instruction(data[i-1])[1]
        dx1 = split_instruction(data[i+1])[1][0]
        jx1, jy1 = split_instruction(data[i+2])[1]
        dx2 = split_instruction(data[i+3])[1][0]
        jx2, jy2 = split_instruction(data[i+4])[1]

        if (cy == dx1 == jx1 and dx2 == jx2 and
                jy1 == "-2" and jy2 == "-5"):
            return (cx, dx1, dx2)


def get_val(x, registers):
    return int(x) if is_number(x) else registers[x]


def main(data, part=None):
    registers = {x: 0 for x in ["a", "b", "c", "d"]}

    if part == 1:
        registers["a"] = 7
    elif part == 2:
        registers["a"] = 12

    i = 0
    while i < len(data):
        action, nums = split_instruction(data[i])

        try:
            if action == "cpy":
                x, y = nums
                registers[y] = get_val(x, registers)
            if action == "inc":
                if part == 2:
                    mul = can_multiply(data, i)
                    if mul:
                        # y = cx * dx2; dx1 and dx2 set to 0
                        registers[nums[0]] += (
                            get_val(mul[0], registers) * get_val(mul[2], registers)
                        )
                        registers[mul[1]] = 0
                        registers[mul[2]] = 0

                        i += 5
                        continue

                registers[nums[0]] += 1
            if action == "dec":
                registers[nums[0]] -= 1
            if action == "jnz":
                x, y = nums
                if get_val(x, registers) != 0:
                    i += get_val(y, registers)
                    continue
            if action == "tgl":
                val = get_val(nums[0], registers)

                naction, nnums = split_instruction(data[val+i])
                if len(nnums) == 1:
                    command = "dec" if naction == "inc" else "inc"
                    nline = f"{command} {nnums[0]}"
                else:
                    command = "cpy" if naction == "jnz" else "jnz"
                    nline = f"{command} {nnums[0]} {nnums[1]}"
                data[val+i] = nline

        except:
            pass

        i += 1
    return registers['a']


if __name__ == '__main__':
    # print(f'EXAMPLE {main(EXAMPLE)}')
    print(f'Part 1 {main(lines, 1)}')
    print(f'Part 2 {main(lines, 2)}')
