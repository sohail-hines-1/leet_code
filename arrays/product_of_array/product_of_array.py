# LeetCode #238 — Product of Array Except Self
#
# Given an integer array nums, return an array answer such that answer[i] is equal
# to the product of all elements in nums except nums[i].
# You must not use division and must run in O(n) time.
#
# Example:
#   Input:  nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
#
#   Input:  nums = [-1, 1, 0, -3, 3]
#   Output: [0, 0, 9, 0, 0]

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    sum = 1
    current_index = 0
    results = [0] * len(nums)

    while current_index < len(nums):
        for i in range(0, len(nums)):
            if i == current_index:
                continue
            sum *= nums[i]
            results [current_index] = sum
        sum = 1
        current_index += 1
    return results


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert product_except_self([0, 0]) == [0, 0]
    print("All tests passed!")
