def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
        
    romtoint = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0
    read_index = len(s)-1

    while read_index >= 0:
        if (read_index > 0) and (romtoint[s[read_index-1]] < romtoint[s[read_index]]):
            total += romtoint[s[read_index]] - romtoint[s[read_index-1]]
            read_index -= 2
        else:
            total += romtoint[s[read_index]]
            read_index -= 1

    return total

print(romanToInt("CMIV"))
print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))