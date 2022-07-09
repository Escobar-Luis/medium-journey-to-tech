"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h = {None : None}
        cur = head
        while cur:
            copy = Node(cur.val)
            h[cur] = copy
            cur = cur.next
        print(h.values())
        cur = head
        while cur:
            copy = h[cur]
            copy.next = h[cur.next]
            copy.random = h[cur.random]
            cur = cur.next
        return h[head]