# LeetCode #435 — Non-overlapping Intervals
#
# Given an array of intervals, return the minimum number of intervals you need
# to remove to make the rest of the intervals non-overlapping.
#
# Example:
#   Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]
#   Output: 1

from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    pass


if __name__ == "__main__":
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
    print("All tests passed!")
