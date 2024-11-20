# Unfinished because I likely need to use dynamic programming to solve this 
# efficiently
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = s.len()

        if length == 1:
            return s[0]
        else:
            while length:
                for index in range(length-1):
                    return blah
                length -= 1
        
        return s[0]

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        length = s.len()