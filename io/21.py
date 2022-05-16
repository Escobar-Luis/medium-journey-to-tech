class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # construct dummy node so we handle edge case of inserting into an empty list
    dummy = ListNode()
    
    tail = dummy
    # iterate through lists while BOTH are not empty
    while l1 and l2:
        # l2 greater than l1
        if l1.val < l2.val:
            # take l1 node and insert into tail
            tail.next = l1
            # iterate l1 to next node
            l1 = l1.next
        # l1 greater than l2
        else:
            # take l2 node and insert it into tail
            tail.next = l2
            # iterate l2 to next node
            l2 = l2.next
        # update tail pointer regardless of which node is inserted which is why it is not in conditionals
        tail = tail.next
    # if one list is empty but other isn't, find non-empty list and insert the remaining nodes to end of our tail list
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    # return the next variable after dummy.next
    return dummy.next