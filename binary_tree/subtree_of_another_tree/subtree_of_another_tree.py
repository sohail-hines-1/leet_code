# LeetCode #572 — Subtree of Another Tree
#
# Given the roots of two binary trees root and subRoot, return True if there is
# a subtree of root with the same structure and node values as subRoot.
#
# Example:
#   Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
#   Output: True

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    pass


if __name__ == "__main__":
    # assert is_subtree(root, subRoot) == True
    assert is_subtree(None, None) == True
    print("All tests passed!")
