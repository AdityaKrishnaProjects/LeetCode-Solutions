# # implementation with just cleaning
# def isPalindrome(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
    
#     alphanumeric = set("qwertyuiopasdfghjklzxcvbnm1234567890")
#     cleaned_string = ""

#     for char in s.lower(): 
#         if char in alphanumeric: 
#             cleaned_string = cleaned_string + char

#     return cleaned_string == cleaned_string[::-1]

# print(isPalindrome("blahhalb"))
# print(isPalindrome("AOWUDH&@912379197"))

# implementation using two pointers
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
        
    length = len(s)
    start_pointer = 0
    end_pointer = length-1

    while start_pointer < end_pointer:
        while not s[start_pointer].isalnum() and start_pointer < end_pointer: 
            start_pointer += 1
        while not s[end_pointer].isalnum() and start_pointer < end_pointer:
            end_pointer -= 1
    
        if s[start_pointer].lower() != s[end_pointer].lower():
            return False
        
        start_pointer +=1
        end_pointer -= 1

    return True

print(isPalindrome("blahhalb"))
print(isPalindrome("AOWUDH&@912379197"))