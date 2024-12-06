# def binToDec(s):
#     len_s = len(s)-1
#     mult_base = 2
#     num = 0 

#     for i in range(len_s, -1, -1):
#         num += int(s[i])*(mult_base**(len_s - i))

#     return num

# extremely long code but the logic is correct and it still operates in linear 
# time, should clean up code by a lot to make it more clean
# def addBinary(a, b):
#     """
#     :type a: str
#     :type b: str
#     :rtype: str
#     """
    
#     if int(a) >= int(b):
#         larger = a
#         smaller = b
#     else:
#         larger = b
#         smaller = a
#     l_index = len(larger)-1
#     s_index = len(smaller)-1
#     pot_bin = ""
#     carryover = 0

#     while l_index >= 0:
#         if s_index < 0:
#             if (int(larger[l_index]) + carryover) == 0:
#                 pot_bin = "0" + pot_bin
#                 carryover = 0
            
#             elif (int(larger[l_index]) + carryover) == 1:
#                 pot_bin = "1" + pot_bin
#                 carryover = 0
            
#             elif (int(larger[l_index]) + carryover) == 2:
#                 pot_bin = "0" + pot_bin
#                 carryover = 1

#             l_index -= 1
#             continue
        
#         if (int(larger[l_index]) + int(smaller[s_index]) + carryover) == 0:
#             pot_bin = "0" + pot_bin
#             carryover = 0
        
#         elif (int(larger[l_index]) + int(smaller[s_index]) + carryover)  == 1:
#             pot_bin = "1" + pot_bin
#             carryover = 0
        
#         elif (int(larger[l_index]) + int(smaller[s_index]) + carryover)  == 2:
#             pot_bin = "0" + pot_bin
#             carryover = 1

#         elif (int(larger[l_index]) + int(smaller[s_index]) + carryover)  == 3:
#             pot_bin = "1" + pot_bin
#             carryover = 1

#         l_index -= 1
#         s_index -= 1

#     if carryover == 1:
#         pot_bin = "1" + pot_bin

#     return pot_bin

# print(addBinary("11", "1"))
# print(addBinary("1010", "1011"))
# print(addBinary("111", "1010"))

def addBinary(a,b):
    """ 
    accepts strings
    returns strings
    """ 

    s = ""
    i = len(a)-1
    j = len(b)-1
    carryover = 0

    while (i >= 0) or (j >= 0) or carryover:
        if i >= 0:
            carryover += int(a[i])
            i -= 1
        if j >= 0:
            carryover += int(b[j])
            j -= 1
        s = str(carryover % 2) + s
        carryover //= 2

    return s