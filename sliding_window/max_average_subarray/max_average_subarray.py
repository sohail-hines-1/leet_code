# Maximum Average Subarray I (LeetCode 643) — Easy
#
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value.
#
# Example:
#   Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
#   Output: 12.75
#   Explanation: Maximum average is (12 + (-5) + (-6) + 50) / 4 = 12.75
#
#   Input:  nums = [5], k = 1
#   Output: 5.0

from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    pass


if __name__ == "__main__":
    assert find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert find_max_average([5], 1) == 5.0
    assert find_max_average([0, 1, 1, 3, 3], 4) == 2.0
    assert find_max_average([4, 0, 4, 3, 3], 5) == 2.8
    assert find_max_average([-1], 1) == -1.0
    print("All tests passed!")
