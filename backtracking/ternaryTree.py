# Given a ternary tree (each node of the tree has at most three children), find all root-to-leaf paths
class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root):
    # dfs helper function
    # We use path to keep track of the nodes we have visited to reach the current node and use it to construct our solution when we reach leaf nodes.
    def dfs(root, path, res):
         # all method returns boolen depending if all iterables are valid
        # If its true that every character is null in our current nodes children meaning we reached a leaf node
        # exit condition, reached leaf node, append paths to results
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + str(root.val))
            return

        # dfs on each non-null child
        for child in root.children:
            if child is not None:
                path.append(str(root.val))
                dfs(child, path, res)
                path.pop()

    res = []
    if root: dfs(root, [], res)
    return res

def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)


