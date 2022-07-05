# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        sum1,sum2 = '',''
        while cur:
            sum1 += str(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            sum2 +=str(cur.val)
            cur = cur.next
        
        newSum = int(''.join(reversed(sum1))) + int(''.join(reversed(sum2)))
        newSumBackwards = ''.join(reversed(str(newSum)))
        print(newSumBackwards)
        
        dummy = ListNode()
        tail = dummy
        for c in newSumBackwards:
            tail.next = ListNode(int(c))
            tail = tail.next
        
        return dummy.next
            