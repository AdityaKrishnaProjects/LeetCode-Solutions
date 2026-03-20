# hash map
def firstUniqChar(s):
    seen = {}

    for char in s:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1

    for i in range(len(s)):
        if seen[s[i]] == 1:
            return i

    return -1

    
        