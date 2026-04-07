# LeetCode #200 — Number of Islands
#
# Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and formed by connecting adjacent land cells
# horizontally or vertically.
#
# Example:
#   Input:  grid = [["1","1","0"],["0","1","0"],["0","0","1"]]
#   Output: 2
#
#   Input:  grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
#   Output: 1

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    pass


if __name__ == "__main__":
    assert num_islands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]) == 1

    assert num_islands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]) == 3

    assert num_islands([["1"]]) == 1
    assert num_islands([["0"]]) == 0

    assert num_islands([
        ["1","0","1"],
        ["0","1","0"],
        ["1","0","1"]
    ]) == 5
    print("All tests passed!")
