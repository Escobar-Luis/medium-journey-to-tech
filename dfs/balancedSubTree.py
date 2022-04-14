class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# I use post-order tranversal (l,r,n) to tranverse to the last node to reach a base case to have enough information to figure out if my subtrees are actually balanced from bottom-up
def tree_height(tree):  
    # Base case to get out of recursion at bottom if if we have no subtree 
    if tree is None:
        return 0
    # report base case to its parent node and use the 0 as the first noted height, then we ask if our last nodes right subtree is balanced.
    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    # In case if one side has no subtree but it's other side does not
    if left_height is -1 or right_height is -1:
        return -1
    # if the absolute difference between them is larger than 1
    if abs(left_height - right_height) > 1:
        return -1
    # This is the state that is being passed up
    return max(left_height, right_height) + 1

# This is the recursive call on itself
def is_balanced(tree: Node) -> bool:
    return tree_height(tree) != -1


        
    