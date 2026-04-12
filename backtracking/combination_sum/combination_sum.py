# LeetCode #39 — Combination Sum
#
# Given an array of distinct integers candidates and a target integer, return all
# unique combinations that sum to target. Candidates may be reused unlimited times.
#
# Example:
#   Input:  candidates = [2,3,6,7], target = 7
#   Output: [[2,2,3],[7]]

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    pass


if __name__ == "__main__":
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print("All tests passed!")
