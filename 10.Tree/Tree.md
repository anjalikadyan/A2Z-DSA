## Tree Data Structure

### Definition
A **Tree** is a non-linear data structure that stores values in a hierarchical manner.

### Binary Tree
A **Binary Tree** is a tree in which every node has at most two child nodes.

### Terminologies
1. **Node**: Represents a value in the tree.
2. **Root**: The topmost node in the tree.
3. **Children and Parent**: If a node is divided into two or fewer child nodes, then those are called **children**, and the original node is called the **parent**.
4. **Sibling**: If two or more nodes share the same parent, they are called **siblings**.
5. **Ancestor**: Nodes on the path from a given node up to the root node are called **ancestors** of that node.
6. **Descendant**: Nodes on the path from a given node down to the last node in its branch are called **descendants** of that node.
7. **Leaf**: The last nodes in the tree (nodes without children) are called **leaf nodes**.

### Java Representation of a Tree
```java
class Node {
    int data;
    Node left;
    Node right;
    
    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    Node root;
    
    public BinaryTree(int data) {
        root = new Node(data);
    }
}
```

This code defines a **Node** class with `data`, `left`, and `right` properties and initializes them in the constructor. The `BinaryTree` class starts with a root node.

