# LeetCode #79 — Word Search
#
# Given an m x n grid of characters and a word, return True if the word exists
# in the grid. The word must be constructed from sequentially adjacent cells
# (horizontally or vertically), and each cell may only be used once.
#
# Example:
#   Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#   Output: True

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    pass


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board, "ABCCED") == True
    assert exist(board, "ABCB") == False
    print("All tests passed!")
