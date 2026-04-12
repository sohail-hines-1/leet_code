# LeetCode #153 — Find Minimum in Rotated Sorted Array
#
# Given a sorted and rotated array of unique elements, find the minimum element.
# The array was originally sorted in ascending order before rotation.
#
# Example:
#   Input:  nums = [3,4,5,1,2]
#   Output: 1

from typing import List


def find_min(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    print("All tests passed!")
