class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None
    
    slow, fast = head, head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    if prev:
        prev.next = slow.next
    
    return head

def printList(head: ListNode):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original list:")
printList(head)
head = deleteMiddle(head)
print("After deleting middle node:")
printList(head)
