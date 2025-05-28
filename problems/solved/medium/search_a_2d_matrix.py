# binary search over flattened 2d matrix
def searchMatrix(matrix, target):

    M = len(matrix)
    N = len(matrix[0])

    left = 0
    right = (M * N) - 1

    while left <= right:
        middle = left + (right - left)//2
        if matrix[middle // N][middle % N] == target:
            return True
        if matrix[middle // N][middle % N] < target:
            left = middle + 1
        else:
            right = middle - 1

    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
# print(searchMatrix())
# print(searchMatrix())