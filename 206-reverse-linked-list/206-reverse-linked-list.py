# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # tmp variable to save next node
#         we set current next pointer to prev
#         reassign prev to current
#       reassign current to tmp variable
#       continue this while we have a head

        prev, curr = None, head
    
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
