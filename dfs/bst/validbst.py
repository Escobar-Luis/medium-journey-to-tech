from math import inf

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pre-order tranversal (n,l,r)
def valid_bst(root: Node) -> bool:
    def dfs(root, min_val, max_val):
        # empty nodes are always valid
        if not root:
            return True
        # At every node we ask, if our value less than the min seen
        if not (min_val <= root.val <= max_val):
            return False

        # When we recursively call DFS on the left node, since the left child's value should be less than or equal to current node's value we should pass current node's value as max value. Vice versa for right recursive call.
        return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)

    return dfs(root, -inf, inf) # root is always valid

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)