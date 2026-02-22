"""Compute the maximum profit that can be obtained by buying and selling a stock at most once."""


def compute_max_profit(prices: list[int]) -> int:
    length = len(prices)
    total_profit = 0
    max_profit = 0

    for i in range(length - 1):
        marginal_profit = prices[i + 1] - prices[i]
        total_profit = total_profit + marginal_profit
        if total_profit < 0:
            total_profit = 0
        max_profit = max(max_profit, total_profit)

    return max_profit


print(compute_max_profit([7, 1, 5, 3, 6, 4]))
print(compute_max_profit([7, 6, 4, 3, 1]))
