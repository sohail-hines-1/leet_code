# LeetCode #55 — Jump Game
#
# Given an array where each element is the max jump length from that position,
# return whether you can reach the last index.
#
# Example:
#   Input:  [2, 3, 1, 1, 4]
#   Output: True
#
#   Input:  [3, 2, 1, 0, 4]
#   Output: False

from typing import List


def can_jump(nums: List[int]) -> bool:
    pass


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) == True
    assert can_jump([3, 2, 1, 0, 4]) == False
    print("All tests passed!")
