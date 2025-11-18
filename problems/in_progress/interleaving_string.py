def isInterleave(s1, s2, s3):

    N, M, K = len(s1), len(s2), len(s3)

    # check if covering is possible
    if N + M != K:
        return False

    # we want to pass in indices of what we have already taken off of the final 
    # set and what we have taken off of our strings respectively. Once we have 
    # states that we know result in s3 reducing we can continue search from 
    # there. If all indices are 0 then we are done.
    def canTake(N, M, K):
        if (N + M + K) == 0:
            return True

    canTake(N, M, K)

print(isInterleave("","",""))


"""
subsets must form a disjoint cover of the set

subsets must interleave one after the other
    allowed to start with subset from either set
    gaurantees that subsets of S and T will be the same size or off by 1

can not include empty string as valid subset for string that is not empty




"""