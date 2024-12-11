# sees everything once. Decent solution.
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    
    if numRows == 1:
        return s

    r_str = ""
    N = len(s)
    step = (numRows-1)*2
    step2 = 0

    for i in range(numRows):
        last = 1
        last_i = -1
        while i < N:
            if i != last_i:
                r_str += s[i]

            last_i = i
            if last == 1:
                i += step
            else:
                i += step2
            last *= -1

        step -= 2
        step2 += 2

    return r_str

print(convert("PAYPALISHIRING",3))
print(convert("PAYPALISHIRING",4))
print(convert("A",1))