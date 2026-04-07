# LeetCode #1448 — Count Good Nodes in Binary Tree
#
# Given a binary tree root, a node X in the tree is "good" if there are no nodes
# with a value greater than X along the path from root to X.
# Return the number of good nodes in the tree.
#
# Example:
#   Input:  [3, 1, 4, 3, null, 1, 5]
#   Output: 4  (nodes with values 3 (root), 3, 4, 5 are good)
#
#   Input:  [3, 3, null, 4, 2]
#   Output: 3  (nodes 3 (root), 3, 4 are good; 2 is not because 3 > 2 on the path)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root: Optional[TreeNode]) -> int:
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
    # [3,1,4,3,null,1,5] -> good nodes: 3 (root), 3 (left->left), 4, 5 = 4
    assert good_nodes(build_tree([3, 1, 4, 3, None, 1, 5])) == 4
    # [3,3,null,4,2] -> good nodes: 3 (root), 3, 4 = 3
    assert good_nodes(build_tree([3, 3, None, 4, 2])) == 3
    assert good_nodes(build_tree([1])) == 1
    print("All tests passed!")
