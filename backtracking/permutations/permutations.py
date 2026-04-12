# LeetCode #46 — Permutations
#
# Given an array of distinct integers, return all possible permutations in any order.
#
# Example:
#   Input:  nums = [1,2,3]
#   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    result = permute([1, 2, 3])
    assert sorted(result) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    assert permute([1]) == [[1]]
    print("All tests passed!")
