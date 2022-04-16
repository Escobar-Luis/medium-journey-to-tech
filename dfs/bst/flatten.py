# Given a binary tree, return a linked list that is a "flattened" version of the tree.

# The linked list still uses the same nodes as a normal binary tree, only the left subtree is always empty, and the right subtree always points to the next element in the linked list (or the empty tree).

# The flattened tree represents the pre-order traversal of the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Since we are building the list backwards to form a pre-order traversal, the return value is the linked list representing the pre-order traversal of the current subtree, followed by the existing linked list.

# To build up the linked list backwards, we add the flattened right subtree before the existing linked linked list, then the flattened left tree, and finally the current node.

def flatten_tree_to_stub(tree: Node, existing_list: Node=None) -> Node:
    if tree is None:
        return existing_list
    # Since we are building list backward, we start from right to left to get existing list and then add the node
    existing_list = flatten_tree_to_stub(tree.right, existing_list)
    existing_list = flatten_tree_to_stub(tree.left, existing_list)
    # A linked list had no left subtree which is why we pass none and our existing list as the right subtree
    return Node(tree.val, None, existing_list)

def flatten_tree(tree: Node) -> Node:
    return flatten_tree_to_stub(tree)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)
