def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    
    N = len(matrix) # vertical length
    M = len(matrix[0]) # horizontal length

    r_list = []

    i = [0,0]
    total_pol = 1
    vert_pol = 1
    hori_pol = 1

    while (M != 0) and (N != 0):
        if total_pol > 0:
            for k in range(M):
                r_list.append(matrix[i[0]][i[1]])
                if k != M-1:
                    i[1] += 1*hori_pol
                else:
                    i[0] += 1*vert_pol
            hori_pol *= -1
            total_pol *= -1
            N -= 1
        else:
            for k in range(N):
                r_list.append(matrix[i[0]][i[1]])
                if k != N-1:
                    i[0] += 1*vert_pol
                else:
                    i[1] += 1*hori_pol
            vert_pol *= -1
            total_pol *= -1
            M -= 1

    return r_list

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(spiralOrder([[0]]))
print(spiralOrder([[1,2]]))