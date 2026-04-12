# LeetCode #323 — Number of Connected Components in an Undirected Graph
#
# Given n nodes labeled 0 to n-1 and a list of undirected edges, return the
# number of connected components in the graph.
#
# Example:
#   Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
#   Output: 2

from typing import List


def count_components(n: int, edges: List[List[int]]) -> int:
    pass


if __name__ == "__main__":
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    print("All tests passed!")
