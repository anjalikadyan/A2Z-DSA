n = int(input())
a = int(input("number: "))
def searchKey(head, key):
        d=False
        while (head):
            if(head.data==key):
                d=True
            head=head.next
        return d
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
key = int(input("search key: "))
head=pre
print("Is the key is present in linked list:",searchKey(head,key))
while head:
    print(head.data,end=" ")
    head=head.next