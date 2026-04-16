# LeetCode #27 — Remove Element
#
# Given an integer array nums and an integer val, remove all occurrences of
# val in-place. Return k, the number of elements not equal to val. The first
# k elements of nums must hold those values; the rest does not matter.
#
# Example:
#   Input:  nums = [3, 2, 2, 3], val = 3
#   Output: 2, nums = [2, 2, ...]
#
#   Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
#   Output: 5, nums = [0, 1, 3, 0, 4, ...]
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    return j


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    assert remove_element(nums, 3) == 2
    assert sorted(nums[:2]) == [2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert remove_element(nums, 2) == 5
    assert sorted(nums[:5]) == [0, 0, 1, 3, 4]

    nums = [1]
    assert remove_element(nums, 1) == 0

    nums = [1]
    assert remove_element(nums, 2) == 1
    assert nums[:1] == [1]

    nums = [2, 2, 2]
    assert remove_element(nums, 2) == 0

    print("All tests passed!")
