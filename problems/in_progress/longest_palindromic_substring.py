# naive solution (no checking if we have seen an answer before)
def longestPalindrome(s):
    """
    :type s: str (minimum length 1)
    :rtype: str
    """

    # normalizes all strings
    s_norm = ""
    for char in s:
        s_norm += char + "|"
    s_norm = "|" + s_norm

    # initialize potential longest to 1 (all strings contain one character)
    longest = [1, s_norm[1]]

    s_norm_len = len(s_norm)
    index = 1
    radius = 0

    while index < s_norm_len:
        while ((index - (radius+1)) > -1) and ((index + (radius+1)) < s_norm_len):
            # skip dummy values
            if s_norm[index - (radius+1)] == "|":
                radius += 1
                continue

            if s_norm[index - (radius+1)] == s_norm[index + (radius+1)]:
                radius += 1
            else:
                break

        if radius > longest[0]:
            if (radius % 2) == 0:
                longest = [radius, s[((index - radius)//2):(((index + radius)//2))]]
            else:
                longest = [radius, s[(index//2) - (radius//2):(index//2) + (radius//2) + 1]]
        radius = 0
        index += 1

    return longest[1]

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("bbbb"))
print(longestPalindrome("racecar"))