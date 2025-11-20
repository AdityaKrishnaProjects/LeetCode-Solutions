def isInterleave(s1, s2, s3):

    N, M, K = len(s1), len(s2), len(s3)

    # check if covering is possible
    if N + M != K:
        return False

    cache = {}

    # we want to pass in indices of what we have already taken off of the final 
    # set and what we have taken off of our strings respectively. Once we have 
    # states that we know result in s3 reducing we can continue search from 
    # there. If all indices are 0 then we are done.
    def canTake(N, M, K):
        if (N, M, K) in cache:
            return cache[(N, M, K)]
        
        if (N + M + K) == 0:
            return True

        res = False

        if N > 0 and s1[N-1:N] == s3[K-1:K] and canTake(N-1, M, K-1):
            res = True

        if M > 0 and s2[M-1:M] == s3[K-1:K] and canTake(N, M-1, K-1):
            res = True

        cache[(N, M, K)] = res
        return res

    return canTake(N, M, K)

print(isInterleave("","",""))
print(isInterleave("","a","a"))
print(isInterleave("aaa","aa","aa"))
print(isInterleave("aabcc","dbbca","aadbbcbcac"))
print(isInterleave("aabcc","dbbca","aadbbbaccc"))

"""
subsets must form a disjoint cover of the set

subsets must interleave one after the other
    allowed to start with subset from either set
    gaurantees that subsets of S and T will be the same size or off by 1

can not include empty string as valid subset for string that is not empty

Only need to return true, so need to return the actual substrings. This means 
when we iterate through the strings to select extra chars to add in at each 
interval, we don't have to care if we select chars from the same string more 
than once, as this would be equivalent to just selecting a larger substring 
rather than a single char. This means at every step we have two choices to 
consider, taking a char from the end of the s1 or from the end of s2 according 
to whatever horizon we have fed the function. This makes the algorthimic 
complexity equal to the total number of left edge substring combinations.
"""