# backtracking
def exist(board, word):
    N = len(board)
    M = len(board[0])
    K = len(word)
    found = False
    starts = [(i, j) for i in range(N) for j in range(M) if board[i][j] == word[0]]


    def search(i, j, count):
        nonlocal found
        
        if found:
            return

        if count == K:
            found = True
            return

        if not (0 <= i < N and 0 <= j < M):
            return

        if board[i][j] != word[count]:
            return
                
        temp = board[i][j]
        board[i][j] = "#"
        
        search(i-1, j, count+1)
        search(i+1, j, count+1)
        search(i, j-1, count+1)
        search(i, j+1, count+1)

        board[i][j] = temp

    for i, j in starts:
        search(i, j, 0)
        if found:
            return True
    
    return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))