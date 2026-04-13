# LeetCode #198 — House Robber
#
# Given an array of non-negative integers representing house values,
# return the max amount you can rob without robbing two adjacent houses.
#
# Example:
#   Input:  [1, 2, 3, 1]
#   Output: 4
#
#   Input:  [2, 7, 9, 3, 1]
#   Output: 12

from typing import List

def do_rob(nums: List[int], position, total) -> int:
    if position >= len(nums):
        return total
    else:
        total += nums[position]
        position += 1
        do_rob(nums, position, total)

    return total

def rob(nums: List[int]) -> int:
    return max(do_rob(nums, 0, 0), do_rob(nums, 1, 0))


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    print("All tests passed!")
