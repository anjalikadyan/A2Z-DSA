class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

def findMiddle(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def sortList(head):
    if not head or not head.next:
        return head
    
    mid = findMiddle(head)
    right_head = mid.next
    mid.next = None
    
    left_sorted = sortList(head)
    right_sorted = sortList(right_head)
    
    return mergeTwoLists(left_sorted, right_sorted)

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print("Original List:")
printList(head)

sorted_head = sortList(head)
print("Sorted List:")
printList(sorted_head)
