# Linked List

## Overview

A linked list is a fundamental data structure that uses non-contiguous memory allocation. It can be stored in various memory structures such as the stack, heap, and deque. Compared to arrays, linked lists offer more efficient insertion and deletion operations.

## Types of Linked Lists

### 1. Singly Linked List

A singly linked list consists of a collection of nodes. Each node has two attributes:

- **Data**: Stores the value.
- **Pointer**: Points to the address of the next node.

**Example:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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
```

### 2. Doubly Linked List

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

