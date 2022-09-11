## advent of code 2021
## https://adventofcode.com/2021
## day 04


def parse_input(lines):
    drawn_nums = lines[0].split(",")
    boards = [[]]
    d = {}
    board_count = 0
    for line in lines[2:]:
        d = {}
        if line == "":
            board_count += 1
            boards.append([])
            continue
        else:
            for num in line.split():
                d[num] = False
            boards[board_count].append(d)

    return drawn_nums, boards


def check_winner(boards, board_count):
    """Returns board_index if winning board is found. Else returns None"""
    board_index = 0

    # loop through all boards to check for winner
    while board_index < board_count:
        # check for completed row
        for i in range(5):
            for j in range(5):
                if list(boards[board_index][i].values())[j] == False:
                    # break and check next row
                    break

                # reached end of row
                if j == 4:
                    # board is winner!
                    return board_index

        # check for completed column
        for i in range(5):
            for j in range(5):
                if list(boards[board_index][j].values())[i] == False:
                    # break and check next column
                    break

                # reached end of column
                if j == 4:
                    # board is winner!
                    return board_index
        board_index += 1
    # No winner found after checking all boards
    return None


def score(boards, board_index, num):
    """Returns final score of winning board given board_index and last number called (num)"""
    sum_unmarked = 0
    for i in range(5):
        for j in range(5):
            if list(boards[board_index][i].values())[j] == False:
                sum_unmarked += int(list(boards[board_index][i])[j])
    return sum_unmarked * int(num)


def part1(drawn_nums, boards):
    # accessed as boards[board_number][row_number][col_number]
    # list(boards[0][2])[3]             --> returns number at r2 c3 for board #0
    # list(boards[0][2].values())[3]    --> returns whether number is drawn or not (True/False)

    board_count = len(boards)
    board_index = 0

    for num in drawn_nums:
        # mark each drawn number on all boards
        while board_index < board_count:
            for i in range(5):
                for j in range(5):
                    if list(boards[board_index][i])[j] == num:
                        boards[board_index][i][num] = True
            board_index += 1

        board_index = check_winner(boards, board_count)
        # break out of loop if board_index is not None
        # meaning winner has been found
        if board_index is not None:
            break

        board_index = 0

    # once winner is found, calculate sum of all unmarked numbers on that board
    return score(boards, board_index, num)


def part2(drawn_nums, boards):
    for num in drawn_nums:
        board_count = len(boards)
        board_index = 0
        # mark each drawn number on all boards
        while board_index < board_count:
            for i in range(5):
                for j in range(5):
                    if list(boards[board_index][i])[j] == num:
                        boards[board_index][i][num] = True
            board_index += 1

        # delete all winning boards for drawn number
        # with certain drawn numbers, multiple boards can be eliminated
        while board_index is not None:
            board_count = len(boards)
            board_index = check_winner(boards, board_count)
            # if winning board is found, remove it
            if board_index is not None:
                if len(boards) > 1:
                    del boards[board_index]
                else:
                    return score(boards, 0, num)
