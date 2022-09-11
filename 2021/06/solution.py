## advent of code 2021
## https://adventofcode.com/2021
## day 06


def parse_input(lines):
    return list(map(int, lines[0].split(",")))


def part1(fish_timers):
    days = 80
    for day_index in range(1, days + 1):
        for i, age in enumerate(fish_timers):
            if age == 0:
                fish_timers.append(9)
                fish_timers[i] = 7
        fish_timers = list(map(lambda x: x - 1, fish_timers))
        # print(f"After {day_index} days: {sorted(fish_timers)}, {len(fish_timers)}")
    return len(list(fish_timers))


def part2(fish_timers):
    days = 256
    count_nums = [fish_timers.count(x) for x in range(9)]
    fish_timers_d = dict(zip(range(9), count_nums))
    zero_extra = 0
    for day_index in range(days):
        # print(day_index + 1, fish_timers_d)
        for i in range(8):
            fish_timers_d[i] = fish_timers_d[i + 1]
            if i == 6:
                fish_timers_d[6] += zero_extra
        if zero_extra:
            fish_timers_d[8] = zero_extra
            zero_extra = 0
        else:
            fish_timers_d[8] = 0
        # print(day_index + 1, fish_timers_d)
        zero_extra = fish_timers_d[0]
    return sum(fish_timers_d.values())
