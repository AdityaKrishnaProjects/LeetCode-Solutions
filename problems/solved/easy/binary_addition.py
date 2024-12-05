def binToDec(s):
    len_s = len(s)-1
    mult_base = 2
    num = 0 

    for i in range(len_s, -1, -1):
        num += int(s[i])*(mult_base**(len_s - i))

    return num

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    
    len_a = len(a)-1
    len_b = len(b)-1

    curr_index = max(len_a, len_b)
    carryover = 0
    r_str = ""

    while curr_index >= 0:
        

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))