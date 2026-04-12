# LeetCode #11 — Container With Most Water
#
# Given an integer array height of n elements representing vertical lines, find
# two lines that together with the x-axis form a container holding the most water.
#
# Example:
#   Input:  height = [1,8,6,2,5,4,8,3,7]
#   Output: 49

from typing import List


def max_area(height: List[int]) -> int:
    pass


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    print("All tests passed!")
