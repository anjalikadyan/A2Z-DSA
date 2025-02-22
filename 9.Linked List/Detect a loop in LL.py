class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next        
            fast = fast.next.next     

            if slow == fast:        
                return True
        
        return False  
def createCycleList(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    temp = head
    cycle_node = None

    for i in range(1, len(values)):
        temp.next = ListNode(values[i])
        temp = temp.next
        if i == pos:
            cycle_node = temp 

    if pos != -1:
        temp.next = cycle_node 

    return head
n = int(input())
a = [0]*n

for i in range(n-1):
    a[i]=int(input("number: "))

head = createCycleList(a, 1)  

sol = Solution()
print("Cycle detected:" if sol.hasCycle(head) else "No cycle detected")
