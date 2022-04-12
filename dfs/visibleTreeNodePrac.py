from cmath import inf
from numpy import Inf


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# The top part is the logic to add counts to total variable, return value
# The bottom part is the logic to tranverse through child nodes recomputing new max_sofar, the state being passed down
def visible_tree_node(root: Node) -> int:
    def dfs(node, m):
        # Exit case when there is no root, return 0 so we add nothing to our return value
        
        if not root:
            return 0
        # At every node we have to ask weather our value is larger than our parents so it can be visible
        # track its visibility with a variable named total 
        total=0
        if root.val >= m:
            total +=1
        # at every node, recursivley call dfs on left and right side using the max btwn current node and max value seen as state being passed down to children and add total return value (which will never be greater than 1 to it)
        total =+ dfs(node.left, max(node.val, m))
        total =+ dfs(node.right, max(node.val, m))
        # At the end of the entire function return its total
        return total
    return dfs(root,-float('inf'))
        
            