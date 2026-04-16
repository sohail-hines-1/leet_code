# LeetCode #253 — Meeting Rooms II
#
# Given an array of meeting time intervals [start, end], return the minimum
# number of conference rooms required to hold all meetings.
#
# Example:
#   Input:  intervals = [[0,30],[5,10],[15,20]]
#   Output: 2

from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    start_intervals = sorted([x[0] for x in intervals])
    end_intervals = sorted([x[1] for x in intervals])
    min_rooms = 0
    rooms = 0
    start_index = 0
    end_index = 0
    for _ in range(0, len(start_intervals)):
        if start_intervals[start_index] < end_intervals[end_index]:     # start less than end indicates an overlap (new room is needed)
            rooms += 1
            start_index += 1
        else:                                                           # start time is >= end indicates a gap (room has been released)
            rooms -= 1
            end_index += 1
        min_rooms = max(min_rooms, rooms)

    return min_rooms


if __name__ == "__main__":
    # Two meetings overlap with the long one, but not with each other — 2 rooms
    # 0    5    10   15   20   25   30
    # |----------------------------|   [0,30]
    #      |----|                      [5,10]
    #                |---|             [15,20]
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2

    # No overlap — meetings are back to back, 1 room sufficient
    # 0    2    4    7    10
    #           |---------|            [7,10]
    # |---------|                      [2,4]
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1

    # Rolling overlaps — only ever 2 concurrent, but naive adjacent comparison overcounts
    # 0  1  2  3  4  5  6
    #    |--|                          [1,3]
    #       |--|                       [2,4]
    #          |--|                    [3,5]
    #             |--|                 [4,6]
    assert min_meeting_rooms([[1, 3], [2, 4], [4, 6], [3, 5]]) == 2

    # Short meetings interleave under a long one — rooms free up and get reused
    # 0  1  2  3  4  5  6  7  8  9  10
    # |--------------------------------|  [0,10]
    #    |--|                              [1,2]
    #          |--|                        [3,4]
    #                |--|                  [5,6]
    assert min_meeting_rooms([[0, 10], [1, 2], [3, 4], [5, 6]]) == 2

    # All meetings overlap — need a room per meeting, peak is 4
    # 0  1  2  3  4  5  6  7  8  9  10
    # |--------------------------------|  [0,10]
    #    |--------------------------|      [1,9]
    #       |----------------------|       [2,8]
    #          |------------------|        [3,7]
    assert min_meeting_rooms([[0, 10], [1, 9], [2, 8], [3, 7]]) == 4

    # Sequential — each meeting ends before the next starts, 1 room sufficient
    # 0    5    10   15
    # |----|                   [0,5]
    #      |----|              [5,10]
    #           |----|         [10,15]
    assert min_meeting_rooms([[0, 5], [5, 10], [10, 15]]) == 1

    # Peak of 3 rooms, then drops back down
    # 0  1  2  3  4  5  6  7  8
    # |------------------------|   [0,8]
    #    |---------|               [1,5]
    #       |---------|            [2,6]
    #                   |--|       [6,7]
    assert min_meeting_rooms([[0, 8], [1, 5], [2, 6], [6, 7]]) == 3

    # Single meeting — always 1 room
    assert min_meeting_rooms([[3, 7]]) == 1

    print("All tests passed!")
