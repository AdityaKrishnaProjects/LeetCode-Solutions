# search after finding Os on boundary to add a marker to any O connected to a 
# boundary O as not surrounded. Then iterate through graph and change all 
# unmarked Os to Xs. 
def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """

    N = len(board)
    M = len(board[0])

    def search(i, j):
        if board[i][j] == "O":
            board[i][j] = "O2"
            if i > 0:
                search(i-1, j)
            if i < N-1:
                search(i+1, j)
            if j > 0:
                search(i, j-1)
            if j < M-1:
                search(i, j+1)

    for i in range(N):
        if board[i][0] == "O":
            search(i, 0)
        if board[i][M-1] == "O":
            search(i, M-1)

    for j in range(1, M-1):
        if board[0][j] == "O":
            search(0, j)
        if board[N-1][j] == "O":
            search(N-1, j)

    print(board)

    for i in range(N):
        for j in range(M):
            if board[i][j] == "O2":
                board[i][j] = "O"
            elif board[i][j] == "O":
                board[i][j] = "X"

    return board

print(solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
print(solve([["X"]]))
print(solve([["X","O","X"],["X","O","X"],["X","O","X"]]))
print(solve([["X","O","X"],["O","X","O"],["X","O","X"]]))