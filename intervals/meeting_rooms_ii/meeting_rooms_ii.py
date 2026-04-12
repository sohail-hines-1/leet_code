# LeetCode #253 — Meeting Rooms II
#
# Given an array of meeting time intervals [start, end], return the minimum
# number of conference rooms required to hold all meetings.
#
# Example:
#   Input:  intervals = [[0,30],[5,10],[15,20]]
#   Output: 2

from typing import List
import heapq


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    pass


if __name__ == "__main__":
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    print("All tests passed!")
