## advent of code 2021
## https://adventofcode.com/2021
## day 07


def parse_input(lines):
    return list(map(int, lines[0].split(",")))


def normal_fuel(all_pos, final_pos):
    """
    Calculates total fuel required to align with a given horizontal position
    all_pos: list of all horizontal positions
    final_pos: final horizontal position to align all others
    """
    return sum(map(lambda x: abs(x - final_pos), all_pos))


def cheapest_pos(all_pos, fuel_calculator):
    """Calculate the horizontal position with the cheapest fuel required"""
    # super inefficient approach where fuel is calculated for all positions instead of taking median
    # return min(
    #     fuel_calculator(all_pos, p) for p in range(min(all_pos), max(all_pos) + 1)
    # )
    if fuel_calculator == normal_fuel:
        all_pos.sort()
        n = len(all_pos)
        med = int(n / 2) if n % 2 == 0 else int((n + 1) / 2)
        return fuel_calculator(all_pos, all_pos[med])
    else:
        return min(
            fuel_calculator(all_pos, p) for p in range(min(all_pos), max(all_pos) + 1)
        )


def part1(all_pos):
    return cheapest_pos(all_pos, normal_fuel)


def cumulative_sum(n):
    return (n * (n + 1)) // 2


def expensive_fuel(all_pos, final_pos):
    """
    Calculates fuel where each step costs one extra fuel to move
    """
    return sum(map(lambda x: cumulative_sum(abs(x - final_pos)), all_pos))


def test(all_pos, final_pos):
    for p in all_pos:
        print(abs(p - final_pos))


def part2(all_pos):
    return cheapest_pos(all_pos, expensive_fuel)
