# LeetCode #15 — Three Sum
#
# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
# such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
#
# Example:
#   Input:  nums = [-1,0,1,2,-1,-4]
#   Output: [[-1,-1,2],[-1,0,1]]

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    print("All tests passed!")
