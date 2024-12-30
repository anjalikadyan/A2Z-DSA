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


1. Absolute Value of an Integer
Task: Find the absolute value of a given integer I.

Description:
Given an integer, the program checks if the number is negative. If so, it converts it to positive. Otherwise, it remains unchanged.

Code:
a = int(input("A number: "))
if(a < 0):
    b = -a
else:
    b = a
print(b)



2. Celsius to Fahrenheit Conversion
Task: Convert a temperature from Celsius to Fahrenheit.

Description:
The program takes a temperature in Celsius and converts it into Fahrenheit using the formula F = (C * 9/5) + 32.

Code:
a=int(input("number: "))
F = (a * 9 / 5) + 32
print("Fahrenheit", F)



3. Factorial of a Number
Task: Calculate the factorial of a positive integer N.

Description:
The program computes the factorial of a given number N, defined as the product of all positive integers less than or equal to N.

Code:
a=int(input("number: "))
sum = 1
for i in range(1, a + 1):
    sum *= i
print("Factorial of N: ", sum)



4. Number of Digits in a Factorial
Task: Find the number of digits in the factorial of a given number N.

Description:
The program calculates the factorial of N and counts the number of digits in the result.

Code:
a=int(input("number: "))
sum = 1
count = 0
for i in range(1, a + 1):
    sum *= i
while sum != 0:
    sum = int(sum / 10)
    count += 1
print(count)



5. Prime Number Check
Task: Check if a given number N is a prime number.

Description:
A prime number is a number that is divisible only by 1 and itself. The program checks if N has any divisors other than 1 and N itself.

Code:
a=int(input("number: "))
count = 1
for i in range(2, a * a + 1):
    if (a % i == 0):
        count += 1
if (count == 2):
    print("Prime")
else:
    print("Not Prime")



6. Numbers with Exactly 3 Divisors
Task: Find how many numbers less than or equal to n have exactly 3 divisors.

Description:
The program identifies numbers that have exactly 3 divisors, which typically are squares of prime numbers.

Code:
import math
a = int(input("A number: "))
count = 0

def primeit(a: int) -> bool:
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if (a % i == 0):
            return False
    return True

for i in range(2, int(math.sqrt(a)) + 1):
    if (primeit(i)):
        if i * i <= a:
            count += 1
print(count)



7. Nth Term of a Geometric Series
Task: Find the Nth term of a geometric series given the first two terms A and B.

Description:
The program calculates the Nth term in a geometric series where the ratio r = B / A.

Code:
a = int(input("A number: "))
b = int(input("B number: "))
c = int(input("N number: "))
if c == 1:
    print(a)
d = b / a
sum = 1
for i in range(1, c):
    sum *= d
f = int(a * sum)
print(f)



8. Sum of Two Numbers Modulo 10^9 +7
Task: Find the sum of two numbers a and b, modulo 10^9 +7.

Description:
The program computes the sum of two integers a and b and then returns the result modulo 10^9 +7, which is a large prime number often used in programming contests.

Code:
import math
a = int(input("A number: "))
b = int(input("B number: "))
c = a + b
d = c % int(math.pow(10, 9) + 7)
print(d)



9. Multiplication of Two Numbers Modulo 10^9 +7
Task: Find the product of two numbers a and b, modulo 10^9 +7.

Description:
This program computes the product of two integers a and b, then takes the result modulo 10^9 +7.

Code:
import math
a = input("A number: ")
a = int(a)
b = int(input("B number: "))
c = a * b
d = int(c % int(math.pow(10, 9) + 7))
print(d)



10. Modular Multiplicative Inverse
Task: Find the smallest modular multiplicative inverse of a under modulo m. If it doesn't exist, return -1.

Description:
This program calculates the modular multiplicative inverse of a modulo m if it exists. The inverse of a modulo m is a number x such that (a * x) % m == 1.

Code:
a = int(input("number: "))
m = int(input("module: "))
for i in range(1, m):
    if ((i * a) % m == 1):
        print(i)

