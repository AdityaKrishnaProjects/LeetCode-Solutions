# happy with this solution as its O(n) and constant space. Could have done 
# something like setting markers at start of column that it needs to be zerod 
# out, but its the same complexity.
def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    N = len(matrix)
    N2 = len(matrix[0])

    for i in range(N):
        for j in range(N2):
            if matrix[i][j] == 0:
                for x in range(N2):
                    if matrix[i][x] != 0:
                        matrix[i][x] = "r"
                for y in range(N):
                    if matrix[y][j] != 0:
                        matrix[y][j] = "r"

    for i in range(N):
        for j in range(N2):
            if matrix[i][j] == "r":
                matrix[i][j] = 0

    print(matrix)

setZeroes([[1,1,1],[1,0,1],[1,1,1]])
setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])