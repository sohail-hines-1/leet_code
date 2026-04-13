# LeetCode #572 — Subtree of Another Tree
#
# Given the roots of two binary trees root and subRoot, return True if there is
# a subtree of root with the same structure and node values as subRoot.
#
# Example:
#   Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
#   Output: True
#
#       3
#      / \
#     4   5
#    / \
#   1   2
#
#   subRoot = [4,1,2]:
#       4
#      / \
#     1   2
#
#   Input:  root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2]
#   Output: False  (the 4-subtree has an extra child 0)
#
#       3
#      / \
#     4   5
#    / \
#   1   2
#      /
#     0
from operator import truediv
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_nodes(root: Optional[TreeNode], node: Optional[TreeNode]) -> List[TreeNode]:
    if root is None or node is None:
        return []
    matches = []
    if root.val == node.val:
        matches.append(root)
    matches += find_nodes(root.left, node)
    matches += find_nodes(root.right, node)
    return matches

def do_compare(root: Optional[TreeNode], node: Optional[TreeNode]) -> bool:
    if root is None:
        return True

    if node is None:
        return False

    if root.val != node.val:
        return False

    return do_compare(root.left, node.left) and do_compare(root.right, node.right)

def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    if sub_root is None:
        return True
    sub_nodes = find_nodes(root, sub_root)
    if len(sub_nodes) == 0:
        return False

    for i in range(0, len(sub_nodes)):
        if do_compare(sub_nodes[i], sub_root):
            return True

    return False

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

    # single-node subRoot not in tree
    root_ = build_tree([1, 2, 3])
    assert is_subtree(root_, build_tree([9])) == False

    # subtree exists at left child
    root = build_tree([3, 4, 5, 1, 2])
    sub  = build_tree([4, 1, 2])
    assert is_subtree(root, sub) == True

    # subtree does not match — extra node makes it differ
    root2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    assert is_subtree(root2, sub) == False

    # subRoot matches root itself
    root3 = build_tree([1, 2, 3])
    sub3  = build_tree([1, 2, 3])
    assert is_subtree(root3, sub3) == True

    # subRoot is a deep right subtree
    root4 = build_tree([1, 2, 3, 4, 5, 6, 7])
    sub4  = build_tree([3, 6, 7])
    assert is_subtree(root4, sub4) == True

    # single-node subRoot present in tree
    root6 = build_tree([1, 2, 3])
    assert is_subtree(root6, build_tree([2])) == True

    # empty root, non-empty subRoot
    assert is_subtree(None, build_tree([1])) == False

    # subRoot is smaller than the matching candidate — extra right child in root should cause mismatch
    # root candidate: 4 with children 1 and 2; subRoot: 4 with only left child 1
    # do_compare skips checking root.right when root.right is not None but node.right IS None
    root8 = build_tree([3, 4, 5, 1, 2])
    sub8  = build_tree([4, 1])          # only left child, no right
    assert is_subtree(root8, sub8) == False

    print("All tests passed!")
