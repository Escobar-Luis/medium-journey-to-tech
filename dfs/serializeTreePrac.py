# # Given a binary tree, write a serialize function that converts the tree into a string and a deserialize function that converts a string to a binary tree. You may serialize the tree into any string representation you want as long as it can be deseralized.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# we can use a queue data structure because it is FIFO
# Think: how do I process this single node and defer all other work using recursive call
def serialize(root):
    # we are going to return a queue so we can deserialize it in our deserialize function
    result = []
    # we are going to define our dercursive function
    

def deserialize(s):
