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
## Extended Binary Tree

An **Extended Binary Tree** (also known as a **2-tree** or **Full Binary Tree**) is a type of binary tree where each node has either **0** or **2** children.

### Node Classification
- A node with **0 children** is called an **External Node (Leaf Node)**.
- A node with **2 children** is called an **Internal Node**.

### Example Representation

```
        (I)
       /   \
     (I)   (I)
    /   \   /   \
  (E)   (E) (I)   (I)
           /   \
         (E)   (E)
```

Where **(I)** represents an internal node and **(E)** represents an external node.

### Properties of an Extended Binary Tree
1. If **n** is the total number of nodes in the tree, then the number of **internal nodes (I)** and **external nodes (E)** are related as:
   
   \[ E = I + 1 \]

2. The total number of nodes **N** in an extended binary tree can be found using:
   
   \[ N = 2I + 1 \]

3. The height of the tree is determined by the longest path from the root to an external node.

4. Every internal node has exactly **two children**, ensuring a balanced structure in terms of node connectivity.

### Applications
- Expression trees in compilers.
- Decision trees in machine learning.
- Huffman coding trees in data compression.
- Binary search trees in computer science.

An extended binary tree is an essential concept in **tree data structures**, providing a foundational basis for various computational applications.

## Tree Structure Example

- Root  
  - Branch 1  
    - Leaf 1.1  
    - Leaf 1.2  
  - Branch 2  
    - Sub-branch 2.1  
      - Leaf 2.1.1  
      - Leaf 2.1.2  
    - Sub-branch 2.2  
      - Leaf 2.2.1  

# AVL Tree

## Introduction
An AVL tree is a self-balancing binary search tree (BST) where the difference between the heights of left and right subtrees cannot be more than one for all nodes. This balance condition ensures that the tree remains balanced, providing efficient operations.

## Properties
1. **Self-balancing**: The height difference between left and right subtrees (balance factor) is at most 1.
2. **BST Property**: Left subtree values are smaller than the node, and right subtree values are greater.
3. **Rotations**: To maintain balance, the AVL tree uses rotations:
   - Right Rotation (LL Rotation)
   - Left Rotation (RR Rotation)
   - Left-Right Rotation (LR Rotation)
   - Right-Left Rotation (RL Rotation)

## Example
### Insertions and Rotations
Consider inserting the following values into an empty AVL tree:
**10, 20, 30, 40, 50, 25**

1. Insert **10** → No rotation needed.
2. Insert **20** → No rotation needed.
3. Insert **30** → The tree becomes unbalanced (Right-heavy). Perform **RR Rotation** at node 10.
4. Insert **40** → No rotation needed.
5. Insert **50** → The tree becomes unbalanced (Right-heavy). Perform **RR Rotation** at node 20.
6. Insert **25** → The tree becomes unbalanced (Right-Left case at node 30). Perform **RL Rotation** at node 30.

### Final AVL Tree Structure
```
        30
       /  \
     20    40
    /  \     \
   10   25    50
```

## Applications
- Database Indexing
- Memory Management
- File Systems

## Conclusion
AVL trees provide efficient operations with **O(log n)** complexity for insertions, deletions, and lookups. By maintaining balance using rotations, they ensure optimal performance for dynamic datasets.



