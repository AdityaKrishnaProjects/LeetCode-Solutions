# recursive approach. Creates tree of possible minimums for current amount and 
# index, caches calculated values and reuses them. n x m recursive cases, and 
# each call does O(1) operations which makes algorithm O(m*n).
def coinChange(coins, amount):

    N = len(coins)
    cache = [[None] * N for _ in range(amount + 1)]

    def coinAllocator(i, amount):
        # base cases
        if amount == 0:
            return 0
        if amount < 0 or i < 0:
            return float("inf")
        
        # cache
        if cache[amount][i] is not None:
            return cache[amount][i]

        # take, decrements amount
        take = 1 + coinAllocator(i, amount - coins[i])
        
        # skip, decrements index
        skip = coinAllocator(i-1, amount)

        cache[amount][i] = min(take, skip)
        return cache[amount][i]
    
    val = coinAllocator(N-1, amount)
    return -1 if val == float("inf") else val

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([2,3,5], 11))