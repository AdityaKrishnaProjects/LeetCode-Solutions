# pretty easy one
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else: 
            digits[i] = 0

    digits[0] = 1
    digits.append(0)

    return digits

print(plusOne([1,2,3,4]))
print(plusOne([1,2,3,9]))
print(plusOne([1,2,9,9]))
print(plusOne([1,9,9,9]))
print(plusOne([9,9,9,9]))
print(plusOne([0]))
print(plusOne([9]))