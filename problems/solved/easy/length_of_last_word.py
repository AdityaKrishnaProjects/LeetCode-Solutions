def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    
    length = len(s)
    empty_char = " "
    count = 1
    letter_encountered = False

    for i in range(length-1, -1, -1):
        if not letter_encountered:
            if s[i] != empty_char:
                letter_encountered = True
        else:
            if s[i] != empty_char:
                count += 1
            else:
                return count

    return count

print(lengthOfLastWord("world  world  l  "))
print(lengthOfLastWord("world  world   "))
print(lengthOfLastWord("world  wor"))
print(lengthOfLastWord("we"))