# LeetCode #297 — Serialize and Deserialize Binary Tree
#
# Design an algorithm to serialize a binary tree to a string and deserialize
# that string back to the original tree structure.
# There is no restriction on the format of the serialized string.
#
# Example:
#   Input:  tree root = [1, 2, 3, null, null, 4, 5]
#   serialize → some string
#   deserialize → reconstructed tree equal to the original

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Optional[TreeNode]) -> str:
    pass


def deserialize(data: str) -> Optional[TreeNode]:
    pass


# Helper to check if two trees are equal
def trees_equal(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and trees_equal(a.left, b.left) and trees_equal(a.right, b.right)


if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert trees_equal(deserialize(serialize(t1)), t1)

    t2 = None
    assert deserialize(serialize(t2)) is None

    t3 = TreeNode(1)
    assert trees_equal(deserialize(serialize(t3)), t3)

    t4 = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert trees_equal(deserialize(serialize(t4)), t4)

    print("All tests passed!")
