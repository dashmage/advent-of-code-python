"""
Link: https://adventofcode.com/2021/day/2
"""

horizontal_pos = 0
vertical_pos = 0

input_file = "inputs/day2-input"

with open(input_file, encoding="utf-8") as f:
    course = [(x.split()[0], x.split()[1]) for x in f]

    for direction, value in course:
        match direction:
            case "forward":
                horizontal_pos += int(value)
            case "down":
                vertical_pos += int(value)
            case "up":
                vertical_pos -= int(value)

print(f"Horizontal: {horizontal_pos}, Depth: {vertical_pos}")
print(f"Multiplied: {horizontal_pos * vertical_pos}")
