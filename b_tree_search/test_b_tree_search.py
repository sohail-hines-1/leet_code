import pytest
from b_tree_search import TreeNode, bfs, dfs_inorder, dfs_preorder, dfs_postorder


def build_tree(values: list) -> TreeNode:
    """Build a binary tree from a level-order list. None = missing node."""
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


# ── BFS ───────────────────────────────────────────────────────────────────────

class TestBFS:
    def test_general_tree(self):
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        root = build_tree([1, 2, 3, 4, 5])
        assert bfs(root) == [1, 2, 3, 4, 5]

    def test_single_node(self):
        root = TreeNode(1)
        assert bfs(root) == [1]

    def test_empty_tree(self):
        assert bfs(None) == []

    def test_left_skewed(self):
        #   1
        #  /
        # 2
        #  \
        #   3  (not a full left-skew but tests mixed path)
        root = build_tree([1, 2, None, None, 3])
        assert bfs(root) == [1, 2, 3]

    def test_right_skewed(self):
        # 1 → 2 → 3 (all right children)
        root = build_tree([1, None, 2, None, 3])
        assert bfs(root) == [1, 2, 3]

    def test_complete_tree(self):
        #         1
        #       /   \
        #      2     3
        #     / \   / \
        #    4   5 6   7
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        assert bfs(root) == [1, 2, 3, 4, 5, 6, 7]

    def test_negative_values(self):
        root = build_tree([-1, -2, -3])
        assert bfs(root) == [-1, -2, -3]


# ── DFS Inorder ───────────────────────────────────────────────────────────────

class TestDFSInorder:
    def test_general_tree(self):
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        # Inorder: 4 2 5 1 3
        root = build_tree([1, 2, 3, 4, 5])
        assert dfs_inorder(root) == [4, 2, 5, 1, 3]

    def test_single_node(self):
        root = TreeNode(7)
        assert dfs_inorder(root) == [7]

    def test_empty_tree(self):
        assert dfs_inorder(None) == []

    def test_bst_sorted_output(self):
        # BST inorder should return sorted values
        #       4
        #      / \
        #     2   6
        #    / \ / \
        #   1  3 5  7
        root = build_tree([4, 2, 6, 1, 3, 5, 7])
        assert dfs_inorder(root) == [1, 2, 3, 4, 5, 6, 7]

    def test_right_skewed(self):
        root = build_tree([1, None, 2, None, 3])
        assert dfs_inorder(root) == [1, 2, 3]

    def test_left_skewed(self):
        root = build_tree([3, 2, None, 1, None])
        assert dfs_inorder(root) == [1, 2, 3]


# ── DFS Preorder ──────────────────────────────────────────────────────────────

class TestDFSPreorder:
    def test_general_tree(self):
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        # Preorder: 1 2 4 5 3
        root = build_tree([1, 2, 3, 4, 5])
        assert dfs_preorder(root) == [1, 2, 4, 5, 3]

    def test_single_node(self):
        root = TreeNode(7)
        assert dfs_preorder(root) == [7]
    
    def test_empty_tree(self):
        assert dfs_preorder(None) == []
    
    def test_complete_tree(self):
        #         1
        #       /   \
        #      2     3
        #     / \   / \
        #    4   5 6   7
        # Preorder: 1 2 4 5 3 6 7
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        assert dfs_preorder(root) == [1, 2, 4, 5, 3, 6, 7]
    
    def test_right_skewed(self):
        root = build_tree([1, None, 2, None, 3])
        assert dfs_preorder(root) == [1, 2, 3]
    
    def test_left_skewed(self):
        root = build_tree([3, 2, None, 1, None])
        assert dfs_preorder(root) == [3, 2, 1]


# ── DFS Postorder ─────────────────────────────────────────────────────────────

class TestDFSPostorder:
    def test_general_tree(self):
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        # Postorder: 4 5 2 3 1
        root = build_tree([1, 2, 3, 4, 5])
        assert dfs_postorder(root) == [4, 5, 2, 3, 1]

    def test_single_node(self):
        root = TreeNode(7)
        assert dfs_postorder(root) == [7]

    def test_empty_tree(self):
        assert dfs_postorder(None) == []

    def test_complete_tree(self):
        #         1
        #       /   \
        #      2     3
        #     / \   / \
        #    4   5 6   7
        # Postorder: 4 5 2 6 7 3 1
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        assert dfs_postorder(root) == [4, 5, 2, 6, 7, 3, 1]

    def test_right_skewed(self):
        root = build_tree([1, None, 2, None, 3])
        assert dfs_postorder(root) == [3, 2, 1]

    def test_left_skewed(self):
        root = build_tree([3, 2, None, 1, None])
        assert dfs_postorder(root) == [1, 2, 3]
