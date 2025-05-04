# seems long but happy with logic. Does so in one pass by editing the board live
# with equivalent values that tell us that the board needs to be updated on 
# second pass
def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    
    h = len(board)
    w = len(board[0])

    for i in range(h):
        for j in range(w):
            if board[i][j] == 0:
                # logic around dead cell
                count = 0
                for x in range(1, -2, -1):
                    for y in range(1, -2, -1):
                        row, col = [i-x,j-y]
                        if [row, col] == [i,j] or (row < 0) or (col < 0) or (row >= h) or (col >= w):
                            continue
                        elif board[row][col] == 1 or board[row][col] == 3:
                            count += 1     
                # set value to equivalent value that shows on next pass it will
                # be changed
                if count == 3:
                    board[i][j] = 2
            else:
                # logic around live cell
                count = 0

                for x in range(1, -2, -1):
                    for y in range(1, -2, -1):
                        row, col = [i-x,j-y]
                        if [row, col] == [i,j] or (row < 0) or (col < 0) or (row >= h) or (col >= w):
                            continue
                        elif board[row][col] == 1 or board[row][col] == 3:
                            count += 1     
                
                # set value to equivalent value that shows on next pass it will
                # be changed
                if (count < 2) or (count > 3):
                    board[i][j] = 3

    for i in range(h):
        for j in range(w):
            if board[i][j] == 2:
                board[i][j] = 1
            elif board[i][j] == 3:
                board[i][j] = 0

    print(board)

print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
print(gameOfLife([[1,1],[1,0]]))
print(gameOfLife([[1]]))