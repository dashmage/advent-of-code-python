## advent of code 2022
## https://adventofcode.com/2022
## day 01

def parse_input(lines):
    """
    Returns a list containing the calories carried by each elf within sublists
    eg: [[1000, 2000], [3000], [4000, 5000]]
    """
    output = [[]]
    n = 0
    for cal in lines:
        if cal != '':
            output[n].append(int(cal))
        else:
            n += 1
            output.append([])
    return output


def part1(calories):
    # list containing the sum of calories of the food carried by each elf
    sum_calories = [sum(c) for c in calories]
    return max(sum_calories)

def part2(calories):
    sum_calories = [sum(c) for c in calories]
    return sum(sorted(sum_calories, reverse=True)[:3])