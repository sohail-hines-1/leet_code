# LeetCode #128 — Longest Consecutive Sequence
#
# Given an unsorted array of integers, return the length of the longest
# sequence of consecutive integers. Must run in O(n) time.
#
# Example:
#   Input:  nums = [100, 4, 200, 1, 3, 2]
#   Output: 4   (1, 2, 3, 4)
#
#   Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
#   Output: 9   (0, 1, 2, 3, 4, 5, 6, 7, 8)

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
    print("All tests passed!")
