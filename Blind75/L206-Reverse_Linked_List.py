from data import ListNode , printList
# O n, O 1
def reverseList1(head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return  prev
# Recursive O n, O n
def reverseList2(head: ListNode) -> ListNode:
    if not head: return None

    newHead = head # for the last head
    if head.next:
        # otherwise newHead is the next head
        newHead = reverseList2(head.next)
        # like going to the end and do these 3 line backward
        head.next.next = head
    head.next = None
    return newHead
# prev4 curNone  recursive
# prev3 cur4     head.next.next  head.next
# 4                              4 -> None
# 3 <- 4         4 -> 3          3 -> None
# 2 <- 3 ->      3 -> 2          2 -> None
# 1 <- 2 ->      2 -> 1          1 -> None

link1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
printList(link1)
printList(reverseList2(link1))