from data import ListNode, printList

def reorderList(head: ListNode) -> None:
    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse second half
    second = slow.next
    # slow.next to None cut the split
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merge two halfs
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

list1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
list2 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
reorderList(list1)
printList(list1) # [1, 7, 2, 6, 3, 5, 4]
reorderList(list2)
printList(list2) # [1, 6, 2, 5, 3, 4]