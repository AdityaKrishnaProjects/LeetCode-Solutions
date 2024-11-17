def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    length = len(prices)
    total_profit = 0
    max_profit = 0

    for i in range(length-1):
        marginal_profit = prices[i+1] - prices[i]
        total_profit = total_profit + marginal_profit
        if total_profit < 0:
            total_profit = 0
        max_profit = max(max_profit, total_profit)

    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))