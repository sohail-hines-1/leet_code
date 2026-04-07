# LeetCode #199 — Binary Tree Right Side View
#
# Given the root of a binary tree, imagine yourself standing on the right side of it.
# Return the values of the nodes you can see, ordered from top to bottom.
# (i.e., the rightmost node at each level)
#
# Example:
#   Input:  [1, 2, 3, null, 5, null, 4]
#   Output: [1, 3, 4]
#
#   Input:  [1, null, 3]
#   Output: [1, 3]

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
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
    assert right_side_view(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert right_side_view(build_tree([1, None, 3])) == [1, 3]
    assert right_side_view(None) == []
    assert right_side_view(build_tree([1])) == [1]
    print("All tests passed!")
