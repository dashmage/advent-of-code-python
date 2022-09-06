"""
https://adventofcode.com/2021/day/1#part2
"""

input_file = "inputs/day1-input"
count_increase = 0

with open(input_file, encoding="utf-8") as f:
    depth_values = [int(x) for x in list(f)]

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

print(count_increase)
