# LeetCode #261 — Graph Valid Tree
#
# Given n nodes labeled 0 to n-1 and a list of undirected edges, determine if
# the edges form a valid tree (connected with no cycles).
#
# Example:
#   Input:  n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
#   Output: True

from typing import List


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    pass


if __name__ == "__main__":
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
    assert valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
    print("All tests passed!")
