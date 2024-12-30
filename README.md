#A2Z-DSA
DSA Series in Python

Why is DSA Important?
-Data Structure is a way to organize data in the main memory or RAM. An algorithm is the
 sequence of steps you write in code to solve a problem. When programming, memory is 
 required to store and process data during program execution. DSA teaches us different 
 methods to store data in memory to allow faster retrieval, as well as various algorithms 
 for solving problems.

Learning DSA helps us:

1-Write efficient code that runs faster.
2-Save hardware costs.
3-Optimize CPU cycles.
4-Become better programmers overall.
*Additionally, DSA is a key topic for most companies during job interviews.

Roadmap to Learn DSA:

1-Learn a programming language: Start with Python.
2-Understand the basics of DSA: Learn and implement foundational concepts.
3-Practice daily: Focus on one topic at a time and build a habit of solving problems regularly.

Asymptotic Analysis:Asymptotic analysis is a theoretical and mathematical measurement used 
to evaluate the efficiency of an algorithm. It helps compare algorithms without depending 
on factors like the machine or programming language used. This approach allows us to 
determine the better algorithm purely based on its performance.

Best, Average, and Worst Cases:
Best Case: Minimum time taken by the algorithm to run.
Average Case: Based on assumptions about the input, the average time taken by the algorithm to run.
Worst Case: Maximum time taken by the program. Worst-case analysis is critical because programs often deal with varying inputs.

Example Code 1:
# Code 1
a = 10
sum = 0
for i in range(a):
    sum += i

Time Complexity: Big O(a) or .
Space Complexity: Big O(1).



# Code 2
// Here c is a constant
for (int i = 1; i <= c; i++) {
    // some O(1) expressions
}

Time Complexity: Big O(1).
Space Complexity: Big O(1).

# Code 3
// Here c is a positive integer constant
for (int i = 1; i <= n; i += c) {
    // some O(1) expressions
}

for (int i = n; i > 0; i -= c) {
    // some O(1) expressions
}

Time Complexity: Big O(n).
Space Complexity: Big O(1).

# Code 4
for (int i = 1; i <= n; i *= c) {
    // some O(1) expressions
}

for (int i = n; i > 0; i /= c) {
    // some O(1) expressions
}

Time Complexity: Big O(\log n).
Space Complexity: Big O(1).

Notations:
1-Big O Notation: Represents the exact or upper bound of the order of growth. For example,  means the growth is linear or less.
2-Theta Notation (): Represents the exact order of growth.
3-Omega Notation (): Represents the exact or lower bound. For example,  indicates a constant or greater value.

Analysis of Recursion:
#Create a recursion relation.
#Solve the relation.

Recursion Tree Method Example:
For :
Level 1:   C
          |---- C
Level 2:   C
          |---- C
          C
          |---- C
          ----

Total:  (log base 2 of n levels)
Time Complexity: .

Time Complexity:The time taken by an algorithm to run as a function of the input length. It helps create better programs and compare algorithms.
Big O Notation: Upper bound.
Theta Notation: Average bound.
Omega Notation: Lower bound.

Time Complexity Classes:
Constant Time: O(1)
Linear Time: O(n)
Logarithmic Time:O(log n)  (e.g., Binary Search)
Quadratic Time: O(n^2) (e.g., Nested Loops)
Cubic Time: O(n^3) (e.g., Deeply Nested Loops)


O(n!)           ^
O(2^n)        |
O(n^3)        |
O(n^2)        |
O(n \log n)    |     Complexity
O(n)          |
O(\log n)     |
O(1)          |

Space Complexity:The amount of memory required by an algorithm as a function of the input
 size.
Example: If we use a vector or array of size , the space complexity is .

Auxiliary Space:Extra or temporary memory used by an algorithm based on the input size.
 It is often used to compare algorithms.

Example Code 2:
# Code 5
int fun(int n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


