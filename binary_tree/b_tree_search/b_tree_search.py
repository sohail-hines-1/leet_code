class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: TreeNode) -> list[int]:
    """
    Breadth-First Search — return node values level by level (left to right).

    Example:
            1
           / \\
          2   3
         / \\
        4   5
    Output: [1, 2, 3, 4, 5]
    """

    results = []
    depth = 0

    do_bfs(root, depth, results)

    return flatten_nested_list(results)

def flatten_nested_list(results: list) -> list:
    return [val for sublist in results for val in sublist]

def do_bfs(node: TreeNode, depth: int, results: list[int]) -> None:

    if node is None:
        return

    if depth >= len(results):
        results.append([])

    results[depth].append(node.val)

    do_bfs(node.left, depth + 1, results)
    do_bfs(node.right, depth + 1, results)

def dfs_inorder(root: TreeNode) -> list[int]:
    """
    Depth-First Search — Inorder traversal (left → root → right).

    Example:
            1
           / \\
          2   3
         / \\
        4   5
    Output: [4, 2, 5, 1, 3]
    """

    results = []
    dfs_recurse_inorder(root, results)

    return results

def dfs_recurse_inorder(node: TreeNode, results: list[int]) -> None:
    if node is None:
        return
    dfs_recurse_inorder(node.left, results)
    results.append(node.val)
    dfs_recurse_inorder(node.right, results)

def dfs_recurse_preorder(node: TreeNode, results: list[int]) -> None:
    if node is None:
        return

    results.append(node.val)
    dfs_recurse_preorder(node.left, results)
    dfs_recurse_preorder(node.right, results)

def dfs_recurse_postorder(node: TreeNode, results: list[int]) -> None:
    if node is None:
        return

    dfs_recurse_postorder(node.left, results)
    dfs_recurse_postorder(node.right, results)
    results.append(node.val)


def dfs_preorder(root: TreeNode) -> list[int]:
    """
    Depth-First Search — Preorder traversal (root → left → right).

    Example:
            1
           / \\
          2   3
         / \\
        4   5
    Output: [1, 2, 4, 5, 3]
    """

    results = []
    dfs_recurse_preorder(root, results)

    return results

def dfs_postorder(root: TreeNode) -> list[int]:
    """
    Depth-First Search — Postorder traversal (left → right → root).

    Example:
            1
           / \\
          2   3
         / \\
        4   5
    Output: [4, 5, 2, 3, 1]
    """
    results = []
    dfs_recurse_postorder(root, results)

    return results
