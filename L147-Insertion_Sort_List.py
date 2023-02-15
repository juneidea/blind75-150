from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    # need a pointer before head
    dummy = ListNode(0, head)
    pre, cur = head, head.next

    while cur:
        if cur.val >= pre.val:
            pre, cur = cur, cur.next
            continue
        # start temp a the top
        temp = dummy
        while cur.val > temp.next.val:
            temp = temp.next
        # now temp is a node before cur wanna move to
        pre.next = cur.next
        cur.next = temp.next
        temp.next = cur
        # arrange pointer above then move to new cur for while loop
        cur = pre.next
    # if head start at (2) but dummy.next can be (1) before
    return dummy.next

def printList(head: Optional[ListNode]) -> list[int]:
    res = []
    res.append(head.val)
    cur = head.next
    while cur:
        res.append(cur.val)
        cur = cur.next
    return print(res)

head1 = ListNode(2, ListNode(1, ListNode(4, ListNode(5, ListNode(3)))))
printList(head1)
sort1 = insertionSortList(head1)
printList(sort1)
