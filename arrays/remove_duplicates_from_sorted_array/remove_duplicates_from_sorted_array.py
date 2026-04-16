# LeetCode #26 — Remove Duplicates from Sorted Array
#
# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once.
# Return k, the number of unique elements. The first k elements of nums
# must hold the unique values in order; the rest does not matter.
#
# Example:
#   Input:  nums = [1, 1, 2]
#   Output: 2, nums = [1, 2, ...]
#
#   Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#   Output: 5, nums = [0, 1, 2, 3, 4, ...]
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)

    i = 1               # Note: both indexes start at 1
    k = 1
    while i < len(nums):
        if nums[i] != nums[i - 1]:      # Important: compare with previous position
            nums[k] = nums[i]           # but copy to position k
            k += 1
        i += 1

    return k

if __name__ == "__main__":
    nums = [1, 2, 3]
    assert remove_duplicates(nums) == 3
    assert nums[:3] == [1, 2, 3]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(nums) == 5
    assert nums[:5] == [0, 1, 2, 3, 4]

    nums = [1, 1, 1, 1, 2]
    assert remove_duplicates(nums) == 2
    assert nums[:2] == [1, 2]

    nums = [1]
    assert remove_duplicates(nums) == 1
    assert nums[:1] == [1]

    print("All tests passed!")
