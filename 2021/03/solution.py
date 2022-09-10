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


def part2(binary_nums):
    len_bin_num = len(binary_nums[0])

    co2_rating = 0
    oxygen_rating = 0

    # copy of binary nums tracking most common values
    binary_nums_more = binary_nums.copy()
    # copy of binary nums tracking least common values
    binary_nums_less = binary_nums.copy()

    # loop over all bits in binary num
    for bit_index in range(len_bin_num):
        # list to hold count for binary nums with most common bits
        count_zero_more = [0 for _ in range(len_bin_num)]
        count_one_more = [0 for _ in range(len_bin_num)]

        # list to hold count for binary nums with least common bits
        count_zero_less = [0 for _ in range(len_bin_num)]
        count_one_less = [0 for _ in range(len_bin_num)]

        # loop over all nums to figure out most common bit in each position
        # most common bits
        for num in binary_nums_more:
            for j, bit in enumerate(num):
                if bit == "1":
                    count_one_more[j] += 1
                else:
                    count_zero_more[j] += 1

        # least common bits
        for num in binary_nums_less:
            for j, bit in enumerate(num):
                if bit == "1":
                    count_one_less[j] += 1
                else:
                    count_zero_less[j] += 1

        # keep only binary nums with most common bit in bit_index position
        # if 0s > 1s in bit_index position, delete nums with 1 in that position
        i = 0
        if count_zero_more[bit_index] > count_one_more[bit_index]:
            # loop over all binary nums
            while i < len(binary_nums_more):
                if binary_nums_more[i][bit_index] == "1":
                    del binary_nums_more[i]
                    i -= 1
                i += 1

        else:
            while i < len(binary_nums_more):
                if binary_nums_more[i][bit_index] == "0":
                    del binary_nums_more[i]
                    i -= 1
                i += 1

        # keep only binary nums with least common bit in bit_index position
        # if 0s < 1s in bit_index position, delete nums with 1 in that position
        i = 0
        if count_zero_less[bit_index] <= count_one_less[bit_index]:
            # loop over all binary nums
            while i < len(binary_nums_less):
                if binary_nums_less[i][bit_index] == "1":
                    del binary_nums_less[i]
                    i -= 1
                i += 1

        else:
            while i < len(binary_nums_less):
                if binary_nums_less[i][bit_index] == "0":
                    del binary_nums_less[i]
                    i -= 1
                i += 1

        # if there's just one num remaining for binary nums tracking most common values
        if len(binary_nums_more) == 1:
            oxygen_rating = binary_nums_more[0]

        # if there's just one num remaining for binary nums tracking least common values
        if len(binary_nums_less) == 1:
            co2_rating = binary_nums_less[0]

        # break out of loop once both oxygen and co2 rating are non-zero
        if oxygen_rating and co2_rating:
            break

    return int(oxygen_rating, 2) * int(co2_rating, 2)
