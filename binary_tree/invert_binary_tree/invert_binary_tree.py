# LeetCode #226 — Invert Binary Tree
#
# Given the root of a binary tree, invert the tree (mirror it) and return its root.
# Swapping left and right children at every node.
#
# Example:
#   Input:  [4, 2, 7, 1, 3, 6, 9]
#   Output: [4, 7, 2, 9, 6, 3, 1]
#
#   Input:  [2, 1, 3]
#   Output: [2, 3, 1]

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    temp = root.left
    root.left = root.right
    root.right = temp
    invert_tree(root.left)
    invert_tree(root.right)

    return root

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


def to_list(root: Optional[TreeNode]) -> list:
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    assert to_list(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert to_list(invert_tree(build_tree([2, 1, 3]))) == [2, 3, 1]
    assert invert_tree(None) is None
    print("All tests passed!")
