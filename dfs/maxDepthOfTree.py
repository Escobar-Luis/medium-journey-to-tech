# Question: Max depth of a binary tree is the longest root-to-leaf path. Given a binary tree, find its max depth.
# We first decide on our return value, which is the depth of the current subtree after we visit each node.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    def dfs(root): # we don't actually need an inner function doing it here just keep consistent with other solutions
        # null node adds no depth
        if not root:
            return 0
        # depth of current node's subtree = max depth of the two subtrees + 1 provided by current node
        # Max function returns the largest number of the two
        return max(dfs(root.left), dfs(root.right)) + 1
    return dfs(root)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)