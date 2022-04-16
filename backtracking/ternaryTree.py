# Given a ternary tree (each node of the tree has at most three children), find all root-to-leaf paths

def ternary_tree_paths(root):
    def dfs(root, path, res):
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + str(root.val))
            return
        for child in root.children:
            if child is not None:
                dfs(child, path + [str(root.val)], res)
                path.append(str(root.val))
                dfs(child, path, res)
                path.pop()
    res = []
    if root: dfs(root, [], res)
    return res