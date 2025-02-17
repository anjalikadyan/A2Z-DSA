class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return self.getLoopLength(slow)
        
        return 0

    def getLoopLength(self, loop_node):
        count = 1
        temp = loop_node.next
        while temp != loop_node:
            count += 1
            temp = temp.next
        return count
def createLoop(head, pos):
    if pos == -1:
        return head
    
    loop_start = head
    last = head
    index = 0
    
    while last.next:
        if index == pos:
            loop_start = last
        last = last.next
        index += 1
    
    last.next = loop_start
    return head

if __name__ == "__main__":
    nodes = [Node(i) for i in range(1, 6)]
    for i in range(4):
        nodes[i].next = nodes[i + 1]
    
    head = createLoop(nodes[0], 1)  
    solution = Solution()
    print(solution.countNodesInLoop(head))
