class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth (root: Node) -> int:
    def dfs(root):
        # If this node is null and we are finding the max depth, then we return 0 because it is adding no depth to us.
        if not root:
            return 0
        # If a node is found, then we find the depth of the current node's subtree which is equal to max depth of the two subtrees + 1 provided by current node.
        return max(dfs(root.left),)
    return dfs(root)

def tree_max_depth(root:Node) -> int:
    def dfs(root):
        if not root:
            return 0
        return max(dfs(root.left),dfs(root.right)) + 1
    return dfs(root)


def tree_max_depth(root:Node) -> int:
    def dfs(root):
        if not root:
            return 0
        return max(dfs(root.left),dfs(root.right)) + 1
    return dfs(root)

