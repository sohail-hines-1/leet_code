# LeetCode #236 — Lowest Common Ancestor of a Binary Tree
#
# Given a binary tree (not necessarily a BST) and two nodes p and q,
# return their lowest common ancestor (LCA).
# The LCA is the deepest node that has both p and q as descendants
# (a node is allowed to be a descendant of itself).
# Unlike #235, you cannot rely on BST ordering here.
#
# Example:
#   Input:  tree = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#   Output: 3
#
#   Input:  tree = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#   Output: 5

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
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
    tree = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert lowest_common_ancestor(tree, find_node(tree, 5), find_node(tree, 1)).val == 3
    assert lowest_common_ancestor(tree, find_node(tree, 5), find_node(tree, 4)).val == 5

    tree2 = build_tree([1, 2])
    assert lowest_common_ancestor(tree2, find_node(tree2, 1), find_node(tree2, 2)).val == 1
    print("All tests passed!")
