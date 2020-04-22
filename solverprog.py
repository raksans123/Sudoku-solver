board = [
    [7, 0, 9, 3, 8, 4, 2, 0, 6],
    [2, 4, 3, 0, 6, 0, 0, 8, 0],
    [8, 5, 6, 2, 1, 9, 4, 7, 0],
    [3, 0, 7, 5, 2, 0, 8, 1, 4],
    [1, 2, 5, 8, 4, 3, 0, 0, 7],
    [6, 8, 4, 1, 9, 7, 5, 3, 2],
    [4, 6, 8, 9, 7, 1, 3, 2, 5],
    [5, 7, 1, 4, 3, 2, 9, 6, 8],
    [9, 3, 2, 6, 5, 8, 7, 4, 1]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


print_board(board)
solve(board)
print("______________")
print_board(board)
