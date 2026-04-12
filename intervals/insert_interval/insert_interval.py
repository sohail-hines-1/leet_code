# LeetCode #57 — Insert Interval
#
# Given a list of non-overlapping intervals sorted by start time and a new interval,
# insert it into the list merging any overlapping intervals.
#
# Example:
#   Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
#   Output: [[1,5],[6,9]]

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert([], [5, 7]) == [[5, 7]]
    print("All tests passed!")
