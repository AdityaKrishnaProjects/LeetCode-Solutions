# decent solution. O(n).
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    
    r_str = ""
    word = ""
    curr_index = len(s)-1

    while curr_index >= 0:
        while s[curr_index] != " " and curr_index >= 0:
            word = s[curr_index] + word
            curr_index -= 1
        else:
            if word != "":
                r_str = r_str + word + " "
                word = ""

        curr_index -= 1

    return r_str[:len(r_str)-1]

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))
print(reverseWords(" "))