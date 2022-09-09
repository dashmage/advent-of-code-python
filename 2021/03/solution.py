## advent of code 2021
## https://adventofcode.com/2021
## day 03


def parse_input(lines):
    return lines


def part1(binary_nums):
    gamma = ""
    epsilon = ""

    count_zero = [0 for _ in range(len(binary_nums[0]))]
    count_one = [0 for _ in range(len(binary_nums[0]))]

    for num in binary_nums:
        for i, bit in enumerate(num):
            if bit == "1":
                count_one[i] += 1
            else:
                count_zero[i] += 1

    for c0, c1 in zip(count_zero, count_one):
        if c0 > c1:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    pass
