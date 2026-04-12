# LeetCode #100 — Same Tree
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same tree (structurally identical with same node values).
#
# Example:
#   Input:  p = [1,2,3], q = [1,2,3]
#   Output: True

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    pass


if __name__ == "__main__":
    # assert is_same_tree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))) == True
    assert is_same_tree(None, None) == True
    print("All tests passed!")
