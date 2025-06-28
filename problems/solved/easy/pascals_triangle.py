
def generate(numRows):
    res = [[0] * (i+1) for i in range(numRows)]

    for i in range(numRows):
        res[i][0] = 1
        res[i][-1] = 1

    for i in range(1, numRows-1):
        for j in range(i):
            res[i+1][j+1] = res[i][j] + res[i][j+1]
    
    return res

print(generate(6))