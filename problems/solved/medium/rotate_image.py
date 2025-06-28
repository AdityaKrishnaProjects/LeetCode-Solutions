# orbit side length increase by factor of 2 each time, which means that number 
# of starting points for orbits increase by 2 each time. 
def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    N = len(matrix)

    # establish bounds for where leaps should start from
    N2 = (len(matrix)+1) // 2
    N3 = (len(matrix)) // 2

    for x in range(N2):
        for y in range(N3):
            # reflects each coordinate across horizontal and then diagonal axis
            # does so for 4 leaps
            current = matrix[x][y]
            matrix[x][y] = matrix[N-1-y][x]
            matrix[N-1-y][x] = matrix[N-1-x][N-1-y]
            matrix[N-1-x][N-1-y] = matrix[y][N-1-x]
            matrix[y][N-1-x] = current

print(rotate([[1,2,3],
              [4,5,6],
              [7,8,9]]))
print(rotate([[5,1,9,11],
              [2,4,8,10],
              [13,3,6,7],
              [15,14,12,16]]))
print(rotate([[1]]))
print(rotate([[42, 17, 93, 58, 36],
              [11, 84, 27, 69, 75],
              [63, 55,  6, 98, 21],
              [39, 88, 14,  3, 47],
              [70, 29, 91, 12, 66]]))

print(rotate([[34, 12, 76, 45, 90, 67, 23],
              [81, 54, 39, 28,  6, 14, 72],
              [59, 91, 33, 48, 19, 85, 62],
              [ 7, 26, 94, 11, 58, 41, 36],
              [88,  3, 65, 22, 17, 77, 53],
              [40, 97,  1, 32, 79, 25, 18],
              [70, 13,  9, 60, 84, 20, 99]]))  