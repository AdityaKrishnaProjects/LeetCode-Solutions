# When an island is seen, recursively removes said island through search and 
# iterates island count. Could have used a hashset to not modify grid, which 
# would have also reduced operations, but would still be O(m x n).
def numIslands(grid):
    
    N = len(grid)
    N2 = len(grid[0])
    islands = 0

    def islandScourer(i, j):
        if  (i < 0) or (j < 0) or (i >= N) or (j >= N2) or (grid[i][j] == "0"):
            return
        grid[i][j] = "0"
        islandScourer(i+1, j)
        islandScourer(i, j+1)
        islandScourer(i-1, j)
        islandScourer(i, j-1)

    for i in range(N):
        for j in range(N2):
            if grid[i][j] == "1":
                islands += 1
                islandScourer(i, j)

    return islands

print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))