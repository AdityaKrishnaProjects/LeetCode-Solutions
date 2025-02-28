# not very clean code but works cleanly. Could have been better if I used more 
# memory by having a set for each column, each row and each box and then 
# checking if the number is in any of the sets it could belong to, if not 
# adding it to those sets
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    # checks horizontals
    for i in range(9):
        seen = set()
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] not in seen:
                    seen.add(board[i][j])
                else:
                    return False
    
    # checks verticals
    for i in range(9):
        seen = set()
        for j in range(9):
            if board[j][i] != '.':
                if board[j][i] not in seen:
                    seen.add(board[j][i])
                else:
                    return False

    # checks 3x3s
    for m in range(3):
        for n in range(3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    if board[i+n*3][j+m*3] != '.':
                        if board[i+n*3][j+m*3] not in seen:
                            seen.add(board[i+n*3][j+m*3])
                        else:
                            return False

    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board3 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","9","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))
print(isValidSudoku(board2))
print(isValidSudoku(board3))