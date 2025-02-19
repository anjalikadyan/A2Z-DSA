class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next

def printList(head):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2
print("Original Linked List:")
printList(head)

new_head = removeNthFromEnd(head, n)

print(f"Linked List after removing {n}th node from the end:")
printList(new_head)