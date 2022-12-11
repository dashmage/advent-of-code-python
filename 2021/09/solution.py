## advent of code 2021
## https://adventofcode.com/2021
## day 09

from pprint import pprint as pp


def parse_input(lines):
    # get row, column size
    r_max = len(lines)
    c_max = len(lines[0])

    # join all input together into one line
    joined = "".join(lines)

    # initialize height_map as a 2d array indexed by i, j
    height_map = [[0 for _ in range(c_max)] for _ in range(r_max)]

    # populate height_map with values from joined input
    x = 0
    for i in range(r_max):
        for j in range(c_max):
            height_map[i][j] = joined[x]
            x += 1
    # pp(height_map)
    return height_map, r_max, c_max


def check_low_point(i, j, r_max, c_max, arr):
    """Check whether (i, j) location is a low point by comparing with adjacent locations. Return True if location provided is a low point. Otherwise False."""

    curr = arr[i][j]

    # x_jump --> j, y_jump --> i
    x_jump = 1 if j == 0 else -1
    y_jump = 1 if i == 0 else -1

    # checking if location is a corner
    if (i == 0 or i == r_max - 1) and (j == 0 or j == c_max - 1):
        if curr < arr[i][j + x_jump] and curr < arr[i + y_jump][j]:
            # print(i, j, "Corner low point!")
            return True

    # checking for top/bottom edge locations
    elif i == 0 or i == r_max - 1:
        if curr < arr[i][j - 1] and curr < arr[i][j + 1] and curr < arr[i + y_jump][j]:
            # print(i, j, "TB edge low point!")
            return True

    # checking for left/right edge locations
    elif j == 0 or j == c_max - 1:
        if curr < arr[i - 1][j] and curr < arr[i + 1][j] and curr < arr[i][j + x_jump]:
            # print(i, j, "LR edge low point!")
            return True

    # middle locations
    else:
        if (
            curr < arr[i][j - 1]
            and curr < arr[i][j + 1]
            and curr < arr[i - 1][j]
            and curr < arr[i + 1][j]
        ):
            # print(i, j, "Middle low point!")
            return True
    return False


def part1(height_map, r_max, c_max):
    low_points = []
    for i in range(r_max):
        for j in range(c_max):
            if check_low_point(i, j, r_max, c_max, height_map):
                low_points.append(height_map[i][j])

    risk_levels = (int(l) + 1 for l in low_points)
    return sum(risk_levels)


def basin_locations(arr, i, j, r_max, c_max):
    """Returns locations in a basin given i, j coordinates of low-point"""
    basin_points = []
    checked = {"l": False, "r": False, "t": False, "b": False}
    checked["t"] = True if i == 0 else False
    checked["b"] = True if i == r_max else False
    checked["l"] = True if j == 0 else False
    checked["r"] = True if j == c_max else False
    if not checked["l"] and arr[i][j - 1] != 9:
        basin_points.append({i, j})
        checked["l"] = True
    if not checked["r"] and arr[i][j + 1] != 9:
        basin_points.append({i, j})
        checked["r"] = True


def part2(height_map, r_max, c_max):
    low_points = []
    # i, j co-ordinate locations of low points
    lp_locs = []
    for i in range(r_max):
        for j in range(c_max):
            if check_low_point(i, j, r_max, c_max, height_map):
                low_points.append(height_map[i][j])
                lp_locs.append((i, j))
    print(lp_locs, low_points)
