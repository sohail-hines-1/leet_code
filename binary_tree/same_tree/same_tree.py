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
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return (is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right))


if __name__ == "__main__":
    v1 = int("300")  # forces a fresh integer object, not interned
    v2 = int("300")
    assert is_same_tree(TreeNode(v1), TreeNode(v2)) == True  # fails — line 27 uses 'is not' instead of '!='
    assert is_same_tree(None, None) == True
    print("All tests passed!")
