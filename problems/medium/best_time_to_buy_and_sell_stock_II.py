# Unbelievably straightforward
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    final_index = len(prices)-1
    total_profit = 0

    for i in range(final_index):
        if prices[i] < prices[i+1]:
            total_profit += prices[i+1] - prices[i]

    return total_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))