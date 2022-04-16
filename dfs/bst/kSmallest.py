# Given the root node of a valid BST and a number k, return the kth smallest number in this BST (1-indexed).
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# To find the kth smallest element in a BST is simple. Consider the root node of a BST: because everything in the left subtree is smaller and everything in the right tree is larger, the root node is the m + 1th largest value in the BST, where m is the size of the left subtree.

# In that case, we can compare this number to k. If they are equal, then the root is the value we want. If it is smaller, we look in the right subtree and find the k - m - 1th smallest value there (as everything there is larger than the root and the left subtree). If it's larger, we look in the left subtree and find the kth smallest value there.

# Below is an implementation. Note that because the implementation of binary trees does not include the size, the calculation of the size is linked to each recursion cycle. The time complexity of calculating size of a tree without prior knowledge about the tree size is O(n), where n is the size of the tree. In addition, the code terminates when it finds the kth largest element, so the overall time complexity is O(k).

def kth_smallest(bst: Node, k: int) -> int:
    val = None
    def tree_size(tree: Node, existing_k: int):
        nonlocal val
        if val is not None:
            return None
        if tree is None:
            return 0
        left_size = tree_size(tree.left, existing_k)
        if val is not None:
            return None
        if left_size + existing_k == k - 1:
            val = tree.val
            return None
        # existing k is added to left size +1 
        right_size = tree_size(tree.right, existing_k + left_size + 1)
        if val is not None:
            return None
        return left_size + right_size + 1
    tree_size(bst, 0)
    return val
