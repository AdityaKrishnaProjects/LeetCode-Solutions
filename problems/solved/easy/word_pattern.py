# Feels a bit hacky. I like the space appending trick. 
def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    
    s += " "

    pattern_index = 0
    len_p = len(pattern)
    curr_word = ""
    char_to_word = {}
    word_to_char = {}

    for char in s:
        if char != " ":
            curr_word += char
            continue

        if pattern_index > len_p-1:
            return False 

        if curr_word in word_to_char:
            if word_to_char[curr_word] != pattern[pattern_index]:
                return False

        if pattern[pattern_index] in char_to_word:
            if char_to_word[pattern[pattern_index]] != curr_word:
                return False

        char_to_word[pattern[pattern_index]] = curr_word
        word_to_char[curr_word] = pattern[pattern_index]
        curr_word = ""
        pattern_index += 1

    return pattern_index == len_p

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat fish dog"))
print(wordPattern("aaaa", "dog cat cat dog"))
print(wordPattern("aaaa", "dog dog dog dog"))
print(wordPattern("abbat", "bog"))