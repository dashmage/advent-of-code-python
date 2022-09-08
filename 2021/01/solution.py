## advent of code 2021
## https://adventofcode.com/2021
## day 01


def parse_input(lines):
    return [int(num) for num in lines]


def part1(depth_values):
    count_increase = 0
    prev_val = -1

    for val in depth_values:
        current_val = val

        if current_val > prev_val and prev_val != -1:
            count_increase += 1

        prev_val = current_val

    return count_increase


def part2(depth_values):
    count_increase = 0

    # left and right are used for the sliding window
    left = 0
    right = left + 3
    prev_sum = 0

    while right < len(depth_values):
        # Finding three measurement sum of sliding window
        current_sum = sum(depth_values[left:right])

        # Compare with previous sum
        if current_sum > prev_sum:
            count_increase += 1

        prev_sum = current_sum
        left += 1
        right += 1

    return count_increase
