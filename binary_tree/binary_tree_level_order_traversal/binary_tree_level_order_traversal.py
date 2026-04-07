# LeetCode #102 — Binary Tree Level Order Traversal
#
# Given the root of a binary tree, return the level-order traversal of its node values
# (i.e., from left to right, level by level) as a list of lists.
#
# Example:
#   Input:  [3, 9, 20, null, null, 15, 7]
#   Output: [[3], [9, 20], [15, 7]]
#
#   Input:  [1]
#   Output: [[1]]

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
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
    assert level_order(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert level_order(build_tree([1])) == [[1]]
    assert level_order(None) == []
    print("All tests passed!")
