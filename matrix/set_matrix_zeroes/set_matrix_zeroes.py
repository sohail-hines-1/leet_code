# LeetCode #73 — Set Matrix Zeroes
#
# Given an m x n integer matrix, if an element is 0, set its entire row and
# column to 0. Do this in-place.
#
# Example:
#   Input:  matrix = [[1,1,1],[1,0,1],[1,1,1]]
#   Output: [[1,0,1],[0,0,0],[1,0,1]]

from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    pass


if __name__ == "__main__":
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(m)
    # assert m == [[1,0,1],[0,0,0],[1,0,1]]
    pass
