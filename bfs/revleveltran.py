from typing import List
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zig_zag_traversal(root: Node) -> List[List[int]]:
    res=[]
    queue=deque([root])
    # This flag is going to keep track if we reverse the order or not
    ltr=True
    while len(queue)>0:
        n = len(queue)
        new_level=[]
        for _ in range(n):
            node=queue.popleft()
            new_level.append(node.val)
            for child in [node.left,node.right]:
                    if child:
                        queue.append(child)
        # This is where reverse our level
        if not ltr:
            new_level.reverse()
        res.append(new_level)
        # We switch the flag by putting not lol
        ltr= not ltr
    return res

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = zig_zag_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))