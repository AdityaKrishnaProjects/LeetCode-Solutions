def reversePrefix(word, ch):
        for i, char in enumerate(word):
            if char == ch:
                return word[i::-1] + word[i+1:]

        return word

print(reversePrefix("abcdefd", "d"))
print(reversePrefix("xyxzxe", "z"))
print(reversePrefix("abcd", "z"))
print(reversePrefix("zez", "z"))