# LeetCode #212 — Word Search II
#
# Given an m x n board of characters and a list of words, return all words that
# can be found in the board. Each word must be constructed from sequentially
# adjacent cells, using each cell at most once per word.
#
# Example:
#   Input:  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
#           words = ["oath","pea","eat","rain"]
#   Output: ["eat","oath"]

from typing import List


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    pass


if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    result = find_words(board, ["oath", "pea", "eat", "rain"])
    assert sorted(result) == sorted(["eat", "oath"])
    print("All tests passed!")
