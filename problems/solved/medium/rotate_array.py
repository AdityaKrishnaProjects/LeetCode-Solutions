# following is commented code
# from math import gcd

# def rotate(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: None Do not return anything, modify nums in-place instead.
#     """
    
#     length = len(nums)
#     greatest_common_denominator = gcd(length, k)
#     temp = None

#     for starting_values in range(1, greatest_common_denominator+1):
#         print("starting value is", starting_values, "\n")
#         placeholder = None

#         for multiplier in range((length//greatest_common_denominator)+1):
#             print("multiplier is", multiplier, "\n")

#             index = ((starting_values + k * multiplier) % length)
#             print("index is", index)

#             if placeholder == None:
#                 placeholder = nums[index]
#                 print("placeholder was None, now is", placeholder)
#                 continue

#             temp = nums[index]
#             print("temp is", temp)

#             nums[index] = placeholder
#             print("nums[", index, "] is", nums[index], "\n")

#             placeholder = temp
#             print("placeholder is", temp)

#     print(nums)

# rotate([-1,-100,3,99], 2)
# rotate([1,2,3,4,5,6,7], 3)
# rotate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 4)

# following is uncommented code (imported gcd for simplicity), including print 
# statements to view results
from math import gcd

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    length = len(nums)
    greatest_common_denominator = gcd(length, k)
    temp = None

    for starting_values in range(1, greatest_common_denominator+1):
        placeholder = None

        for multiplier in range((length//greatest_common_denominator)+1):
            index = ((starting_values + k * multiplier) % length)

            if placeholder == None:
                placeholder = nums[index]
                continue

            temp = nums[index]
            nums[index] = placeholder
            placeholder = temp

    print(nums)

rotate([-1,-100,3,99], 2)
rotate([1,2,3,4,5,6,7], 3)
rotate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 4)

# # following is code with self implemented gcd and without print statement
# def gcd(self, a, b):
#     """
#     returns gcd
#     """

#     while b:
#         a, b = b, a%b
#     return a

# def rotate(self, nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: None Do not return anything, modify nums in-place instead.
#     """
    
#     length = len(nums)
#     greatest_common_denominator = self.gcd(length, k)
#     temp = None

#     for starting_values in range(1, greatest_common_denominator+1):
#         placeholder = None

#         for multiplier in range((length//greatest_common_denominator)+1):
#             index = ((starting_values + k * multiplier) % length)

#             if placeholder == None:
#                 placeholder = nums[index]
#                 continue

#             temp = nums[index]
#             nums[index] = placeholder
#             placeholder = temp