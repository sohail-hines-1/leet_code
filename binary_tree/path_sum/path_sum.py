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


def do_has_sum(root, target_sum, total):
    if root is None:
        return False

    total += root.val
    if total == target_sum and (root.left is None and root.right is None):
        return True
    if total > target_sum:
        return False
    return do_has_sum(root.left, target_sum, total) or do_has_sum(root.right, target_sum, total)

def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    total = 0
    return do_has_sum(root, target_sum, total)

def print_tree(root: Optional[TreeNode]) -> None:
    """Print the binary tree visually to the console, level by level."""
    if not root:
        print("(empty tree)")
        return
    levels = []
    queue = [root]
    while queue:
        level_vals = []
        next_queue = []
        for node in queue:
            if node:
                level_vals.append(str(node.val))
                next_queue.append(node.left)
                next_queue.append(node.right)
            else:
                level_vals.append("null")
        if any(v != "null" for v in level_vals):
            levels.append(level_vals)
        queue = [n for n in next_queue if n is not None]
    height = len(levels)
    for i, level in enumerate(levels):
        indent = " " * (2 ** (height - i - 1) - 1)
        gap = " " * (2 ** (height - i) - 1)
        print(indent + gap.join(level))


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
    print_tree(root)
    return root

if __name__ == "__main__":
    assert has_path_sum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) == True
    assert has_path_sum(build_tree([1, 2, 3]), 5) == False
    assert has_path_sum(None, 0) == False
    assert has_path_sum(build_tree([1, 2]), 1) == False
    print("All tests passed!")
