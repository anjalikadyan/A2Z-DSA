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


##Quick Sort

Quick Sort is a **divide-and-conquer** algorithm that efficiently sorts arrays by recursively partitioning them based on a selected pivot element. 

### Key Points:
1. **Pivot Selection**: A pivot can be chosen randomly, or from the first or last element.
2. **Partitioning**:
   - Elements smaller than the pivot go to the left.
   - Elements larger than the pivot go to the right.
3. **Recursion**: The same process is applied to the left and right subarrays until all subarrays contain one element.

### Time Complexity:
- **Best Case**: Ω(n log n) - When the pivot splits the array evenly.
- **Average Case**: Θ(n log n) - For most cases.
- **Worst Case**: O(n²) - When the array is already sorted or reverse-sorted, and the smallest or largest element is chosen as the pivot.

### Auxiliary Space:
- **O(n)** - Space used by the recursive call stack.

### Example:
#### Input: `[8, 3, 7, 6, 2]`
#### Output: `[2, 3, 6, 7, 8]`

### Python Code:
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example Usage
arr = [8, 3, 7, 6, 2]
print(quick_sort(arr))  # Output: [2, 3, 6, 7, 8]
```

### Advantages:
- Highly efficient for large datasets.
- Average and best-case time complexity are **O(n log n)**.

### Disadvantages:
- Worst-case time complexity is **O(n²)**.
- Recursive nature can cause stack overflow for very large arrays if not optimized.

# **Backtracking**

**Backtracking** is an algorithmic approach that uses recursion and a "try-and-error" strategy to explore all possible solutions to a problem. If a solution does not meet the defined conditions, the algorithm backtracks (undoes the last step) and tries a different path. It is particularly useful for solving problems with multiple constraints or configurations, such as puzzles, pathfinding, and combinatorial problems.

---

## **Key Steps in Backtracking**  
1. **Define the Problem**: Specify the conditions for a valid solution.  
2. **Use Recursion**: Explore potential solutions step-by-step.  
3. **Undo and Retry**: Backtrack if the current solution does not satisfy the conditions and try alternative paths.

---

### **Examples**  
1. **N-Queens Problem**:  
   - **Goal**: Place N queens on an N×N chessboard such that no two queens threaten each other.  
   - **Approach**: Place queens row by row, validate their positions, and backtrack if conflicts arise.  

2. **Maze Problem (Pathfinding)**:  
   - **Goal**: Find a path from the start to the destination in a grid-based maze.  
   - **Approach**: Recursively move to neighboring cells, backtrack if a dead-end is reached, and explore alternate paths.  

3. **Generating All Subsets of a Set**:  
   - **Goal**: Create all possible subsets of a given set.  
   - **Approach**: Include or exclude elements recursively, backtracking to explore all combinations.

---

### **Applications of Backtracking**  
- Solving combinatorial problems (e.g., subsets, permutations).  
- Pathfinding in mazes or graphs.  
- Puzzle-solving (e.g., Sudoku, N-Queens).  
- Optimizing resource allocation problems.

Backtracking is a powerful problem-solving technique but can be computationally expensive for large input sizes.

Here is the content for your `README.md`:

```markdown
## Binary Search Algorithm

### Description

Binary Search is a highly efficient algorithm used to find an element in a **sorted array**. It works by repeatedly dividing the search interval in half, narrowing down the potential location of the target element.

#### Steps:
1. Start with two pointers (`low` and `high`) representing the boundaries of the array.
2. Find the middle element of the array.
3. Compare the middle element with the target:
   - If the middle element is the target, return the index.
   - If the middle element is larger than the target, search the left half.
   - If the middle element is smaller than the target, search the right half.
4. Repeat the process until the target is found or the pointers cross.

### Time and Space Complexity

- **Time Complexity**: `O(log n)` - Each step halves the array size, making it much faster than linear search for large datasets.
- **Space Complexity**: `O(1)` - No additional space required for iterative implementation.

### Binary Search Algorithm Example

#### Example 1: Searching for an element in an array.

Given a sorted array:

```python
arr = [1, 3, 5, 7, 9, 11, 13, 15]
```

#### Binary Search Code:

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

#### Example 2: Searching for the target value `7`:

```python
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
```

#### Output:

```
Element found at index 3
```

### Usage

1. The array must be sorted.
2. Call the `binary_search` function, passing the array and the target element as arguments.

---

### Conclusion

Binary search is a powerful and efficient algorithm when applied to sorted arrays. It offers significant performance improvements over linear search, especially as the size of the array grows.
```
```
## Strings in Python

A **string** is a data type in programming used to represent a sequence of characters. Strings can include letters, numbers, symbols, and spaces. They are typically enclosed in **quotation marks**: either single (`'`) or double (`"`).

## Examples of Strings
- `"Hello, World!"`  
- `'Python is fun!'`  
- `"12345"` (a string of numbers, not actual integers)  
- `'!@#$%^&*()'` (a string of symbols)

## String in Python
In Python, strings are created by enclosing text in quotes:

```python
# Examples of strings
string1 = "Hello, World!"
string2 = 'Python is fun!'
string3 = "12345"  # This is a string, not an integer
```

## Operations with Strings
You can perform various operations with strings, such as:

### 1. Concatenation (joining strings):
```python
greeting = "Hello"
name = "Alice"
result = greeting + ", " + name + "!"
print(result)  # Output: Hello, Alice!
```

### 2. Repetition:
```python
word = "Hi"
repeated = word * 3
print(repeated)  # Output: HiHiHi
```

### 3. Accessing Characters:
```python
my_string = "Python"
print(my_string[0])  # Output: P (first character)
print(my_string[-1])  # Output: n (last character)
```

### 4. String Length:
```python
my_string = "Hello"
print(len(my_string))  # Output: 5
```

### 5. String Methods:
```python
text = "hello"
print(text.upper())  # Output: HELLO
print(text.capitalize())  # Output: Hello
print(text.replace('l', 'r'))  # Output: herro
```



