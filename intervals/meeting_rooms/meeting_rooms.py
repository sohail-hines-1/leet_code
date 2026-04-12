# LeetCode #252 — Meeting Rooms
#
# Given an array of meeting time intervals [start, end], determine if a person
# could attend all meetings (no two meetings overlap).
#
# Example:
#   Input:  intervals = [[0,30],[5,10],[15,20]]
#   Output: False

from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    pass


if __name__ == "__main__":
    assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) == False
    assert can_attend_meetings([[7, 10], [2, 4]]) == True
    print("All tests passed!")
