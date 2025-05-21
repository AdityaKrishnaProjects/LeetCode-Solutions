# Used sliding window and hashtable. We know that if we encounter a seen char 
# then we can start to slide the left part of the window until we see the same 
# char, as the substring that includes our current non-unique char must start 
# one char after the repeating char. From there we keep sliding the window till 
# we cover the whole array. We only move L at most N times, and we do constant 
# operations within the while loop, so we are doing at most O(2N) operations, 
# which makes our algorithm O(N).
def lengthOfLongestSubstring(s):
    
    L, longest= 0, 0
    seen = set()

    for R in range(len(s)):
        while s[R] in seen:
            seen.remove(s[L])
            L += 1
        seen.add(s[R])
        longest = max(longest, R - L + 1)

    return longest

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("cdd"))
print(lengthOfLongestSubstring("amqpcsrumjjufpu"))