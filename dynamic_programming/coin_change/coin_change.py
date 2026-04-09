# LeetCode #322 — Coin Change
#
# Given an array of coin denominations and a total amount, return the fewest number
# of coins needed to make up that amount. If it cannot be made up by any combination
# of the coins, return -1. You may use each coin denomination an unlimited number of times.
#
# Example:
#   Input:  coins = [1, 5, 10, 25], amount = 36
#   Output: 3   (25 + 10 + 1)
#
#   Input:  coins = [2], amount = 3
#   Output: -1  (impossible)

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    pass


if __name__ == "__main__":
    assert coin_change([4, 3, 1], 6) == 2   # 25 + 10 + 1
    assert coin_change([1, 5, 10, 25], 36) == 3   # 25 + 10 + 1
    assert coin_change([1, 5, 10, 25], 30) == 2   # 25 + 5
    assert coin_change([2], 3) == -1               # impossible
    assert coin_change([1], 0) == 0                # no coins needed
    assert coin_change([1], 1) == 1
    print("All tests passed!")
