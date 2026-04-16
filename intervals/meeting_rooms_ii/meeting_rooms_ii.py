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
    start_intervals = sorted([x[0] for x in intervals])
    end_intervals = sorted([x[1] for x in intervals])
    min_rooms = 0
    rooms = 0
    start_index = 0
    end_index = 0
    for i in range(0, len(start_intervals)):
        if start_intervals[start_index] < end_intervals[end_index]:
            rooms += 1
            start_index += 1
        else:
            rooms -= 1
            end_index += 1
        min_rooms = max(min_rooms, rooms)

    return min_rooms


if __name__ == "__main__":
    # Rolling overlaps — only ever 2 concurrent, but naive adjacent comparison overcounts
    assert min_meeting_rooms([[1, 3], [2, 4], [4, 6], [3, 5]]) == 2

    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1

    # Meetings interleave — rooms free up and get reused
    assert min_meeting_rooms([[0, 10], [1, 2], [3, 4], [5, 6]]) == 2

    # All meetings overlap — need a room per meeting
    assert min_meeting_rooms([[0, 10], [1, 9], [2, 8], [3, 7]]) == 4

    # Sequential — only one room needed
    assert min_meeting_rooms([[0, 5], [5, 10], [10, 15]]) == 1

    print("All tests passed!")
