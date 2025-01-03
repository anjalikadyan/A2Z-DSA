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

> *Additionally, DSA is a key topic for most companies during job interviews.*

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

### Example: Comparing Complexities

```python
# Example to illustrate time complexity
import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Comparing the two methods
arr = list(range(1, 1000000))
target = 999999

start = time.time()
linear_search(arr, target)
print("Linear Search Time:", time.time() - start)

start = time.time()
binary_search(arr, target)
print("Binary Search Time:", time.time() - start)
```

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

Here’s a summary of the key points about **Hashing in Data Structures and Algorithms (DSA)**:

---

### Hashing in DSA**

**Hashing** is a technique used to store and retrieve data efficiently by mapping keys to fixed-size indexes using a **hash function**. It significantly improves the time complexity for operations like insertion, deletion, and searching compared to other data structures.

---

### **Key Concepts**

1. **Hash Function**:
   - A function that converts a key into an index for the hash table. Example: `key % table_size`.

2. **Hash Table**:
   - A structure that stores key-value pairs. The hash function determines where each pair is stored.

3. **Collision**:
   - Occurs when two keys hash to the same index. Collision resolution is necessary to maintain data integrity.

---

### **Operations in Hashing**

1. **Insert**: Use the hash function to find an index and store the key-value pair.
2. **Search**: Use the hash function to locate the index and retrieve the value.
3. **Delete**: Use the hash function to locate the index and remove the key-value pair.

---

### **Collision Resolution Techniques**

1. **Chaining**: Each table index holds a linked list. Multiple keys that hash to the same index are stored in the list.
2. **Open Addressing**: All elements are stored in the table. If a collision occurs, methods like **linear probing**, **quadratic probing**, and **double hashing** are used to find the next available index.

---

### **Advantages of Hashing**

1. **Fast Access**: Average time complexity for insertion, deletion, and search is \(O(1)\).
2. **Efficient Memory Usage**: Hash tables store data compactly, ensuring efficient memory usage.

---

### **Example: Hash Table with Chaining**

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
                self.table[index].remove((k, v))  # Remove old pair
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

# Example Usage
hash_table = HashTable(10)
hash_table.insert(1, "one")
hash_table.insert(11, "eleven")
print(hash_table.search(11))  # Output: eleven
hash_table.delete(11)
print(hash_table.search(11))  # Output: None
```

---

### **Conclusion**

Hashing is essential for efficient data retrieval and storage, especially in cases like databases, caches, and implementing hash maps. It helps achieve fast access to data with \(O(1)\) time complexity, but requires careful collision handling to maintain performance.

---

# Sorting Algorithms for Arrays

### Selection Sort:
- Works by repeatedly finding the minimum element and swapping it.
- Time Complexity: **O(n^2)** (all cases).
- Space Complexity: **O(1)**.

### Bubble Sort:
- Repeatedly compares and swaps adjacent elements.
- Time Complexity: **O(n^2)** (worst and average), **O(n)** (best).
- Space Complexity: **O(1)**.

### Insertion Sort:
- Iteratively inserts elements into their correct position.
- Time Complexity: **O(n)** (best), **O(n^2)** (average and worst).
- Space Complexity: **O(1)**.

### Merge Sort Algorithm
- **Merge Sort** is a **divide-and-conquer** sorting algorithm.
- It is both **efficient** and **stable**.
- The algorithm works by dividing the array into two halves until no further division is possible. Each subarray is then sorted recursively and merged back together in sorted order.

### Time Complexity
1. **Best Case**:
   - **O(n log n)**
   - Occurs when the array is already sorted or nearly sorted.

2. **Average Case**:
   - **O(n log n)**
   - Occurs when the array is randomly ordered.

3. **Worst Case**:
   - **O(n log n)**
   - Occurs when the array is sorted in reverse order.

### Auxiliary Space
- **O(n)**:
  - Additional space is required for the temporary arrays used during the merge process.




