# # very naive solution
# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
    
#     int_list = [0 for i in range(32)]
#     neg = 0
#     intl_i = len(int_list)-1
#     first_intl_i = intl_i

#     for num in nums:
#         bin_num = bin(num)
#         N = len(bin_num)
#         if bin_num[0] == "-":
#             neg += 1
#             bin_num = bin_num[3:N]
#         else:
#             bin_num = bin_num[2:N]
        
#         intl_i = len(int_list)-1
#         for i in range(len(bin_num)-1, -1, -1):
#             int_list[intl_i] += int(bin_num[i])
#             int_list[intl_i] %= 3
#             intl_i -= 1
#             first_intl_i = min(intl_i, first_intl_i)
        
#     first_intl_i += 1
#     r_bin = ""

#     while first_intl_i < 32:
#         r_bin += str(int_list[first_intl_i])
#         first_intl_i += 1

#     r_int = int(r_bin, 2)

#     neg %= 3
#     if neg != 0:
#         return r_int * -1

#     return r_int 

# # fast, efficient and readable version of the above code
# def singleNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
    
#     result = 0
#     for i in range(32):
#         # mask sets the bit under consideration
#         mask = 1 << i
#         count = 0
#         for num in nums:
#             # checks if current bit is 1 in current num
#             if num & mask:
#                 count += 1

#         # mod out bit count by 3
#         if count % 3:
#             # checks for negative bit
#             if i == 31:
#                 # if negative bit make number negative by subtracting 2^31
#                 result -= mask
#             else:
#                 # bitwise or current considered bit
#                 result ^= mask

#     return result

# print(singleNumber([2,2,3,2]))
# print(singleNumber([0,1,0,1,0,1,99]))
# print(singleNumber([0,1,0,1,0,1,-99]))
# print(singleNumber([0,-1,0,-1,0,-1,99]))