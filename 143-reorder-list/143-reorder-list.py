# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # cut in half
        # I tranverse backwards in 2nd half and normal in first half
        # We reassign pointers and return the list from start
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        prev = slow.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        front, back = head, prev
        while back:
            tmp1, tmp2 = front.next, back.next
            front.next = back
            back.next = tmp1
            front, back = tmp1, tmp2
        
        