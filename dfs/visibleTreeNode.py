class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# The top part is the logic to add counts to total variable, return value
# The bottom part is the logic to tranverse through child nodes recomputing new max_sofar, the state being passed down
def visible_tree_node(root: Node) -> int:
    def dfs(root, max_sofar):
        # If root does NOT exist, return 0 because it will not add to to total amount of visible nodes seen
        if not root:
            return 0
        #  intialize total to 0
        total = 0
        # If the current root value in the iteration is greater than the highest node value seen transversing, then add 1 to our total count
        if root.val >= max_sofar:
            total += 1
        # Recompute the max_sofar by checking if the previous parent node value is higher than current node value using max method
        total += dfs(root.left, max(max_sofar, root.val)) # max_sofar for child node is the larger of previous max and current node val
        total += dfs(root.right, max(max_sofar, root.val))

        return total

    # start max_sofar with smallest number possible so any value root has is smaller than it
    return dfs(root, -float('inf'))