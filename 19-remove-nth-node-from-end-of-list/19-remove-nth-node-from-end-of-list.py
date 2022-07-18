# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prev, cur = dummy, dummy
        
        while n>0:
            cur = cur.next
            n-=1
        while cur and cur.next:
            cur = cur.next
            prev = prev.next
        
        prev.next = prev.next.next
        
        return dummy.next
        