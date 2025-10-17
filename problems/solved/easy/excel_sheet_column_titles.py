def convertToTitle(columnNumber):
    res = ""

    num_to_letter = {i: chr(64 + i) for i in range(1, 26)}
    num_to_letter[0] = "Z"

    while columnNumber > 0:
        remainder = columnNumber%26
        
        res = num_to_letter[columnNumber%26] + res
        
        # removes a full 26 by removing 1 if remainder is 0
        if remainder == 0:
            columnNumber -= 1
        
        columnNumber //= 26

    return res

print(convertToTitle(26))
print(convertToTitle(27))
print(convertToTitle(701))
print(convertToTitle(702))
print(convertToTitle(703))