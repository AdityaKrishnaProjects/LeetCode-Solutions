def getRow(rowIndex):
    
    if rowIndex == 0:
        return [1]

    res = [1]

    while rowIndex > 0:
        temp = []

        for k in range(len(res)+1):
            val = 0
            i, j = k-1, k
            if (i < 0) or (j > (len(res)-1)):
                val = 1
            else:
                val = res[i] + res[j]
            
            temp.append(val)

        res = temp

        rowIndex -= 1

    return res

print(getRow(1))

print(getRow(3))  