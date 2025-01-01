# Hashing in DSA

Hashing is a data structure technique that helps in significantly reducing the time complexity for operations like traversing, deleting, and searching compared to other methods. It is extensively used in **Data Structures and Algorithms (DSA)** to map data (keys) into a fixed-size table (called a hash table) using a function (called a hash function). This technique is fundamental in scenarios requiring fast data retrieval, such as database indexing, caches, and implementing data structures like hash maps and hash sets.

---

## Hash Table

A **hash table** is a data structure that stores key-value pairs. It uses a hash function to compute an index (or position) in an underlying array for storing the value. The table can either be ordered or unordered, depending on the implementation.

### Types of Hash Tables:
1. **Ordered Map (Map)**: The time complexity for operations is \(O(\log n)\).
2. **Unordered Map (Hash Map)**: The time complexity for most operations is \(O(1)\) in the average case.

---

## Key Concepts in Hashing

1. **Hash Function**:
   - A mathematical function that takes a key as input and returns an index (position) in the hash table where the key-value pair is to be stored.
   - Example:
     ```python
     def hash_function(key):
         return key % table_size
     ```
     Here, the `key` is divided by the `table_size`, and the remainder is used as the index.

2. **Hash Table**:
   - A data structure that stores key-value pairs.
   - The hash function is responsible for determining where the data should be stored within the table.

3. **Collision**:
   - A **collision** occurs when two different keys generate the same hash value (index).
   - Collisions need to be handled to ensure that the data remains consistent in the table.

---

## Hashing Operations

### 1. **Insert**:
   - To insert a key-value pair, the hash function is applied to calculate the index, and the pair is stored at that index.

### 2. **Search**:
   - To search for a key, the hash function calculates the index, and the value at that index is retrieved.

### 3. **Delete**:
   - To delete a key, the hash function is used to locate the index of the key, and the key-value pair is removed from the table.

---

## Collision Resolution Techniques

Since collisions are inevitable when using hashing, there are several techniques to handle them:

### 1. **Chaining**:
   - Chaining involves creating a linked list at each index in the hash table.
   - If multiple keys hash to the same index, they are stored in the linked list at that index.
   - **Example**:
     ```python
     class HashTable:
         def __init__(self, size):
             self.size = size
             self.table = [[] for _ in range(size)]  # List of empty lists

         def hash_function(self, key):
             return key % self.size

         def insert(self, key, value):
             index = self.hash_function(key)
             # Check if the key already exists in the list at the index
             for i, (k, v) in enumerate(self.table[index]):
                 if k == key:
                     self.table[index][i] = (key, value)
                     return
             self.table[index].append((key, value))  # Add a new pair

         def search(self, key):
             index = self.hash_function(key)
             for k, v in self.table[index]:
                 if k == key:
                     return v
             return None  # Key not found

         def delete(self, key):
             index = self.hash_function(key)
             for i, (k, v) in enumerate(self.table[index]):
                 if k == key:
                     del self.table[index][i]  # Remove the pair
                     return True
             return False  # Key not found
     ```

### 2. **Open Addressing**:
   - In open addressing, all elements are stored within the hash table itself.
   - When a collision occurs, a secondary strategy is used to find the next available position.
   
   There are different strategies to handle collisions in open addressing:

   - **Linear Probing**: 
     - Check the next index sequentially until an available spot is found.
   - **Quadratic Probing**: 
     - Check indices with quadratic increments (e.g., 1, 4, 9, 16...).
   - **Double Hashing**: 
     - Use a secondary hash function to determine the next index to check.

---

## Advantages of Hashing

1. **Fast Data Access**:
   - Hashing provides efficient data access. In an ideal case, operations like insertion, deletion, and search have a time complexity of \(O(1)\).
   
2. **Efficient Memory Usage**:
   - Data is stored in compact and effective structures, allowing for efficient use of memory.

---

## Python Example: Hash Table with Chaining

Here’s an example of how you can implement a hash table with chaining in Python:

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists (chaining)

    def hash_function(self, key):
        return key % self.size  # Simple hash function

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key already exists in the linked list at the index
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update value if key exists
                return
        self.table[index].append((key, value))  # Add new key-value pair

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the pair from the list
                return True
        return False  # Key not found

# Example Usage
hash_table = HashTable(10)
hash_table.insert(1, "one")
hash_table.insert(11, "eleven")
hash_table.insert(21, "twenty-one")

print(hash_table.search(11))  # Output: eleven
hash_table.delete(11)
print(hash_table.search(11))  # Output: None
```

### Example Walkthrough:
- The hash table is created with 10 slots (buckets).
- Inserting the key-value pair `(1, "one")`, the hash function calculates `1 % 10 = 1`, so "one" is inserted at index 1.
- Similarly, the key-value pair `(11, "eleven")` hashes to index 1, causing a collision. Using chaining, it is stored in the list at index 1.
- Searching for the key `11` finds the corresponding value "eleven".
- Deleting the key `11` removes it from the list at index 1.

---

## Conclusion

Hashing is an essential concept in data structures and algorithms. It allows for efficient data access with constant-time complexity for most operations. Proper collision resolution techniques like chaining and open addressing ensure that hash tables can handle collisions gracefully. With its fast retrieval times and efficient memory usage, hashing is widely used in applications like databases, caches, and implementing hash maps.

