# Linked List

## Overview

A linked list is a fundamental data structure that uses non-contiguous memory allocation. It can be stored in various memory structures such as the stack, heap, and deque. Compared to arrays, linked lists offer more efficient insertion and deletion operations.

## Types of Linked Lists

### Singly Linked List: Insertion and Deletion

A **Singly Linked List** is a data structure that consists of nodes, where each node contains:
- **Data**
- **Pointer** to the next node

### Insertion in a Singly Linked List
Insertion in a singly linked list can be performed at different positions:

### 1. Insertion at the Beginning
1. Create a new node.
2. Set the new node's `next` pointer to the current head.
3. Update the head to the new node.

**Code:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
```

#### 2. Insertion at the End
1. Create a new node.
2. Traverse to the last node.
3. Set the last node's `next` pointer to the new node.

**Code:**
```python
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
```

#### 3. Insertion at a Specific Position
1. Create a new node.
2. Traverse to the desired position.
3. Update the pointers to insert the new node.

**Code:**
```python
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
```

### Deletion in a Singly Linked List
Deletion can also be performed at different positions:

#### 1. Deletion at the Beginning
1. Update the head to point to the next node.

**Code:**
```python
    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next
```

#### 2. Deletion at the End
1. Traverse to the second last node.
2. Set its `next` pointer to `None`.

**Code:**
```python
    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
```

#### 3. Deletion at a Specific Position
1. Traverse to the node before the target node.
2. Update its `next` pointer to skip the target node.

**Code:**
```python
    def delete_at_position(self, position):
        if not self.head:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            return
        for _ in range(position - 1):
            if temp is None or temp.next is None:
                return
            temp = temp.next
        temp.next = temp.next.next
```

## Conclusion
A singly linked list allows dynamic memory allocation and efficient insertions and deletions at different positions. However, it lacks backward traversal and requires sequential access for searches.### 2. Doubly Linked List

A doubly linked list consists of nodes where:
- Each node contains **two pointers** (one pointing to the next node and another pointing to the previous node).
- This allows traversal in both forward and backward directions.
**Example:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
```

### 3. Circular Linked List

Circular linked lists can be classified into two types:

- **Singly Circular Linked List**: In this type, the last node stores the address of the first node in its pointer, creating a circular structure.
- **Doubly Circular Linked List**: In this type, the last node stores the address of the first node, and the first node stores the address of the last node, forming a complete circular connection in both directions.

**Example:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
```

