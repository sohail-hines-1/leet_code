# LeetCode #15 — Three Sum
#
# Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
# such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
#
# Example:
#   Input:  nums = [-1,0,1,2,-1,-4]
#   Output: [[-1,-1,2],[-1,0,1]]
import itertools
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    all_combinations = list(itertools.combinations(nums, 3))
    valid_combinations = []
    seen = set()
    for combo in all_combinations:
        triplet = tuple(sorted(combo))
        if sum(triplet) == 0 and triplet not in seen:
            seen.add(triplet)
            valid_combinations.append(list(triplet))

    return valid_combinations

if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
    assert three_sum([0, 1, 1]) == []
    print("All tests passed!")
