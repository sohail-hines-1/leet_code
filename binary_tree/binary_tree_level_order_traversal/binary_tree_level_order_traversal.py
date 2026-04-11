# LeetCode #102 — Binary Tree Level Order Traversal
#
# Given the root of a binary tree, return the level-order traversal of its node values
# (i.e., from left to right, level by level) as a list of lists.
#
# Example 1:
#   Input:  [3, 9, 20, null, null, 15, 7]
#   Output: [3, 9, 20, 15, 7]
#
#       3
#      / \
#     9   20
#        /  \
#       15   7
#
# Example 2:
#   Input:  [1]
#   Output: [1]
#
#       1
#
# Example 3:
#   Input:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
#            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
#   Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
#            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
#
#                               1                          <- level 1
#               /---------------+---------------\
#              2                                 3         <- level 2
#       /------+------\                   /------+------\
#      4               5                 6               7 <- level 3
#    /---\           /---\             /---\           /---\
#   8     9        10    11          12    13         14    15 <- level 4
#  /\    /\        /\    /\          /\    /\         /\    /\
# 16 17 18 19    20 21 22 23       24 25 26 27      28 29 30 31 <- level 5
# /
# 32                                                            <- level 6
#
# Example 4:
#   Input:  [1, 2, 3, 4, None, 5, 6, 7, None, 8, None, None, 9,
#            10, None, 11, None, None, 12, 13, None, 14]
#   Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#
#       1                  <- level 1
#      / \
#     2   3                <- level 2
#    /   / \
#   4   5   6              <- level 3
#  /   /     \
# 7   8       9            <- level 4
# |   |       |
# 10  11      12           <- level 5
# |   |
# 13  14                   <- level 6
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:

    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)
    while queue:
        level = []                             # captures all nodes found at the current level
        for _ in range(0, len(queue)):         # loop through all nodes in queue
            current = queue.popleft()
            level.append(current.val)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        result.append(level)                    # append all nodes found at the current level to main results array
    return result

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
    assert level_order(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert level_order(build_tree([1])) == [[1]]
    assert level_order(None) == []

    # Example 3: near-complete tree, 6 levels deep
    assert level_order(build_tree(list(range(1, 33)))) == [
        [1],
        [2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        [32],
    ]

    # Example 4: unbalanced tree, 6 levels deep
    ex4_input = [1, 2, 3, 4, None, 5, 6, 7, None, 8, None, None, 9,
                 10, None, 11, None, None, 12, 13, None, 14]
    assert level_order(build_tree(ex4_input)) == [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14],
    ]

    print("All tests passed!")
