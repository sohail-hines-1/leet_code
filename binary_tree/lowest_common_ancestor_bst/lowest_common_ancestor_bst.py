# LeetCode #235 — Lowest Common Ancestor of a Binary Search Tree
#
# Given a BST and two nodes p and q, return their lowest common ancestor (LCA).
# The LCA is the deepest node that has both p and q as descendants
# (a node is allowed to be a descendant of itself).
# You may exploit BST ordering properties to solve this efficiently.
#
# Example:
#   Input:  BST = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#   Output: 6
#
#   Input:  BST = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#   Output: 2

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


if __name__ == "__main__":
    tree = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert lowest_common_ancestor(tree, find_node(tree, 2), find_node(tree, 8)).val == 6
    assert lowest_common_ancestor(tree, find_node(tree, 2), find_node(tree, 4)).val == 2

    tree2 = build_tree([2, 1])
    assert lowest_common_ancestor(tree2, find_node(tree2, 2), find_node(tree2, 1)).val == 2
    print("All tests passed!")
