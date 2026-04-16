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
    if root is None:
        return 0

    max_sum = max(0, root.val)
    max_sum += max(0, max_path_sum(root.left))
    max_sum += max(0, max_path_sum(root.right))

    return max_sum

if __name__ == "__main__":
    # Simple tree — path goes left → root → right
    #     1
    #    / \
    #   2   3        path: 2 → 1 → 3 = 6
    assert max_path_sum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6

    # Single negative node — must still return it (path must be non-empty)
    #   -3            path: -3 = -3
    assert max_path_sum(TreeNode(-3)) == -3

    # Single positive node
    #    5             path: 5 = 5
    assert max_path_sum(TreeNode(5)) == 5

    # Best path is entirely in the right subtree, not through root
    #      -10
    #      / \
    #     9   20      path: 15 → 20 → 7 = 42
    #        /  \
    #       15   7
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_path_sum(root) == 42

    # All negative — best path is the least negative single node
    #      -1
    #      / \
    #    -2  -3       path: -1 = -1
    assert max_path_sum(TreeNode(-1, TreeNode(-2), TreeNode(-3))) == -1

    # Best path goes down the left spine, ignoring negative right branches
    #       1
    #      / \
    #     4  -1       path: 4 → 1 → 5 = 10
    #    / \
    #   5  -2
    root = TreeNode(1, TreeNode(4, TreeNode(5), TreeNode(-2)), TreeNode(-1))
    assert max_path_sum(root) == 10

    # Path does not have to pass through root
    #        1
    #       /
    #      2
    #     / \
    #   10   10       path: 10 → 2 → 10 = 22
    root = TreeNode(1, TreeNode(2, TreeNode(10), TreeNode(10)))
    assert max_path_sum(root) == 22

    print("All tests passed!")
