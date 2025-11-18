# multidimensional DP
def minPathSum(grid):
    N = len(grid)
    M = len(grid[0])

    for j in range(M):
        for i in range(N):
            if i-1 >= 0 and j-1 >= 0:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            elif i-1 >= 0:
                grid[i][j] += grid[i-1][j]
            elif j-1 >= 0:
                grid[i][j] += grid[i][j-1]

    return grid[N-1][M-1]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1,2,3],[4,5,6]]))
print(minPathSum([[1]]))