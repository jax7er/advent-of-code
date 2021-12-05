class Bingo(UserWarning):
    pass

def sum_unmarked(board, board_marked):
    return sum(
        n
        for row_i, line in enumerate(board)
        for col_i, n in enumerate(line)
        if not board_marked[row_i][col_i]
    )

def is_win(board_marked):
    return any(all(row) for row in board_marked) or any(all(col) for col in zip(*board_marked))

with open("input.txt") as f:
    data_str = f.read().strip()

numbers_str, *boards_str = data_str.split("\n\n")
numbers = [int(n_str) for n_str in numbers_str.split(",")]
boards = [[[int(n_str) for n_str in row.split()] for row in board_str.splitlines()] for board_str in boards_str]
boards_marked = [[[False] * len(row) for row in board] for board in boards]

try:
    for number in numbers:
        for board_i, board in enumerate(boards):
            for row_i, row in enumerate(board):
                for col_i, n in enumerate(row):
                    if n == number:
                        boards_marked[board_i][row_i][col_i] = True

            board_marked = boards_marked[board_i]
            score = number * sum_unmarked(board, board_marked)
            for row_marked in board_marked:
                if all(row_marked):
                    raise Bingo(score)
            for col_marked in zip(*board_marked):
                if all(col_marked):
                    raise Bingo(score)
except Bingo as bingo:
    print("part 1:", str(bingo))

try:
    for number in numbers:
        for board_i, board in enumerate(boards):
            for row_i, row in enumerate(board):
                for col_i, n in enumerate(row):
                    if n == number:
                        boards_marked[board_i][row_i][col_i] = True
        
        win_boards_i = [i for i, marked in enumerate(boards_marked) if is_win(marked)]  

        if len(win_boards_i) == len(boards) and is_win(boards_marked[0]):
            raise Bingo(number * sum_unmarked(boards[0], boards_marked[0]))

        boards = [b for i, b in enumerate(boards) if i not in win_boards_i]
        boards_marked = [b for i, b in enumerate(boards_marked) if i not in win_boards_i]
        
        if len(boards) == 1 and is_win(boards_marked[0]):
            raise Bingo(number * sum_unmarked(boards[0], boards_marked[0]))
except Bingo as bingo:
    print("part 2:", str(bingo))