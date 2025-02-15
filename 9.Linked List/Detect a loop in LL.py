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

head = createCycleList([1, 2, 3, 4, 5], 1)  

sol = Solution()
print("Cycle detected:" if sol.hasCycle(head) else "No cycle detected")
