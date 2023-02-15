from data import ListNode , printList

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0:
        right = right.next
        n -= 1
    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next

list1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
printList(removeNthFromEnd(list1, 2)) # [1, 2, 3, 5]