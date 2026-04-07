# LeetCode #1 — Two Sum
#
# Given an array of integers nums and an integer target, return the indices of
# the two numbers that add up to target. Each input has exactly one solution,
# and the same element may not be used twice.
#
# Example:
#   Input:  nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]  (nums[0] + nums[1] == 9)
#
#   Input:  nums = [3, 2, 4], target = 6
#   Output: [1, 2]

#from idlelib.rpc import response_queue
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    value_indexes = {}

    for i in range(0, len(nums)):
        value_indexes[nums[i]] = i

    for i in range(0, len(nums)):
        required_value = target - nums[i]
        if required_value in value_indexes and value_indexes[required_value] != i:
            return [i, value_indexes[required_value]]
    return []

if __name__ == "__main__":
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]
    assert two_sum([-1, -2, -3, -4], -6) == [1, 3]
#    assert two_sum([3, 3, 3, 7], 6) == [0, 1]
    print("All tests passed!")
