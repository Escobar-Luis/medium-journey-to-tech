# Given a binary tree, invert it and return the new value. You may invert it in-place.

# To "invert" a binary tree, switch the left subtree and the right subtree, and invert them both. Inverting an empty tree does nothing.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    # If i have no tree, then return nothing
    if tree is None:
        return None
    # otherwise make a node using the current nodes value, yet recursively call invert onto the right as the left parameter and vice versa for the right parmeter
    return Node(tree.val, invert_binary_tree(tree.right), invert_binary_tree(tree.left))

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)