# # recursive solution. Checks if prefix in dictionary for all prefix lengths, if 
# # so calls function on string[prefix:]. Returns true if empty string is found, 
# # false otherwise. 
# def wordBreak(s, wordDict):
    
#     wordDict = set(wordDict)
#     cache = {}

#     def checkAllFrames(s):
#         N = len(s)

#         if s in cache:
#             return cache[s]
#         if s == "":
#             return True

#         for i in range(1, N+1):
#             if s[:i] in wordDict and checkAllFrames(s[i:]):
#                 cache[s] = True
#                 return True

#         cache[s] = False
#         return False
    
#     return checkAllFrames(s)

# Approach doesn't use recursive calls, and instead goes bottom up to check if a
# break up to a certain index is possible. If so then we mark that index as 
# True and break and move to the next index i.
def wordBreak(s, wordDict):

    wordDict = set(wordDict)
    N = len(s)
    dp = [False] * (N+1)
    dp[0] = True

    for i in range(1, N+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    
    return dp[N]


print(wordBreak("leetcode", ["leet","code"]))
print(wordBreak("applepenapple", ["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(wordBreak("abcd", ["a","abc","b","cd"]))