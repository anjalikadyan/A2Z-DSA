class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, x):
        temp = Node(x)
        if self.head is None:
            self.head = temp
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = temp
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Create LinkedList object
n = int(input())
llist = LinkedList()

# Insert first node
a = int(input("number: "))
llist.insert(a)

# Insert remaining nodes
for i in range(n-1):
    s = int(input("number: "))
    llist.insert(s)

# Display the list
llist.display()

