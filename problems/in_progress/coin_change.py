def coinChange(coins, amount):

    N = len(coins)
    cache = [[False for _ in range(N)] for _ in range(amount)]

    def coinAllocator(i, amount, used):
        if amount == 0:
            return 1
        
        take, skip = float("inf"), float("inf")
        # take, decrements amount
        if amount - coins[i] >= 0:
            cache[amount - coins[i]][i] = coinAllocator(i, amount - coins[i], used+1)
            take = cache[amount - coins[i]][i]
        
        # skip, decrements index
        if i > 0:
            cache[amount][i-1] = coinAllocator(i-1, amount, used)
            skip = cache[amount][i-1]

        return min(take, skip)
    
    return coinAllocator(N-1, amount)

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))
print(coinChange([2,3,5], 11))