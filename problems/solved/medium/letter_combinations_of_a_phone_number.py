# Recursive call to keep generating prefixes. 
def letterCombinations(digits):

    r_list = []
    num_to_char = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], 
                   "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], 
                   "8": ['t', 'u', 'v'], "9": ['w', 'y', 'x', 'z']}

    def comboGenerator(digits, prefix):
        if digits == "":
            if prefix:
                r_list.append(prefix)
        else:
            num = digits[0]
            for char in num_to_char[num]:
                comboGenerator(digits[1:], prefix + char)

    comboGenerator(digits, "")

    return r_list
    
print(letterCombinations("23"))
print(letterCombinations(""))
print(letterCombinations("2"))
# print(letterCombinations())
# print(letterCombinations())