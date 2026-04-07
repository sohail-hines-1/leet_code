# LeetCode #53 — Maximum Subarray
#
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum, and return that sum.
#
# Example:
#   Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   Output: 6   (subarray [4, -1, 2, 1])
#
#   Input:  nums = [5, 4, -1, 7, 8]
#   Output: 23  (entire array)

from typing import List


def max_subarray(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1]) == -1
    assert max_subarray([-2, -1]) == -1
    print("All tests passed!")
