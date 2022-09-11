day = "04"
input_file_name = f"2021/{day}/input.txt"


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
    return None


def score(boards, board_index, num):
    """Returns final score of winning board given board_index and last number called (num)"""
    sum_unmarked = 0
    for i in range(5):
        for j in range(5):
            if list(boards[board_index][i].values())[j] == False:
                sum_unmarked += int(list(boards[board_index][i])[j])
    return sum_unmarked * int(num)


with open(input_file_name, encoding="utf-8") as f:
    lines = f.read().split("\n")
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

    last_one = False
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
        while board_index is not None:
            board_count = len(boards)
            board_index = check_winner(boards, board_count)
            print(num, board_index)
            # if winning board is found, remove it
            if board_index is not None:
                if len(boards) > 1:
                    del boards[board_index]
                else:
                    print(score(boards, 0, num))
                    last_one = True
                    break
        if last_one:
            break
