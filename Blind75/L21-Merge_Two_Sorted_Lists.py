from data import ListNode , printList

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        # start at dummy then keep update tail
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    
    return dummy.next

link1 = ListNode(1, ListNode(2, ListNode(4)))
link2 = ListNode(1, ListNode(3, ListNode(4)))
printList(mergeTwoLists(link1, link2)) # [1,1,2,3,4,4]