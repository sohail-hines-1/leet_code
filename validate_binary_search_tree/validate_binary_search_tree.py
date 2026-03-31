from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    pass


# Helper to build tree from level-order list (None = missing node)
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
    assert is_valid_bst(build_tree([2, 1, 3])) == True
    assert is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])) == False
    assert is_valid_bst(build_tree([1])) == True
    assert is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])) == False
    assert is_valid_bst(None) == True
    print("All tests passed!")
