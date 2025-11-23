# In place DP (can keep track of intermediate solutions bottom up)
def uniquePathsWithObstacles(obstacleGrid):
    N = len(obstacleGrid)
    M = len(obstacleGrid[0])

    for i in range(N):
        for j in range(M):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            elif i == 0 and j == 0:
                obstacleGrid[i][j] = 1
            else:
                obstacleGrid[i][j] += (obstacleGrid[i-1][j] if i > 0 else 0) + (obstacleGrid[i][j-1] if j > 0 else 0)

    return obstacleGrid[N-1][M-1]

print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(uniquePathsWithObstacles([[0,1],[0,0]]))
print(uniquePathsWithObstacles([[0,1],[1,0]]))
print(uniquePathsWithObstacles([[0]]))
print(uniquePathsWithObstacles([[1]]))