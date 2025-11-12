# Uses existing structure to iteratively store necessary data
def minimumTotal(triangle):

    N = len(triangle)

    for i in range(N-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0][0]

print(
minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]),
minimumTotal([[-11]]))