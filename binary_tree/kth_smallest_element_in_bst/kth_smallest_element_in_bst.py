# LeetCode #230 — Kth Smallest Element in a BST
#
# Given the root of a BST and an integer k, return the kth smallest value
# (1-indexed) among all node values in the tree.
#
# Example:
#   Input:  root = [3, 1, 4, null, 2], k = 1
#   Output: 1
#
#   Input:  root = [5, 3, 6, 2, 4, null, null, 1], k = 3
#   Output: 3

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    pass


def build_tree(values: list) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    assert kth_smallest(build_tree([3, 1, 4, None, 2]), 1) == 1
    assert kth_smallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    assert kth_smallest(build_tree([1]), 1) == 1
    print("All tests passed!")
