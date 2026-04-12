# LeetCode #78 — Subsets
#
# Given an integer array of unique elements, return all possible subsets
# (the power set). The solution set must not contain duplicate subsets.
#
# Example:
#   Input:  nums = [1,2,3]
#   Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    result = subsets([1, 2, 3])
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]])
    assert subsets([0]) == [[], [0]]
    print("All tests passed!")
