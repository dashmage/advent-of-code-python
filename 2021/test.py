day = "04"
input_file_name = f"2021/{day}/example_input.txt"

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
    # print(list(boards[0][2])[3])
    # print(drawn_nums)
    board_count += 1
    board_index = 0
    for num in drawn_nums:
        # mark each drawn number on all boards
        while board_index < board_count:
            for i in range(5):
                for j in range(5):
                    if list(boards[board_index][i])[j] == num:
                        boards[board_index][i][num] = True
            board_index += 1

    print(boards[0])
