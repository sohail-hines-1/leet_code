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

# TODO: Since do_rob(nums, position) always returns the same value for the same position, you can cache the result the first time it's computed and return the cached value
#   on subsequent calls — avoiding redundant subtree traversals.
#
#   In Python the simplest way is @functools.lru_cache on the helper, or a plain dict passed through as a parameter. Without it the time complexity is O(2^n) — with it, it drops
#    to O(n) since each position is computed exactly once.

from typing import List

def do_rob(nums: List[int], position) -> int:

    if position < 0:     # Note: position 0 is valid and permitted
        return 0

    skip_total = do_rob(nums, position - 1)                         # skip robs adjacent house

    include_total = nums[position]  + do_rob(nums, position - 2)    # Important: The current home value is added here !!

    return max(skip_total, include_total)                           # returns the max of two totals

def rob(nums: List[int]) -> int:
    return do_rob(nums, len(nums) - 1)

if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    print("All tests passed!")
