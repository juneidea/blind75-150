from data import ListNode , printList
# L206
# def reverseList(head: ListNode) -> ListNode:
#     prev, cur = None, head
#     while cur:
#         tmp = cur.next
#         cur.next = prev
#         prev = cur
#         cur = tmp
#     return prev

# Recursive O n, O n
def reverseList(head: ListNode) -> ListNode:
    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    head.next = None
    return newHead

# link1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# printList(link1)
# printList(reverseList(link1))



# L21
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l2.val < l1.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        tail = tail.next
    if l1: tail.next = l1
    if l2: tail.next = l2
    return dummy.next

# link1 = ListNode(1, ListNode(2, ListNode(4)))
# link2 = ListNode(1, ListNode(3, ListNode(4)))
# printList(mergeTwoLists(link1, link2)) # [1,1,2,3,4,4]



# L143
# order as 1, last, 2, last-1, 3
def reorderList(head: ListNode) -> None:
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
    return head

# list1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
# list2 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
# reorderList(list1)
# printList(list1) # [1, 7, 2, 6, 3, 5, 4]
# reorderList(list2)
# printList(list2) # [1, 6, 2, 5, 3, 4]



# L19
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    left, right = dummy, head
    while n > 0:
        right = right.next
        n -= 1
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next
    return head

# list1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
# printList(removeNthFromEnd(list1, 2)) # [1, 2, 3, 5]



# L141
def hasCycle(head: ListNode) -> bool:
    slow, fast = head, head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

# list1 = ListNode(1,ListNode(2,ListNode(3)))
# list1.next.next.next = list1.next # 3 -> 2
# list2 = ListNode(1,ListNode(2,ListNode(3)))
# print(hasCycle(list1)) # True
# print(hasCycle(list2)) # False



# L23
def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists: return None
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i < len(lists)-1 else None
            mergedLists.append(mergeTwoLists(l1, l2))from data import ListNode , printList
# L206
# def reverseList(head: ListNode) -> ListNode:

# Recursive O n, O n
# def reverseList(head: ListNode) -> ListNode:

# link1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# printList(link1)
# printList(reverseList(link1))



# L21
# def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

# link1 = ListNode(1, ListNode(2, ListNode(4)))
# link2 = ListNode(1, ListNode(3, ListNode(4)))
# printList(mergeTwoLists(link1, link2)) # [1,1,2,3,4,4]



# L143
# order as 1, last, 2, last-1, 3
# def reorderList(head: ListNode) -> None:

# list1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
# list2 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
# reorderList(list1)
# printList(list1) # [1, 7, 2, 6, 3, 5, 4]
# reorderList(list2)
# printList(list2) # [1, 6, 2, 5, 3, 4]



# L19
# def removeNthFromEnd(head: ListNode, n: int) -> ListNode:

# list1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
# printList(removeNthFromEnd(list1, 2)) # [1, 2, 3, 5]



# L141
# def hasCycle(head: ListNode) -> bool:

# list1 = ListNode(1,ListNode(2,ListNode(3)))
# list1.next.next.next = list1.next # 3 -> 2
# list2 = ListNode(1,ListNode(2,ListNode(3)))
# print(hasCycle(list1)) # True
# print(hasCycle(list2)) # False



# L23
# def mergeKLists(lists: list[ListNode]) -> ListNode:
        
# lists1 = [ListNode(2, ListNode(7)), ListNode(5), ListNode(4, ListNode(8)), ListNode(3,ListNode(6)), ListNode(1)]
# printList(mergeKLists(lists1)) # [1, 2, 3, 4, 5, 6, 7, 8]
        print(mergedLists)
        lists = mergedLists
    return lists[0]
        
lists1 = [ListNode(2, ListNode(7)), ListNode(5), ListNode(4, ListNode(8)), ListNode(3,ListNode(6)), ListNode(1)]
printList(mergeKLists(lists1)) # [1, 2, 3, 4, 5, 6, 7, 8]