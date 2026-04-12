# LeetCode #33 — Search in Rotated Sorted Array
#
# Given a sorted rotated integer array and a target, return the index of the target
# or -1 if it is not present. Must run in O(log n) time.
#
# Example:
#   Input:  nums = [4,5,6,7,0,1,2], target = 0
#   Output: 4

from typing import List


def search(nums: List[int], target: int) -> int:
    pass


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    print("All tests passed!")
