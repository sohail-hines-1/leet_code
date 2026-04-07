# LeetCode #104 — Maximum Depth of Binary Tree
#
# Given the root of a binary tree, return its maximum depth.
# The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
# Example:
#   Input:  [3, 9, 20, null, null, 15, 7]
#   Output: 3
#
#   Input:  [1, null, 2]
#   Output: 2

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
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
    assert max_depth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth(build_tree([1, None, 2])) == 2
    assert max_depth(None) == 0
    assert max_depth(build_tree([1])) == 1
    print("All tests passed!")
