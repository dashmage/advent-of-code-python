"""
Link: https://adventofcode.com/2021/day/1
"""

count_increasing = 0

with open("inputs/day1-input", encoding="utf-8") as depth_values:
    prev_val = -1
    for val in depth_values:
        current_val = int(val)
        print(current_val, end="")
        if prev_val == -1:
            print(" (N/A - no previous measurement)")
        elif current_val > prev_val:
            count_increasing += 1
            print(" (increased)")
        else:
            print(" (decreased)")
        prev_val = current_val

print(count_increasing)
