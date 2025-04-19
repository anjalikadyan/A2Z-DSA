# A2Z-DSA

### DSA Series in Python

---

## Table of Contents
1. [Introduction to DSA](#introduction-to-dsa)
2. [Time and Space Complexity](#time-and-space-complexity)
3. [Data Structures](#data-structures)
4. [Algorithms](#algorithms)
5. [Mathematical Problems](#mathematical-problems)

---

## Introduction to DSA

### Why is DSA Important?

Data Structures and Algorithms (DSA) form the foundation of computer science and programming. They are essential for writing efficient and optimized code. Here's why DSA is crucial:

1. **Efficiency**: DSA helps write code that runs faster and uses fewer resources.
2. **Problem Solving**: Provides systematic approaches to solve complex problems.
3. **Optimization**: Helps optimize both time and space usage in programs.
4. **Career Growth**: Essential for technical interviews and career advancement.

### Benefits of Learning DSA:

1. **Write efficient code**: Optimize your programs to run faster.
2. **Save hardware costs**: Efficient code requires fewer resources.
3. **Optimize CPU cycles**: Better algorithms mean less processing time.
4. **Become a better programmer**: Develop systematic problem-solving skills.

---

## Time and Space Complexity

### Asymptotic Analysis

Asymptotic analysis is a mathematical approach to evaluate algorithm efficiency. It helps compare algorithms independently of hardware or programming language.

#### Best, Average, and Worst Cases:

- **Best Case**: Minimum time taken by the algorithm to run.
- **Average Case**: Expected time based on random inputs.
- **Worst Case**: Maximum time taken by the algorithm.

#### Big O Notation

Big O notation describes the upper bound of an algorithm's growth rate:

```
Growth Rate Comparison:
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

| Complexity Class | Description | Example | Visual Representation |
|-----------------|-------------|---------|----------------------|
| O(1) | Constant time | Array access | ```
  |
  |________________
``` |
| O(log n) | Logarithmic time | Binary search | ```
  /
 / 
/________________
``` |
| O(n) | Linear time | Linear search | ```
  /
 /
/________________
``` |
| O(n log n) | Linearithmic time | Merge sort | ```
  /
 / 
/________________
``` |
| O(n²) | Quadratic time | Bubble sort | ```
  /
 / 
/________________
``` |
| O(2ⁿ) | Exponential time | Recursive Fibonacci | ```
  /
 / 
/________________
``` |
| O(n!) | Factorial time | Permutations | ```
  /
 / 
/________________
``` |

### Space Complexity

Space complexity measures the amount of memory an algorithm needs relative to input size:

```
Memory Usage Types:
1. Input Space: Memory for storing input data
2. Auxiliary Space: Extra space used during execution
3. Total Space: Input space + Auxiliary space
```

---

## Data Structures

### 1. Arrays and Strings

#### Arrays
Arrays are contiguous blocks of memory storing elements of the same type.

```
Array Memory Layout:
+---+---+---+---+---+
| 1 | 2 | 3 | 4 | 5 |
+---+---+---+---+---+
  ↑   ↑   ↑   ↑   ↑
  0   1   2   3   4  (indices)
```

```python
# Array operations
arr = [1, 2, 3, 4, 5]
print(arr[0])  # Access: O(1)
arr.append(6)  # Append: O(1)
arr.pop()      # Pop: O(1)
```

#### Strings
Strings are sequences of characters with various operations:

```
String Memory Layout:
+---+---+---+---+---+
| H | e | l | l | o |
+---+---+---+---+---+
  ↑   ↑   ↑   ↑   ↑
  0   1   2   3   4  (indices)
```

```python
# String operations
s = "Hello"
print(s[0])        # Access: O(1)
s += " World"      # Concatenation: O(n)
print(len(s))      # Length: O(1)
```

### 2. Linked Lists

A linked list is a linear data structure where elements are linked using pointers.

#### Types:

1. **Singly Linked List**:
```
+---+     +---+     +---+
| 1 | --> | 2 | --> | 3 |
+---+     +---+     +---+
```

2. **Doubly Linked List**:
```
+---+     +---+     +---+
| 1 | <-> | 2 | <-> | 3 |
+---+     +---+     +---+
```

3. **Circular Linked List**:
```
+---+     +---+     +---+
| 1 | --> | 2 | --> | 3 |
+---+     +---+     +---+
   ^                   |
   |___________________|
```

#### Operations:
- Insertion: O(1) at head, O(n) at tail
- Deletion: O(1) at head, O(n) at tail
- Search: O(n)

### 3. Trees

#### Binary Tree
A tree where each node has at most two children.

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

#### Binary Search Tree (BST)
A binary tree with ordering property:
- Left subtree values < Node value
- Right subtree values > Node value

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

#### AVL Tree
A self-balancing BST where height difference between subtrees is at most 1.

```
Before Rotation:
    3
   /
  2
 /
1

After Rotation:
  2
 / \
1   3
```

---

## Algorithms

### 1. Searching Algorithms

#### Linear Search
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for unsorted arrays

```
Linear Search Process:
+---+---+---+---+---+
| 5 | 2 | 8 | 1 | 3 |
+---+---+---+---+---+
  ↑
  Start
```

#### Binary Search
- Time Complexity: O(log n)
- Space Complexity: O(1)
- Requires sorted array

```
Binary Search Process:
+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
+---+---+---+---+---+---+---+---+
  ↑           ↑               ↑
 low         mid            high
```

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 2. Sorting Algorithms

#### Bubble Sort
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Stable sorting algorithm

```
Bubble Sort Process:
Pass 1: [5, 3, 8, 4, 2] → [3, 5, 4, 2, 8]
Pass 2: [3, 5, 4, 2, 8] → [3, 4, 2, 5, 8]
Pass 3: [3, 4, 2, 5, 8] → [3, 2, 4, 5, 8]
Pass 4: [3, 2, 4, 5, 8] → [2, 3, 4, 5, 8]
```

#### Merge Sort
- Time Complexity: O(n log n)
- Space Complexity: O(n)
- Stable sorting algorithm

```
Merge Sort Process:
        [5, 3, 8, 4, 2]
        /             \
   [5, 3, 8]       [4, 2]
    /     \         /   \
 [5, 3]   [8]     [4]   [2]
  /   \
[5]   [3]
```

### 3. Graph Algorithms

#### Depth-First Search (DFS)
- Time Complexity: O(V + E)
- Space Complexity: O(V)
- Uses stack or recursion

```
DFS Traversal:
    A
   / \
  B   C
 / \   \
D   E   F

DFS Order: A → B → D → E → C → F
```

#### Breadth-First Search (BFS)
- Time Complexity: O(V + E)
- Space Complexity: O(V)
- Uses queue

```
BFS Traversal:
    A
   / \
  B   C
 / \   \
D   E   F

BFS Order: A → B → C → D → E → F
```

### 4. Dynamic Programming

Dynamic Programming is a method for solving complex problems by breaking them down into simpler subproblems.

#### Key Concepts:
1. **Overlapping Subproblems**: Problems that can be broken down into smaller subproblems
2. **Optimal Substructure**: Optimal solution can be constructed from optimal solutions of subproblems
3. **Memoization**: Storing results of expensive function calls

#### Example: Fibonacci Sequence
```
Fibonacci Tree:
        fib(5)
       /       \
    fib(4)     fib(3)
    /   \      /   \
fib(3) fib(2) fib(2) fib(1)
```

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

---

## Mathematical Problems

### 1. Number Theory

#### Prime Numbers
- Sieve of Eratosthenes: O(n log log n)
- Prime Factorization: O(√n)

```
Sieve of Eratosthenes:
2  3  4  5  6  7  8  9  10
2  3  X  5  X  7  X  9  X
2  3  X  5  X  7  X  X  X
```

#### GCD and LCM
- Euclidean Algorithm: O(log min(a,b))
- LCM using GCD: O(log min(a,b))

```
Euclidean Algorithm:
gcd(48, 18) = gcd(18, 12)
             = gcd(12, 6)
             = gcd(6, 0)
             = 6
```

### 2. Combinatorics

#### Permutations and Combinations
- Factorial: O(n)
- nCr: O(n)

```
Permutations of ABC:
ABC
ACB
BAC
BCA
CAB
CBA
```

### 3. Modular Arithmetic

#### Properties:
1. (a + b) mod m = (a mod m + b mod m) mod m
2. (a * b) mod m = (a mod m * b mod m) mod m
3. (a - b) mod m = (a mod m - b mod m + m) mod m

---

## Advanced Topics

### 1. Bit Manipulation

#### Bitwise Operations:
- AND (&): Sets bit to 1 if both bits are 1
- OR (|): Sets bit to 1 if either bit is 1
- XOR (^): Sets bit to 1 if bits are different
- NOT (~): Inverts all bits
- Left Shift (<<): Multiplies by 2
- Right Shift (>>): Divides by 2

```
Bitwise Operations:
5 & 3 = 1
5 | 3 = 7
5 ^ 3 = 6
~5 = -6
5 << 1 = 10
5 >> 1 = 2
```

### 2. Hashing

#### Hash Table Operations:
- Insert: O(1) average, O(n) worst
- Search: O(1) average, O(n) worst
- Delete: O(1) average, O(n) worst

```
Hash Table with Chaining:
[0] -> (key1, value1) -> (key2, value2)
[1] -> (key3, value3)
[2] -> NULL
[3] -> (key4, value4)
```

#### Collision Resolution:
1. **Chaining**: Using linked lists
2. **Open Addressing**: Linear/Quadratic probing

### 3. Backtracking

#### Applications:
1. N-Queens Problem
2. Sudoku Solver
3. Maze Pathfinding
4. Subset Generation

```
N-Queens Solution:
+---+---+---+---+
| Q |   |   |   |
+---+---+---+---+
|   |   | Q |   |
+---+---+---+---+
|   |   |   | Q |
+---+---+---+---+
|   | Q |   |   |
+---+---+---+---+
```

---

## Practice Resources

1. **Online Judges**:
   - LeetCode
   - HackerRank
   - Codeforces
   - CodeChef

2. **Books**:
   - "Introduction to Algorithms" by CLRS
   - "Algorithm Design Manual" by Steven Skiena
   - "Cracking the Coding Interview" by Gayle Laakmann McDowell

3. **Courses**:
   - MIT OpenCourseWare
   - Coursera
   - edX

---

## Conclusion

DSA is a fundamental aspect of computer science that helps in writing efficient and optimized code. Regular practice and understanding of these concepts are essential for becoming a better programmer and solving complex problems effectively.