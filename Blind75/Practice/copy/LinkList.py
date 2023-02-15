from data import ListNode , printList
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