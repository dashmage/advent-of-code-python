## advent of code 2021
## https://adventofcode.com/2021
## day 05

SIZE = 1000
# from pprint import pprint as pp


def parse_input(lines):
    """
    Returns vent line coordinates as a list of tuples each containing 2 tuples for the set of 2 coordinates
    Ex:
        [((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((5, 5), (8, 2))]
    """
    # Go from "9,0 -> 9,5" to "9,0,9,5"
    vent_line_coords = [line.replace(" -> ", ",") for line in lines]
    for i, el in enumerate(vent_line_coords):
        # "9,0,9,5" -> ["9", "0", "9", "5"]
        coords = el.split(",")
        # tuple1 -> (9, 0)
        # tuple2 -> (9, 5)
        tuple1 = int(coords[0]), int(coords[1])
        tuple2 = int(coords[2]), int(coords[3])
        # Replace "9,0,9,5" with "((9, 0), (9, 5))"
        vent_line_coords[i] = tuple1, tuple2
    return vent_line_coords


def mark_grid(grid, vent_line_coords):
    """Mark grid positions as per horizontal or vertical vent lines coordinates"""
    for coord_set in vent_line_coords:
        x1 = coord_set[0][0]
        y1 = coord_set[0][1]
        x2 = coord_set[1][0]
        y2 = coord_set[1][1]

        # check only horizontal or vertical lines
        if x1 == x2 or y1 == y2:
            # if line is vertical
            if x1 == x2:
                if y1 > y2:
                    y1, y2 = y2, y1
                # print(f"({x1}, {y1}) -> ({x2}, {y2})")
                for y in range(y1, y2 + 1):
                    if grid[y][x1] == ".":
                        grid[y][x1] = 1
                    else:
                        grid[y][x1] += 1
                        # print grid nicely formatted
                        # grid[y][x1] = str(int(grid[y][x1]) + 1)

            # if line is horizontal
            if y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                # print(f"({x1}, {y1}) -> ({x2}, {y2})")
                for x in range(x1, x2 + 1):
                    if grid[y1][x] == ".":
                        grid[y1][x] = 1
                    else:
                        grid[y1][x] += 1
                        # print grid nicely formatted
                        # grid[y1][x] = str(int(grid[y1][x]) + 1)
            # pp(grid)
    return grid


def part1(vent_line_coords):
    grid = [["." for i in range(SIZE)] for j in range(SIZE)]
    grid = mark_grid(grid, vent_line_coords)
    high_overlap = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if isinstance(grid[i][j], int) and grid[i][j] >= 2:
                high_overlap += 1
    print(high_overlap)


def part2(vent_line_coords):
    pass
