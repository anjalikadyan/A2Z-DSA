class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev      
            prev = curr            
            curr = next_node       
        
        return prev  

def printList(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")

head = ListNode(1)
head.next = ListNode(6)
head.next.next = ListNode(7)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original List:")
printList(head)

sol = Solution()
reversed_head = sol.reverseList(head)

print("Reversed List:")
printList(reversed_head)
