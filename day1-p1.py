"""
Link: https://adventofcode.com/2021/day/1
"""

count_increasing = 0
input_file = "inputs/day1-input"

with open(input_file, encoding="utf-8") as depth_values:
    prev_val = -1

    for val in depth_values:
        current_val = int(val)
        print(current_val, end="")

        # For the very first depth value
        if prev_val == -1:
            print(" (N/A - no previous measurement)")

        # When the current value is increasing over prev one
        elif current_val > prev_val:
            count_increasing += 1
            print(" (increased)")

        # Otherwise current value is decreasing
        else:
            print(" (decreased)")

        # Re-assign previous value to current one
        prev_val = current_val

print("\nMeasurements larger than previous one: ", count_increasing)
