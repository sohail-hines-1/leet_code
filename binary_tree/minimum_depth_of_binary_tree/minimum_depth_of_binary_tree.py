# LeetCode #111 — Minimum Depth of Binary Tree
#
# Given the root of a binary tree, return its minimum depth.
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
# A leaf is a node with no children.
#
# Example:
#   Input:  [3, 9, 20, null, null, 15, 7]
#   Output: 2
#
#           3
#          / \
#         9   20
#            /  \
#           15   7
#
#   The shortest root-to-leaf path is 3 -> 9 (length 2).
#
#   Input:  [2, null, 3, null, 4, null, 5, null, 6]
#   Output: 5
#
#           2
#            \
#             3
#              \
#               4
#                \
#                 5
#                  \
#                   6
#
#   Only one root-to-leaf path exists: 2 -> 3 -> 4 -> 5 -> 6 (length 5).
#   Note: 2, 3, 4, 5 each have only a right child, so they are NOT leaves.
#
# Note: BFS is the natural fit — the first leaf encountered while
# traversing level by level is guaranteed to be at the minimum depth,
# so you can return immediately.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    depth = 0
    queue = deque()
    queue.append(root)
    while queue:
        depth += 1
        for _ in range(len(queue)):
            current = queue.popleft()
            if current.left is None and current.right is None:
                return depth
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
    return depth

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
    assert min_depth(build_tree([3, 9, 20, None, None, 15, 7])) == 2
    assert min_depth(build_tree([2, None, 3, None, 4, None, 5, None, 6])) == 5
    assert min_depth(None) == 0
    assert min_depth(build_tree([1])) == 1
    assert min_depth(build_tree([1, 2])) == 2
    print("All tests passed!")
