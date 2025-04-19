# A2Z-DSA

### DSA Series in Python

---

## Why is DSA Important?

Data Structure is a way to organize data in the main memory or RAM. An algorithm is the sequence of steps you write in code to solve a problem. When programming, memory is required to store and process data during program execution. DSA teaches us different methods to store data in memory to allow faster retrieval, as well as various algorithms for solving problems.

### Benefits of Learning DSA:

1. Write efficient code that runs faster.
2. Save hardware costs.
3. Optimize CPU cycles.
4. Become better programmers overall.
---

## Roadmap to Learn DSA

1. **Learn a programming language**: Start with Python.
2. **Understand the basics of DSA**: Learn and implement foundational concepts.
3. **Practice daily**: Focus on one topic at a time and build a habit of solving problems regularly.

---

## Asymptotic Analysis

Asymptotic analysis is a theoretical and mathematical measurement used to evaluate the efficiency of an algorithm. It helps compare algorithms without depending on factors like the machine or programming language used. This approach allows us to determine the better algorithm purely based on its performance.

### Best, Average, and Worst Cases:

- **Best Case**: Minimum time taken by the algorithm to run.
- **Average Case**: Based on assumptions about the input, the average time taken by the algorithm to run.
- **Worst Case**: Maximum time taken by the program. Worst-case analysis is critical because programs often deal with varying inputs.

### Notations:

1. **Big O Notation**: Represents the exact or upper bound of the order of growth. Example: O(n) means the growth is linear or less.
2. **Theta (Θ) Notation**: Represents the exact order of growth.
3. **Omega (Ω) Notation**: Represents the exact or lower bound. Example: Ω(1) indicates constant or greater growth.

---

## Time Complexity

Time complexity is the time taken by an algorithm to run as a function of the input length. It helps create better programs and compare algorithms.

### Common Time Complexity Classes:

- **Constant Time**: O(1)  
- **Logarithmic Time**: O(log n) (e.g., Binary Search)
- **Linear Time**: O(n)  
- **Linearithmic Time**: O(n log n) (e.g., Merge Sort)
- **Quadratic Time**: O(n²) (e.g., Nested Loops)
- **Cubic Time**: O(n³) (e.g., Deeply Nested Loops)
- **Exponential Time**: O(2ⁿ)
- **Factorial Time**: O(n!)

### Big O Complexity Chart:

| Complexity Class      | Examples                   |
|-----------------------|----------------------------|
| O(1)                 | Accessing an array element |
| O(log n)             | Binary Search              |
| O(n)                 | Linear Search              |
| O(n log n)           | Merge Sort, Quick Sort     |
| O(n²)                | Bubble Sort, Insertion Sort|
| O(2ⁿ)                | Recursive Fibonacci        |
| O(n!)                | Permutations               |

---

## Space Complexity

Space complexity refers to the amount of memory required by an algorithm as a function of the input size.

### Key Concepts:

- **Input Space**: Memory required to store input data.
- **Auxiliary Space**: Extra or temporary memory used by the algorithm.

### Example: Space Complexity of an Array

```python
# Space complexity example
n = 100
arr = [i for i in range(n)]
print("Space complexity of the array is O(n):", len(arr))
```

---

## Mathematical Problems and Recursion

### Mathematical Problems

1. **Count Digits**: Count the number of digits in a given number.
   ```python
   n = 12345
   print("Number of digits:", len(str(n)))
   ```

2. **Palindrome Numbers**: Check if a number is the same when reversed.
   ```python
   n = 121
   print("Is palindrome:", str(n) == str(n)[::-1])
   ```

3. **Factorial of a Number**: Calculate the factorial (n!) of a given number.
   ```python
   def factorial(n):
       return 1 if n == 0 else n * factorial(n - 1)

   print("Factorial:", factorial(5))
   ```

4. **Trailing Zeros in Factorial**: Find the number of trailing zeros in n!.
   ```python
   def trailing_zeros(n):
       count = 0
       while n >= 5:
           n //= 5
           count += n
       return count

   print("Trailing zeros:", trailing_zeros(100))
   ```

5. **GCD or HCF of Two Numbers**: Compute the greatest common divisor.
   ```python
   def gcd(a, b):
       while b:
           a, b = b, a % b
       return a

   print("GCD:", gcd(56, 98))
   ```

6. **LCM of Two Numbers**: Calculate the least common multiple.
   ```python
   def lcm(a, b):
       return abs(a * b) // gcd(a, b)

   print("LCM:", lcm(4, 5))
   ```

---

### Recursion

Recursion is a technique where a function calls itself directly or indirectly to solve a problem.

#### Key Recursion-based Algorithms

1. **Dynamic Programming**: Optimize recursive solutions by storing results to avoid recalculating.
2. **Backtracking**: Solve problems by trying potential solutions and backtracking when necessary.
3. **Divide and Conquer**: Solve problems by dividing them into smaller subproblems (e.g., Binary Search, Quick Sort, Merge Sort).

#### Example: Tower of Hanoi

```python
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

n = 3
print("Tower of Hanoi steps:")
tower_of_hanoi(n, 'A', 'C', 'B')
```

---

## Data Structures

### Strings in Python

A **string** is a data type in programming used to represent a sequence of characters. Strings can include letters, numbers, symbols, and spaces. They are typically enclosed in **quotation marks**: either single (`'`) or double (`"`).

#### Examples of Strings
- `"Hello, World!"`  
- `'Python is fun!'`  
- `"12345"` (a string of numbers, not actual integers)  
- `'!@#$%^&*()'` (a string of symbols)

#### Operations with Strings
1. **Concatenation (joining strings)**:
```python
greeting = "Hello"
name = "Alice"
result = greeting + ", " + name + "!"
print(result)  # Output: Hello, Alice!
```

2. **Repetition**:
```python
word = "Hi"
repeated = word * 3
print(repeated)  # Output: HiHiHi
```

3. **Accessing Characters**:
```python
my_string = "Python"
print(my_string[0])  # Output: P (first character)
print(my_string[-1])  # Output: n (last character)
```

4. **String Length**:
```python
my_string = "Hello"
print(len(my_string))  # Output: 5
```

5. **String Methods**:
```python
text = "hello"
print(text.upper())  # Output: HELLO
print(text.capitalize())  # Output: Hello
print(text.replace('l', 'r'))  # Output: herro
```

### Linked List

A **linked list** is a linear data structure in which elements (called **nodes**) are linked together using pointers. Unlike arrays, linked lists do not require contiguous memory locations, making them more flexible in dynamic memory allocation.

#### Types of Linked Lists
1. **Singly Linked List** – Each node has data and a pointer to the next node.
2. **Doubly Linked List** – Each node has data, a pointer to the next node, and a pointer to the previous node.
3. **Circular Linked List** – The last node points back to the first node, forming a loop.

#### Basic Structure of a Node (Singly Linked List in C++)
```cpp
struct Node {
    int data;
    Node* next;
};
```

#### Operations on Linked List
1. **Insertion** – Add a new node at the beginning, end, or a specific position.
2. **Deletion** – Remove a node from the list.
3. **Traversal** – Go through the list to access elements.
4. **Searching** – Find a node with a given value.

#### Usage
Linked lists are useful in scenarios where:
- Dynamic memory allocation is required.
- Frequent insertions and deletions occur.
- Memory utilization needs to be optimized.

### Tree Data Structures

#### Basic Tree

A **Tree** is a non-linear hierarchical data structure. A **Binary Tree** is a special kind of tree where each node has at most two children.

##### Terminologies
- **Node**: Represents a value.
- **Root**: Topmost node of the tree.
- **Children/Parent**: Direct connections between nodes.
- **Siblings**: Nodes with the same parent.
- **Ancestor/Descendant**: Nodes above or below a given node.
- **Leaf**: Node with no children.

##### Java Representation
```java
class Node {
    int data;
    Node left, right;
    Node(int data) { this.data = data; }
}
class BinaryTree {
    Node root;
    BinaryTree(int data) { root = new Node(data); }
}
```

#### Extended Binary Tree

An **Extended Binary Tree** (also known as a **2-tree** or **Full Binary Tree**) is a type of binary tree where each node has either **0** or **2** children.

##### Node Classification
- A node with **0 children** is called an **External Node (Leaf Node)**.
- A node with **2 children** is called an **Internal Node**.

#### AVL Tree

An AVL tree is a self-balancing binary search tree (BST) where the difference between the heights of left and right subtrees cannot be more than one for all nodes. This balance condition ensures that the tree remains balanced, providing efficient operations.

##### Properties
1. **Self-balancing**: The height difference between left and right subtrees (balance factor) is at most 1.
2. **BST Property**: Left subtree values are smaller than the node, and right subtree values are greater.
3. **Rotations**: To maintain balance, the AVL tree uses rotations:
   - Right Rotation (LL Rotation)
   - Left Rotation (RR Rotation)
   - Left-Right Rotation (LR Rotation)
   - Right-Left Rotation (RL Rotation)

---

## Algorithms

### Binary Search Algorithm

Binary Search is a highly efficient algorithm used to find an element in a **sorted array**. It works by repeatedly dividing the search interval in half, narrowing down the potential location of the target element.

#### Steps:
1. Start with two pointers (`low` and `high`) representing the boundaries of the array.
2. Find the middle element of the array.
3. Compare the middle element with the target:
   - If the middle element is the target, return the index.
   - If the middle element is larger than the target, search the left half.
   - If the middle element is smaller than the target, search the right half.
4. Repeat the process until the target is found or the pointers cross.

#### Time and Space Complexity
- **Time Complexity**: `O(log n)` - Each step halves the array size, making it much faster than linear search for large datasets.
- **Space Complexity**: `O(1)` - No additional space required for iterative implementation.

#### Example:
```python
def binary_search(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2  # Find middle element

        if array[mid] == target:
            return mid  # Target found
        elif array[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Target not found
```

### Sorting Algorithms

#### Selection Sort:
- Works by repeatedly finding the minimum element and swapping it.
- Time Complexity: **O(n^2)** (all cases).
- Space Complexity: **O(1)**.

#### Bubble Sort:
- Repeatedly compares and swaps adjacent elements.
- Time Complexity: **O(n^2)** (worst and average), **O(n)** (best).
- Space Complexity: **O(1)**.

#### Insertion Sort:
- Iteratively inserts elements into their correct position.
- Time Complexity: **O(n)** (best), **O(n^2)** (average and worst).
- Space Complexity: **O(1)**.

#### Merge Sort
- **Merge Sort** is a **divide-and-conquer** sorting algorithm.
- It is both **efficient** and **stable**.
- The algorithm works by dividing the array into two halves until no further division is possible. Each subarray is then sorted recursively and merged back together in sorted order.

##### Time Complexity
1. **Best Case**: **O(n log n)**
2. **Average Case**: **O(n log n)**
3. **Worst Case**: **O(n log n)**

##### Auxiliary Space: **O(n)**

#### Quick Sort
Quick Sort is a **divide-and-conquer** algorithm that efficiently sorts arrays by recursively partitioning them based on a selected pivot element.

##### Key Points:
1. **Pivot Selection**: A pivot can be chosen randomly, or from the first or last element.
2. **Partitioning**:
   - Elements smaller than the pivot go to the left.
   - Elements larger than the pivot go to the right.
3. **Recursion**: The same process is applied to the left and right subarrays until all subarrays contain one element.

##### Time Complexity:
- **Best Case**: Ω(n log n)
- **Average Case**: Θ(n log n)
- **Worst Case**: O(n²)

##### Auxiliary Space: **O(n)**

##### Example:
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
```

### Backtracking

**Backtracking** is an algorithmic approach that uses recursion and a "try-and-error" strategy to explore all possible solutions to a problem. If a solution does not meet the defined conditions, the algorithm backtracks (undoes the last step) and tries a different path.

#### Key Steps in Backtracking
1. **Define the Problem**: Specify the conditions for a valid solution.
2. **Use Recursion**: Explore potential solutions step-by-step.
3. **Undo and Retry**: Backtrack if the current solution does not satisfy the conditions and try alternative paths.

#### Examples
1. **N-Queens Problem**
2. **Maze Problem (Pathfinding)**
3. **Generating All Subsets of a Set**

#### Applications
- Solving combinatorial problems
- Pathfinding in mazes or graphs
- Puzzle-solving (e.g., Sudoku, N-Queens)
- Optimizing resource allocation problems

### Hashing

**Hashing** is a technique used to store and retrieve data efficiently by mapping keys to fixed-size indexes using a **hash function**.

#### Key Concepts
1. **Hash Function**: Converts a key into an index for the hash table.
2. **Hash Table**: Structure that stores key-value pairs.
3. **Collision**: Occurs when two keys hash to the same index.

#### Operations in Hashing
1. **Insert**: Use the hash function to find an index and store the key-value pair.
2. **Search**: Use the hash function to locate the index and retrieve the value.
3. **Delete**: Use the hash function to locate the index and remove the key-value pair.

#### Collision Resolution Techniques
1. **Chaining**: Each table index holds a linked list.
2. **Open Addressing**: All elements are stored in the table.

#### Example: Hash Table with Chaining
```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                self.table[index].remove((k, v))
                break
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
```

### Bit Manipulation

Bit manipulation is a technique used in programming to interact with individual bits of data. It is commonly used in systems programming, embedded systems, competitive programming, and areas where performance and memory efficiency are crucial.

#### Why Use Bit Manipulation?
- **Efficiency**: Bit operations are very fast
- **Memory Optimization**: Allows for compact data representation
- **Low-level Access**: Useful when working close to hardware

#### Bitwise Operators
| Operator | Symbol | Description            |
|----------|--------|------------------------|
| AND      | `&`    | 1 if both bits are 1   |
| OR       | `|`    | 1 if at least one is 1 |
| XOR      | `^`    | 1 if bits are different|
| NOT      | `~`    | Inverts all the bits   |
| LEFT SHIFT  | `<<` | Shifts bits left       |
| RIGHT SHIFT | `>>` | Shifts bits right      |

#### Examples
```cpp
// Check if a number is even or odd
if (num & 1) 
    cout << "Odd";
else 
    cout << "Even";
```