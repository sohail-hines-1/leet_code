# LeetCode #101 — Symmetric Tree
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
# Example:
#   Input:  [1, 2, 2, 3, 4, 4, 3]
#   Output: True
#
#   Input:  [1, 2, 2, null, 3, null, 3]
#   Output: False

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: Optional[TreeNode]) -> bool:
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
    assert is_symmetric(build_tree([1, 2, 2, 3, 4, 4, 3])) == True
    assert is_symmetric(build_tree([1, 2, 2, None, 3, None, 3])) == False
    assert is_symmetric(build_tree([1])) == True
    assert is_symmetric(None) == True
    print("All tests passed!")
