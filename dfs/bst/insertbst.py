# Given the root node of a valid BST and a value to insert into the tree, return a new root node representing the valid BST with the addition of the new item. If the new item already exists in the binary search tree, do not insert anything.

# You must expand on the original BST by adding a leaf node. Do not change the structure of the original BST.
# Output a valid BST with the inserted number, or the same BST if the number already exists.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(bst: Node, val: int) -> Node:
    # if no node, than create the node
    if bst is None:
        return Node(val)
    # If our node is less than the value, than recurse to the right since everything to the right of bst is larger
    if bst.val < val:
        bst.right = insert_bst(bst.right, val)
    # If our node is greater than the value, than recurse to the left since everything to the left of bst is smaller
    elif bst.val > val:
        bst.left = insert_bst(bst.left, val)
    # we return the bst
    return bst