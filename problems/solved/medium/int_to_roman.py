# # Pretty bad
# def intToRoman(num):
#     """
#     :type num: int
#     :rtype: str
#     """
        
#     int_to_rom = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
#     s = ""
#     num_str = str(num)
#     decimal_power = 10**(len(num_str)-1)

#     for char in num_str:
#         cur_num = int(char)

#         if cur_num >= 5:
#             cur_num -= 5

#             if cur_num == 4:
#                 s += (int_to_rom[decimal_power] + int_to_rom[decimal_power*10])
#             else:
#                 s += (int_to_rom[decimal_power*5] + (int_to_rom[decimal_power] * cur_num))
#         else:
#             if cur_num == 4:
#                 s += (int_to_rom[decimal_power] + int_to_rom[decimal_power*5])
#             else:
#                 s += (int_to_rom[decimal_power] * cur_num)

#         decimal_power //= 10

#     return s

# print(intToRoman(3749))
# print(intToRoman(58))
# print(intToRoman(1994))
# print(intToRoman(4))

# Looks cleaner but performs the same
def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """

    r = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], 
    [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]

    result = ""

    for i in range(len(r)):
        if num == 0:
                break

        while num >= r[i][0]:
            num -= r[i][0]
            result += r[i][1]

    return result

print(intToRoman(3749))
print(intToRoman(58))
print(intToRoman(1994))
print(intToRoman(4))