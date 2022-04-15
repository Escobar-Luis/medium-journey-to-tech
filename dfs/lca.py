# Lowest common ancestor (LCA) of two nodes v and w in a tree is the lowest (i.e. deepest) node that has both v and w as descendants. We also define each node to be a descendant of itself (so if v has a direct connection from w, w is the lowest common ancestor).
# Given two nodes of a binary tree, find their lowest common ancestor.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# done in pre-order tranversal (n,l,r)
def lca(root, node1, node2):
    # base case to end recursion
    if not root:
        return

    # case 2 in above figure
    # if Current node is one of the target or the other node is in a subtree
    if root == node1 or root == node2:
        return root
    # recursive call to left and right subtrees 
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # case 1
    # One target node is on the left subtree, the other target node on the right subtree, so the current node itself is the LCA
    if left and right:
        return root

    # at this point, left and right can't be both non-null since we checked above
    # case 4 and 5, report target node or LCA back to parent
    if left:
        return left
    if right:
        return right

    # case 4, not found return null
    return None
