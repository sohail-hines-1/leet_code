# LeetCode #124 — Binary Tree Maximum Path Sum
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes has an edge. Return the maximum path sum of any non-empty path.
#
# Example:
#   Input:  root = [1,2,3]
#   Output: 6

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    pass


if __name__ == "__main__":
    # assert max_path_sum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6
    assert max_path_sum(TreeNode(-3)) == -3
    print("All tests passed!")
