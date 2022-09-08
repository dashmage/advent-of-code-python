## advent of code 2021
## https://adventofcode.com/2021
## day 02


def parse_input(lines):
    # change input from "forward 5\n down 3\n" to [(forward, 5), (down, 3)]
    return [(x.split()[0], x.split()[1]) for x in lines]


def part1(course):
    horizontal_pos = 0
    vertical_pos = 0

    # loop over each tuple in the course
    for direction, value in course:
        match direction:
            case "forward":
                horizontal_pos += int(value)
            case "down":
                vertical_pos += int(value)
            case "up":
                vertical_pos -= int(value)

    return horizontal_pos * vertical_pos


def part2(course):
    horizontal_pos = 0
    vertical_pos = 0
    aim = 0
    for direction, value in course:
        match direction:
            case "forward":
                horizontal_pos += int(value)
                vertical_pos += int(value) * aim
            case "down":
                aim += int(value)
            case "up":
                aim -= int(value)

    return horizontal_pos * vertical_pos
