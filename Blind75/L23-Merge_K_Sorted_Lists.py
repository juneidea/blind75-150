from data import ListNode, printList
# Pairing O nlogk, O n/2
def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists: return None
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        lists = mergedLists
    return lists[0]

def mergeList(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy.next

lists1 = [ListNode(2, ListNode(7)), ListNode(5), ListNode(4, ListNode(8)), ListNode(3,ListNode(6)), ListNode(1)]
printList(mergeKLists(lists1)) # [1, 2, 3, 4, 5, 6, 7, 8]