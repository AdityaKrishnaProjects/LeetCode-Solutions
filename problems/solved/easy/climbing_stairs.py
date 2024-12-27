# babys first memoization
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    
    memo = [0] * (n+1)

    def countSteps(n):
        if n == 0:
            return 1
        if n == 1: 
            return 1
        if memo[n]:
            return memo[n]

        memo[n] = countSteps(n-1) + countSteps(n-2)
        return memo[n]

    return countSteps(n)

print(climbStairs(4))