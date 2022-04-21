# Given a binary tree, return its level order traversal. Input is the root node of the tree. The output should be a list of lists of integers, with the ith list containing the values of nodes on level i, from left to right.

from collections import deque
from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    res = []
    queue = deque([root]) # at least one element in the queue to kick start bfs
    # eventually the queue will become empty hence the while loop
    while len(queue) > 0: # as long as there is element in the queue
        n = len(queue) # number of nodes in current level, see explanation above
        new_level = []
        for _ in range(n): # dequeue each node in the current level
            # FIFO, poping first node from list (leftend)
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]: # enqueue non-null children
                if child is not None:
                    queue.append(child)
        res.append(new_level)
    return res

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)