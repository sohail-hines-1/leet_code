# LeetCode #417 — Pacific Atlantic Water Flow
#
# Given an m x n matrix of heights, return a list of coordinates where water
# can flow to both the Pacific ocean (top/left) and Atlantic ocean (bottom/right).
#
# Example:
#   Input:  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
#   Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

from typing import List


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    # assert pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    assert pacific_atlantic([[1]]) == [[0, 0]]
    print("All tests passed!")
