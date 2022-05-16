class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList_iteratively( head: ListNode) -> ListNode:
    # intialize 2 pointers so we can reverse nodes
    prev, curr = None, head
    
    # while there is a node
    while curr: 
        # save next node to tmp variable
        temp = curr.next
        # save next node to previous so we can shift our pointers
        curr.next = prev
        # update prev and set it to curr node
        prev = curr
        # save curr to tmp and not curr.next because we reassigned it to prev in line 15
        curr = temp
    # return result which is stored in previous when loop stops executing
    return prev

def reverseList_recursive( head: ListNode) -> ListNode:
    # base case / simplest problem is node is null
    if not head:
        return None
    # set newHead to current head
    newHead = head
    # if there is another node next to current node
    if head.next:
        # reassign head to a recursive call on next node
        newHead = reverseList_recursive(head.next)
        # reverse the next head
        head.next.next = head
    # set head next to none
    head.next = None
    # return newHead
    return newHead
