# LeetCode #56 — Merge Intervals
#
# Given an array of intervals where intervals[i] = [start, end],
# merge all overlapping intervals and return an array of the non-overlapping intervals.
#
# Example:
#   Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#
#   Input:  intervals = [[1,4],[4,5]]
#   Output: [[1,5]]  (touching intervals are merged)

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert merge([[1, 2]]) == [[1, 2]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    print("All tests passed!")
