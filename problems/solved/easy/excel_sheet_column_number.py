# make chars into their num values and then use base26 to translate
def titleToNumber(columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    
    res = 0
    let_to_num = {chr(i): i - 64 for i in range(65, 91)}

    for i in range(1, len(columnTitle)+1):
        res += let_to_num[columnTitle[-i]] * (26**(i-1))

    return res

print(titleToNumber("ZY"))