from data import ListNode
# fast and slow pointer closing down gap -1 at a time so it will met
def hasCycle(head: ListNode) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

list1 = ListNode(1,ListNode(2,ListNode(3)))
# 3 -> 2
list1.next.next.next = list1.next
list2 = ListNode(1,ListNode(2,ListNode(3)))
print(hasCycle(list1)) # True
print(hasCycle(list2)) # False