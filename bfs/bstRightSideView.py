from typing import List
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_right_side_view(root: Node) -> List[int]:
    res = []
    queue = deque([root])
    while len(queue)>0:
        n = len(queue)
        new_level=[]
        for _ in range(n):
            node=queue.popleft()
            new_level.append(node.val)
            for child in [node.left,node.right]:
                if child:
                    queue.append(child)
        # From every level, we are popping of the right most character
        r=new_level.pop()
        res.append(r)
    return res
            
def binary_tree_right_side_view_cleaner(root):
    res = []
    queue = deque([root]) # at least one element in the queue to kick start bfs
    while len(queue) > 0: # as long as there is element in the queue
        n = len(queue) # number of nodes in current level
        res.append(queue[0].val) # only append the first node we encounter since it's the rightmost
        for _ in range(n): # dequeue each node in the current level
            node = queue.popleft()
            for child in [node.right, node.left]: # we add right children first so it'll pop out of the queue first
                if child is not None:
                    queue.append(child)
    return res

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)