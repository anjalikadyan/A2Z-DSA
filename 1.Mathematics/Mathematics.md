# Mathematical Problems and Algorithms

This repository contains solutions to several important mathematical problems that are commonly encountered in programming and algorithmic challenges. The problems range from basic number theory to more complex arithmetic algorithms. Below is a breakdown of each problem with detailed explanations, diagrams, and examples.

## Table of Contents
1. [Basic Number Operations](#1-basic-number-operations)
   - [Count Digits](#11-count-digits)
   - [Palindrome Numbers](#12-palindrome-numbers)
2. [Factorial and Related Problems](#2-factorial-and-related-problems)
   - [Factorial of a Number](#21-factorial-of-a-number)
   - [Trailing Zeros in Factorial](#22-trailing-zeros-in-factorial)
3. [Number Theory](#3-number-theory)
   - [GCD or HCF of Two Numbers](#31-gcd-or-hcf-of-two-numbers)
   - [LCM of Two Numbers](#32-lcm-of-two-numbers)
   - [Check for Prime](#33-check-for-prime)
   - [Prime Factors](#34-prime-factors)
   - [All Divisors of a Number](#35-all-divisors-of-a-number)
   - [Sieve of Eratosthenes](#36-sieve-of-eratosthenes)
4. [Exponentiation and Modular Arithmetic](#4-exponentiation-and-modular-arithmetic)
   - [Computing Power](#41-computing-power)
   - [Modular Arithmetic](#42-modular-arithmetic)
   - [Iterative Power](#43-iterative-power)

---

## 1. Basic Number Operations

### 1.1 Count Digits
#### Problem Description:
Given a number `n`, count the total number of digits in `n`. This is a fundamental problem that tests the ability to manipulate numbers.

#### Example:
```
Input: n = 12345
Output: 5
Explanation: The number 12345 has 5 digits: 1, 2, 3, 4, and 5.
```

#### Approaches:
1. **Iterative Approach**:
   ```python
   def count_digits(n):
       count = 0
       while n > 0:
           n = n // 10
           count += 1
       return count
   ```
   Time Complexity: O(log₁₀ n)
   Space Complexity: O(1)

2. **Logarithmic Approach**:
   ```python
   import math
   def count_digits(n):
       return math.floor(math.log10(n) + 1)
   ```
   Time Complexity: O(1)
   Space Complexity: O(1)

#### Diagram:
```
n = 12345
Step 1: 12345 // 10 = 1234, count = 1
Step 2: 1234 // 10 = 123, count = 2
Step 3: 123 // 10 = 12, count = 3
Step 4: 12 // 10 = 1, count = 4
Step 5: 1 // 10 = 0, count = 5
```

### 1.2 Palindrome Numbers
#### Problem Description:
A number is called a palindrome if it remains the same when its digits are reversed.

#### Example:
```
Input: n = 121
Output: True
Explanation: 121 reversed is 121, which is the same as the original number.

Input: n = 123
Output: False
Explanation: 123 reversed is 321, which is different from the original number.
```

#### Approaches:
1. **String Conversion Approach**:
   ```python
   def is_palindrome(n):
       return str(n) == str(n)[::-1]
   ```
   Time Complexity: O(log₁₀ n)
   Space Complexity: O(log₁₀ n)

2. **Mathematical Approach**:
   ```python
   def is_palindrome(n):
       original = n
       reverse = 0
       while n > 0:
           reverse = reverse * 10 + n % 10
           n = n // 10
       return original == reverse
   ```
   Time Complexity: O(log₁₀ n)
   Space Complexity: O(1)

#### Diagram:
```
n = 121
Step 1: reverse = 0 * 10 + 121 % 10 = 1, n = 121 // 10 = 12
Step 2: reverse = 1 * 10 + 12 % 10 = 12, n = 12 // 10 = 1
Step 3: reverse = 12 * 10 + 1 % 10 = 121, n = 1 // 10 = 0
Final: 121 == 121 → True
```

---

## 2. Factorial and Related Problems

### 2.1 Factorial of a Number
#### Problem Description:
The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. It's a fundamental concept in combinatorics and probability.

#### Example:
```
Input: n = 5
Output: 120
Explanation: 5! = 5 × 4 × 3 × 2 × 1 = 120
```

#### Approaches:
1. **Iterative Approach**:
   ```python
   def factorial(n):
       result = 1
       for i in range(2, n + 1):
           result *= i
       return result
   ```
   Time Complexity: O(n)
   Space Complexity: O(1)

2. **Recursive Approach**:
   ```python
   def factorial(n):
       if n == 0 or n == 1:
           return 1
       return n * factorial(n - 1)
   ```
   Time Complexity: O(n)
   Space Complexity: O(n) (due to recursion stack)

#### Diagram:
```
n = 5
Iterative:
Step 1: result = 1 * 2 = 2
Step 2: result = 2 * 3 = 6
Step 3: result = 6 * 4 = 24
Step 4: result = 24 * 5 = 120

Recursive:
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120
```

### 2.2 Trailing Zeros in Factorial
#### Problem Description:
Count the number of trailing zeros in the factorial of a number. Trailing zeros are created by factors of 10, which come from pairs of 2 and 5 in the prime factorization.

#### Example:
```
Input: n = 100
Output: 24
Explanation: 100! has 24 trailing zeros
```

#### Approach:
```python
def count_trailing_zeros(n):
    count = 0
    while n >= 5:
        n = n // 5
        count += n
    return count
```
Time Complexity: O(log₅ n)
Space Complexity: O(1)

#### Diagram:
```
n = 100
Step 1: count = 0 + 100//5 = 20, n = 100//5 = 20
Step 2: count = 20 + 20//5 = 24, n = 20//5 = 4
Step 3: n < 5, stop
Final count = 24
```

---

## 3. Number Theory

### 3.1 GCD or HCF of Two Numbers
#### Problem Description:
The Greatest Common Divisor (GCD) or Highest Common Factor (HCF) is the largest number that divides both `a` and `b` without leaving a remainder.

#### Example:
```
Input: a = 56, b = 98
Output: 14
Explanation: The largest number that divides both 56 and 98 is 14.
```

#### Approaches:
1. **Euclidean Algorithm**:
   ```python
   def gcd(a, b):
       while b:
           a, b = b, a % b
       return a
   ```
   Time Complexity: O(log(min(a, b)))
   Space Complexity: O(1)

2. **Recursive Euclidean Algorithm**:
   ```python
   def gcd(a, b):
       if b == 0:
           return a
       return gcd(b, a % b)
   ```
   Time Complexity: O(log(min(a, b)))
   Space Complexity: O(log(min(a, b)))

#### Diagram:
```
a = 56, b = 98
Step 1: a = 98, b = 56 % 98 = 56
Step 2: a = 56, b = 98 % 56 = 42
Step 3: a = 42, b = 56 % 42 = 14
Step 4: a = 14, b = 42 % 14 = 0
Final GCD = 14
```

### 3.2 LCM of Two Numbers
#### Problem Description:
The Least Common Multiple (LCM) is the smallest number that is a multiple of both `a` and `b`.

#### Example:
```
Input: a = 4, b = 5
Output: 20
Explanation: 20 is the smallest number that is divisible by both 4 and 5.
```

#### Approach:
```python
def lcm(a, b):
    return (a * b) // gcd(a, b)
```
Time Complexity: O(log(min(a, b)))
Space Complexity: O(1)

#### Diagram:
```
a = 4, b = 5
GCD(4, 5) = 1
LCM = (4 * 5) // 1 = 20
```

### 3.3 Check for Prime
#### Problem Description:
A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

#### Example:
```
Input: n = 7
Output: True
Explanation: 7 has no divisors other than 1 and itself.

Input: n = 10
Output: False
Explanation: 10 has divisors 2 and 5 besides 1 and itself.
```

#### Approaches:
1. **Naive Approach**:
   ```python
   def is_prime(n):
       if n <= 1:
           return False
       for i in range(2, n):
           if n % i == 0:
               return False
       return True
   ```
   Time Complexity: O(n)
   Space Complexity: O(1)

2. **Optimized Approach**:
   ```python
   def is_prime(n):
       if n <= 1:
           return False
       if n <= 3:
           return True
       if n % 2 == 0 or n % 3 == 0:
           return False
       i = 5
       while i * i <= n:
           if n % i == 0 or n % (i + 2) == 0:
               return False
           i += 6
       return True
   ```
   Time Complexity: O(√n)
   Space Complexity: O(1)

#### Diagram:
```
n = 7
Step 1: Check divisibility by 2 → No
Step 2: Check divisibility by 3 → No
Step 3: Check divisibility by 5 → No
Final: 7 is prime
```

### 3.4 Prime Factors
#### Problem Description:
Prime factorization is the process of determining which prime numbers multiply together to make the original number.

#### Example:
```
Input: n = 28
Output: [2, 2, 7]
Explanation: 28 = 2 × 2 × 7
```

#### Approach:
```python
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    if n > 2:
        factors.append(n)
    return factors
```
Time Complexity: O(√n)
Space Complexity: O(log n)

#### Diagram:
```
n = 28
Step 1: 28 % 2 = 0 → factors = [2], n = 14
Step 2: 14 % 2 = 0 → factors = [2, 2], n = 7
Step 3: 7 % 3 = 1 → skip
Step 4: 7 % 5 = 2 → skip
Step 5: n = 7 > 2 → factors = [2, 2, 7]
```

### 3.5 All Divisors of a Number
#### Problem Description:
Find all the divisors of a number `n`. A divisor of `n` is any number that divides `n` without leaving a remainder.

#### Example:
```
Input: n = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
```

#### Approach:
```python
def divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors)
```
Time Complexity: O(√n)
Space Complexity: O(√n)

#### Diagram:
```
n = 36
Step 1: i = 1 → 36 % 1 = 0 → divisors = [1, 36]
Step 2: i = 2 → 36 % 2 = 0 → divisors = [1, 36, 2, 18]
Step 3: i = 3 → 36 % 3 = 0 → divisors = [1, 36, 2, 18, 3, 12]
Step 4: i = 4 → 36 % 4 = 0 → divisors = [1, 36, 2, 18, 3, 12, 4, 9]
Step 5: i = 5 → 36 % 5 ≠ 0 → skip
Step 6: i = 6 → 36 % 6 = 0 → divisors = [1, 36, 2, 18, 3, 12, 4, 9, 6]
```

### 3.6 Sieve of Eratosthenes
#### Problem Description:
The Sieve of Eratosthenes is an ancient algorithm used to find all primes smaller than a given number `n`.

#### Example:
```
Input: n = 30
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

#### Approach:
```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]
```
Time Complexity: O(n log log n)
Space Complexity: O(n)

#### Diagram:
```
n = 30
Initial: [F, F, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T]

After marking multiples of 2:
[F, F, T, T, F, T, F, T, F, T, F, T, F, T, F, T, F, T, F, T, F, T, F, T, F, T, F, T, F, T, F]

After marking multiples of 3:
[F, F, T, T, F, T, F, T, F, F, F, T, F, T, F, F, F, T, F, T, F, F, F, T, F, T, F, F, F, T, F]

After marking multiples of 5:
[F, F, T, T, F, T, F, T, F, F, F, T, F, T, F, F, F, T, F, T, F, F, F, T, F, T, F, F, F, T, F]

Final primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

## 4. Exponentiation and Modular Arithmetic

### 4.1 Computing Power
#### Problem Description:
Compute \( a^b \) (a raised to the power of b) efficiently.

#### Example:
```
Input: a = 2, b = 10
Output: 1024
```

#### Approaches:
1. **Naive Approach**:
   ```python
   def power(a, b):
       result = 1
       for _ in range(b):
           result *= a
       return result
   ```
   Time Complexity: O(b)
   Space Complexity: O(1)

2. **Binary Exponentiation**:
   ```python
   def power(a, b):
       result = 1
       while b > 0:
           if b % 2 == 1:
               result *= a
           a *= a
           b //= 2
       return result
   ```
   Time Complexity: O(log b)
   Space Complexity: O(1)

#### Diagram:
```
a = 2, b = 10
Step 1: b = 10 (even) → a = 4, b = 5
Step 2: b = 5 (odd) → result = 4, a = 16, b = 2
Step 3: b = 2 (even) → a = 256, b = 1
Step 4: b = 1 (odd) → result = 1024, a = 65536, b = 0
Final result = 1024
```

### 4.2 Modular Arithmetic
#### Problem Description:
Modular arithmetic involves computing the remainder of a division. It's widely used in cryptography and algorithms.

#### Example:
```
Input: a = 10, b = 3
Output: 1
Explanation: 10 divided by 3 gives a remainder of 1.
```

#### Properties:
1. (a + b) mod m = ((a mod m) + (b mod m)) mod m
2. (a * b) mod m = ((a mod m) * (b mod m)) mod m
3. (a - b) mod m = ((a mod m) - (b mod m) + m) mod m

#### Diagram:
```
a = 10, b = 3
10 ÷ 3 = 3 with remainder 1
10 mod 3 = 1
```

### 4.3 Iterative Power
#### Problem Description:
Calculate the power of a number \( a^b \) iteratively without recursion.

#### Example:
```
Input: a = 3, b = 4
Output: 81
```

#### Approach:
```python
def iterative_power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result
```
Time Complexity: O(b)
Space Complexity: O(1)

#### Diagram:
```
a = 3, b = 4
Step 1: result = 1 * 3 = 3
Step 2: result = 3 * 3 = 9
Step 3: result = 9 * 3 = 27
Step 4: result = 27 * 3 = 81
Final result = 81
```

---
