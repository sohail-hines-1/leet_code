# LeetCode #300 — Longest Increasing Subsequence
#
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is derived from the array by deleting some elements without changing the order.
#
# Example:
#   Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
#   Output: 4   ([2, 3, 7, 101])
#
#   Input:  nums = [7, 7, 7, 7]
#   Output: 1   (strictly increasing, so repeated values don't count)

from typing import List

def do_longest_subsequence(nums: List[int], position: int, last: int) -> int:
    if position >= len(nums):
        return 0

    current = nums[position]
    skip    = do_longest_subsequence(nums, position + 1, last)
    include = 1 + do_longest_subsequence(nums, position + 1, current) if current > last else 0

    return max(skip, include)

def length_of_lis(nums: List[int]) -> int:
    return do_longest_subsequence(nums, 0, float('-inf'))

if __name__ == "__main__":
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4             # [0, 1, 2, 3]
    assert length_of_lis([1, 2, 3, 4, 5]) == 5
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4  # [2, 3, 7, 101]
    assert length_of_lis([7, 7, 7, 7, 7]) == 1
    assert length_of_lis([1]) == 1

    print("All tests passed!")
