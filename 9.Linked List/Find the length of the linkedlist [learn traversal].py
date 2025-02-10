n = int(input())
a = int(input("number: "))
def getCount(head):
        count=0
        while (head):
            head=head.next
            count+=1
        return count
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

for i in range(n-1):
    s=int(input("number: "))
    insert(head,s)
head=pre
print("The length of linked list is",getCount(head))
while head:
    print(head.data,end=" ")
    head=head.next