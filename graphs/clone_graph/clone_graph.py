# LeetCode #133 — Clone Graph
#
# Given a reference of a node in a connected undirected graph, return a deep copy
# (clone) of the graph. Each node contains a val and a list of its neighbors.
#
# Example:
#   Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
#   Output: [[2,4],[1,3],[2,4],[1,3]]

from typing import Optional, List


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    pass


if __name__ == "__main__":
    # n1 = Node(1); n2 = Node(2); n1.neighbors = [n2]; n2.neighbors = [n1]
    # cloned = clone_graph(n1)
    # assert cloned is not n1 and cloned.val == 1
    assert clone_graph(None) is None
    print("All tests passed!")
