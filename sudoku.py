
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
            if j in [2, 5]:
                print(" | ", end="")
        print("\n")


def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j
    return None


def number_allowed(board, number, x, y):
    for i in range(len(board)):
        if i != x and board[i][y] == number:
            return False

    for j in range(len(board)):
        if j != y and board[x][j] == number:
            return False

    i_start_idx = (x//3)*3
    j_start_idx = (y//3)*3
    for i in range(i_start_idx, i_start_idx+3):
        for j in range(j_start_idx, j_start_idx+3):
            if board[i][j] == number:
                return False

    return True


def solve_sudoku(board):
    find = find_zero(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if number_allowed(board, i, row, col):
            board[row][col] = i
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False



