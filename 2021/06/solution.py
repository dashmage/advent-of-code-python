## advent of code 2021
## https://adventofcode.com/2021
## day 06


def parse_input(lines):
    return list(map(int, lines[0].split(",")))


def part1(fish_timers):
    days = 80
    # day_index = 0
    # print(f"Initial state: {fish_timers}")
    for i in range(days):
        for i, age in enumerate(fish_timers):
            fish_timers[i] -= 1
            if age == 0:
                fish_timers.append(9)
                fish_timers[i] = 6
        # day_index += 1
        # print(f"After {day_index} days: {fish_timers}")
    return len(fish_timers)


def part2(data):
    pass
