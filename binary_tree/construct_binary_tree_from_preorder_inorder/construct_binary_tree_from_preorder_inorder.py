# LeetCode #105 — Construct Binary Tree from Preorder and Inorder Traversal
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal and inorder is the inorder traversal of the same binary tree,
# construct and return the binary tree.
#
# Example:
#   Input:  preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
#   Output: [3, 9, 20, null, null, 15, 7]
#
#   Input:  preorder = [-1], inorder = [-1]
#   Output: [-1]

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    pass


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
    assert to_list(build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])) == [3, 9, 20, None, None, 15, 7]
    assert to_list(build_tree([-1], [-1])) == [-1]
    print("All tests passed!")
