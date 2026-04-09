# Best Time to Buy and Sell Stock (LeetCode 121) — Easy
#
# You are given an array prices where prices[i] is the price of a given stock
# on the ith day. You want to maximize your profit by choosing a single day
# to buy and a single day to sell in the future.
# Return the maximum profit. If no profit is possible, return 0.
#
# Example:
#   Input:  prices = [7, 1, 5, 3, 6, 4]
#   Output: 5
#   Explanation: Buy on day 2 (price=1), sell on day 5 (price=6), profit = 6-1 = 5.
#
#   Input:  prices = [7, 6, 4, 3, 1]
#   Output: 0
#   Explanation: No profitable transaction is possible.

from typing import List


def max_profit(prices: List[int]) -> int:
    profit = 0
    buy_price = prices[0]
    for i in range(0, len(prices)):
        if prices[i] < buy_price:
            buy_price = prices[i]
        elif prices[i] > buy_price:
            profit = max(profit, prices[i] - buy_price)

    return profit

if __name__ == "__main__":
    assert max_profit([2, 4, 1]) == 2
    assert max_profit([1, 2]) == 1
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([2, 1]) == 0
    assert max_profit([3, 3, 3]) == 0
    print("All tests passed!")
