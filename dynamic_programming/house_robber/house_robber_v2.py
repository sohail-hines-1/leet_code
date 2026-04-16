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

#   This version include memoization that is missing from the previous version.
#
#   In Python the simplest way is @functools.lru_cache on the helper, or a plain dict passed through as a parameter. Without it the time complexity is O(2^n) — with it, it drops
#    to O(n) since each position is computed exactly once.

from typing import List

def do_rob(nums: List[int], position, skips, includes) -> int:
    if position < 0:     # Note: position 0 is valid and permitted
        return 0

    skip_total = fetch_skip_total(nums, position, skips, includes)

    include_total = fetch_include_total(nums, position, skips, includes)

    return max(skip_total, include_total)                           # returns the max of two totals


def fetch_include_total(nums: list[int], position, skips, includes) -> int:
    if position - 2 in includes:
        rob_path_total = includes[position - 2]
        include_total = nums[position] + rob_path_total
    else:
        rob_path_total = do_rob(nums, position - 2, skips, includes)  # Important: The current home value is added here !!
        include_total = nums[position] + rob_path_total
        includes[position - 2] = rob_path_total

    return include_total


def fetch_skip_total(nums: list[int], position, skips, includes) -> int:
    if position - 1 in skips:
        skip_total = skips[position - 1]
    else:
        skip_total = do_rob(nums, position - 1, skips, includes)  # skip robs adjacent house
        skips[position - 1] = skip_total

    return skip_total


def rob(nums: List[int]) -> int:

    skips = {}
    includes = {}

    return do_rob(nums, len(nums) - 1, skips, includes)

if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    print("All tests passed!")
