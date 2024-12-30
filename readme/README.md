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


Notations:
1-Big O Notation: Represents the exact or upper bound of the order of growth. For example,  means the growth is linear or less.
2-Theta Notation: Represents the exact order of growth.
3-Omega Notation: Represents the exact or lower bound. For example,  indicates a constant or greater value.

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
Time Complexity: Big O(log n).

Time Complexity:The time taken by an algorithm to run as a function of the input length. It helps create better programs and compare algorithms.
Big O Notation: Upper bound.
Theta Notation: Average bound.
Omega Notation: Lower bound.

Time Complexity Classes:
Constant Time: Big O(1)
Linear Time: Big O(n)
Logarithmic Time: Big O(log n)  (e.g., Binary Search)
Quadratic Time: Big O(n^2) (e.g., Nested Loops)
Cubic Time: Big O(n^3) (e.g., Deeply Nested Loops)


Big O(n!)           ^
Big O(2^n)        |
Big O(n^3)        |
Big O(n^2)        |
Big O(n log n)    |     Complexity
Big O(n)          |
Big O(log n)     |
Big O(1)          |

Space Complexity:The amount of memory required by an algorithm as a function of the input size.
Example: If we use a vector or array of size , the space complexity is .

Auxiliary Space:Extra or temporary memory used by an algorithm based on the input size.
 It is often used to compare algorithms.

-->Mathematical Problems and Recursion:

#Mathematical Problems:
1-Count Digits: Count the number of digits in a given number.
2-Palindrome Numbers: Check if a number is the same when reversed.
3-Factorial of a Number: Calculate the factorial (n!) of a given number.
4-Trailing Zeros in Factorial: Find the number of trailing zeros in n!.
5-GCD or HCF of Two Numbers: Compute the greatest common divisor of two numbers using the Euclidean algorithm.
6-LCM of Two Numbers: Calculate the least common multiple using the relationship with GCD.
7-Check for Prime: Verify if a number is prime (divisible by only 1 and itself).
8-Prime Factors: Find the prime factors of a number.
9-All Divisors of a Number: List all divisors of a number.
10-Sieve of Eratosthenes: Efficiently find all primes up to a given number.
11-Computing Power: Compute a^b using exponentiation by squaring.
12-Modular Arithmetic: Perform operations with a modulus to find remainders in division.
13-Iterative Power: Compute powers iteratively without recursion.

#Recursion:
Recursion is a technique where a function calls itself directly or indirectly to solve a problem.

-Recursion-based Algorithms:
1-Dynamic Programming: Optimizing recursive solutions by storing results to avoid recalculating.
2-Backtracking: Solving problems by trying potential solutions and backtracking when necessary.
3-Divide and Conquer: Solving problems by dividing them into smaller subproblems (e.g., Binary Search, Quick Sort, Merge Sort).
-Problems Inherently Using Recursion:
1-Tower of Hanoi: Solving the puzzle by recursively moving disks between pegs.
2-DFS Traversals: Performing Depth-First Search on a graph or tree, including Inorder, Preorder, and Postorder tree traversals.








