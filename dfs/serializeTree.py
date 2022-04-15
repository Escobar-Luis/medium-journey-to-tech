# Given a binary tree, write a serialize function that converts the tree into a string and a deserialize function that converts a string to a binary tree. You may serialize the tree into any string representation you want as long as it can be deseralized.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # our result is going to be an array
    res = []
    # defining recurive call
    def dfs(root):
        # base case to exit recursion, if no root found then we append x to our result and return nothing
        if not root:
            res.append('x')
            return
        # this is pre-order tranversal because we are doing work first at every visit of subtree by appending the nodes value to our result
        res.append(root.val)
        # check left and right subtree
        dfs(root.left)
        dfs(root.right)
    # calling recurive function
    dfs(root)
    # returning our response by joining the array
    return ' '.join(res)

def deserialize(s):
    # defining recurive call 
    def dfs(nodes):
        # built in next method prints the next node in our array
        val = next(nodes)
        # we appended an x into our array in our serialize function, so we return nothing if we do not find anything
        if val == 'x': return
        # converting current val into a node
        cur = Node(int(val))
        # converting the current nodes subtrees from array to tree
        cur.left = dfs(nodes)
        cur.right = dfs(nodes)
        return cur
    # create an iterator that returns a token each time we call `next`
    return dfs(iter(s.split()))

serialize([1,2,3,None,None,4,5])
