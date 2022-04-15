# Lowest common ancestor (LCA) of two nodes v and w in a tree is the lowest (i.e. deepest) node that has both v and w as descendants. We also define each node to be a descendant of itself (so if v has a direct connection from w, w is the lowest common ancestor).
# Given two nodes of a binary tree, find their lowest common ancestor.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# done in pre-order tranversal (n,l,r)
# My current node is lca if:
# 1) one target node is on my left subtree, and the other on my right subtree
# 2) I am equal to one of the targets and the other target is in one of my subtrees

# My current node is not lca if:
# 3) Current node is neither target node and its subtrees has no target node.
# 4) Current node is in the path between LCA and target node in case 2.
# 5) LCA is in the subtree of current node



def lca(root, node1, node2):
    # case 2
    if node1 == root or node2 == root:
        return root
    # Check if the targets are either in my left or right subtrees
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)
    
    # case 1
    # If I do find a left and right node euqal to targets, then the node I am on during recursion that first satisfies that will be returned since it will be lca
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
    