"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
#         Hash to store all nodes and their values
#         Return that Hash with key as the original head so we have a copy

        copyHash = {None:None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            copyHash[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copyHash[cur]
            copy.next = copyHash[cur.next]
            copy.random = copyHash[cur.random]
            cur = cur.next
        
        return copyHash[head]