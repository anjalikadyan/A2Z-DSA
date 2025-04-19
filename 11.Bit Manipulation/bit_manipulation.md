
# Introduction to Bit Manipulation

Bit manipulation is the process of performing operations directly on binary digits or bits. These operations are fundamental in computer science and are particularly useful in scenarios where performance and memory optimization are crucial.

Every number in a computer is stored in binary — a sequence of 0s and 1s. Understanding how to manipulate these bits can unlock faster and more efficient code.

---

## Why Bit Manipulation?

- **Efficiency**: Bitwise operations are extremely fast and performed directly by the processor.
- **Memory Saving**: Allows compact data representations.
- **Low-Level Control**: Enables precise control over system-level programming, such as device drivers and embedded systems.
- **Problem Solving**: Simplifies problems that would be complex with arithmetic or logical operations.
- **Competitive Programming**: Provides elegant solutions to common algorithmic problems.

---

## Basic Bitwise Operators

These are binary operators — they operate on binary representations of integers.

| Operator     | Symbol | Description                                              |
|--------------|--------|----------------------------------------------------------|
| AND          | `&`    | Result is 1 only if both corresponding bits are 1        |
| OR           | `&#124;` | Result is 1 if at least one of the bits is 1           |
| XOR          | `^`    | Result is 1 only if the bits are different               |
| NOT          | `~`    | Inverts all the bits (1 becomes 0, and 0 becomes 1)      |
| Left Shift   | `<<`   | Shifts bits to the left, filling in with 0s              |
| Right Shift  | `>>`   | Shifts bits to the right, discarding the rightmost bits  |

---

## Visualizing Bitwise Operations

Let's take two numbers:

```text
a = 5  => 00000101  
b = 3  => 00000011
```

Now apply different bitwise operations:

### AND (`a & b`)
```text
  00000101
& 00000011
------------
  00000001  => 1
```

### OR (`a | b`)
```text
  00000101
| 00000011
------------
  00000111  => 7
```

### XOR (`a ^ b`)
```text
  00000101
^ 00000011
------------
  00000110  => 6
```

### NOT (`~a`)
```text
  ~00000101
  = 11111010 (in two's complement: -6)
```

---

## Bit Representation (Two's Complement)

In computing, **negative numbers** are represented using two's complement notation.

For example, in 8-bit:

- `5`  = `00000101`
- `-5` = `11111011` (invert the bits of 5 → `11111010`, then add 1)

---

## Common Bit Manipulation Techniques

1. **Check if a number is even or odd**  
   ```cpp
   if (n & 1)  
   ```

2. **Set the ith bit**  
   ```cpp
   n = n | (1 << i);  
   ```

3. **Clear the ith bit**  
   ```cpp
   n = n & ~(1 << i); 
   ```

4. **Toggle the ith bit**  
   ```cpp
   n = n ^ (1 << i);  
   ```

5. **Check the ith bit**  
   ```cpp
   if (n & (1 << i))  
   ```

6. **Multiply or divide by powers of two**  
   ```cpp
   n << 1  
   n >> 1  
   ```

---

## Bit Masking Diagram

Here's a simplified diagram to show how masking works:

```
Original number:     01010110  (86)
Mask (1 << 2):       00000100
Operation (AND):     01010110
                   & 00000100
                   -----------
                     00000100  → Bit 2 is set
```

---

## Applications of Bit Manipulation

- **Data compression** – Efficient packing of data into fewer bits.
- **Encryption algorithms** – Bit-level data scramblers.
- **Embedded systems** – Accessing hardware registers.
- **Game development** – Efficient data flagging and toggling.
- **Image processing** – Manipulating pixel data.
- **Permission systems** – Using bit flags to represent access levels.

---

## Summary Table

| Task                         | Operation                     |
|------------------------------|-------------------------------|
| Set ith bit                  | `n = n | (1 << i)`            |
| Clear ith bit                | `n = n & ~(1 << i)`           |
| Toggle ith bit               | `n = n ^ (1 << i)`            |
| Check ith bit is set         | `n & (1 << i)`                |
| Multiply by 2^k              | `n << k`                      |
| Divide by 2^k                | `n >> k`                      |
| Check if n is a power of 2   | `n & (n - 1) == 0`            |

---

## Conclusion

Bit manipulation is a core concept in systems programming and high-performance computing. With practice, it becomes an incredibly useful tool for simplifying logic, optimizing code, and controlling hardware behavior. Mastering it equips you to write faster, leaner, and smarter code.
```