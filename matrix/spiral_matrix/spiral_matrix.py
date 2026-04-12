# LeetCode #54 — Spiral Matrix
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Example:
#   Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
#   Output: [1,2,3,6,9,8,7,4,5]

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    pass


if __name__ == "__main__":
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1]]) == [1]
    print("All tests passed!")
