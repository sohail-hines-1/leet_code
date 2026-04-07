# LeetCode #112 — Path Sum
#
# Given the root of a binary tree and an integer targetSum, return True if the tree
# has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.
#
# Example:
#   Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#   Output: True   (path: 5 → 4 → 11 → 2)
#
#   Input:  root = [1, 2, 3], targetSum = 5
#   Output: False

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
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
    assert has_path_sum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) == True
    assert has_path_sum(build_tree([1, 2, 3]), 5) == False
    assert has_path_sum(None, 0) == False
    assert has_path_sum(build_tree([1, 2]), 1) == False
    print("All tests passed!")
