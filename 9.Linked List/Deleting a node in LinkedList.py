n = int(input())
a = int(input("number: "))

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
head=Node(a)
pre=head
def insert(head,x):
    temp=Node(x)
    current=head
    while current.next:
        current=current.next
    current.next=temp
def deleteNode(head, node):
    temp = head
    prev = None

    if temp is None:
        return head
    if node == 1:
        head = temp.next
        return head
    for i in range(1, node):
        prev = temp
        temp = temp.next
        if temp is None:
            print("Data not present")
            return head
    if temp is not None:
        prev.next = temp.next
    return head
node1 = int(input("number: "))
for i in range(n-1):
    s=int(input("number: "))
    insert(head,s)
head=pre
deleteNode(head,node1)
while head:
    print(head.data,end=" ")
    head=head.next