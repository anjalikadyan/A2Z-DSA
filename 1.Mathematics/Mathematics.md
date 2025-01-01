# Mathematical Problems and Algorithms

This repository contains solutions to several important mathematical problems that are commonly encountered in programming and algorithmic challenges. The problems range from basic number theory to more complex arithmetic algorithms. Below is a breakdown of each problem with a brief description.

---

## 1. Count Digits
### Problem Description:
Given a number `n`, count the total number of digits in `n`. This is a basic problem that tests the ability to manipulate numbers.

### Example:
For `n = 12345`, the output will be `5` (because there are 5 digits in 12345).

### Approach:
This can be achieved by repeatedly dividing the number by 10 until it becomes 0, counting how many divisions occur.

---

## 2. Palindrome Numbers
### Problem Description:
A number is called a palindrome if it remains the same when its digits are reversed.

### Example:
For `n = 121`, the number is a palindrome. For `n = 123`, it is not.

### Approach:
To check for a palindrome, reverse the digits of the number and compare it with the original number.

---

## 3. Factorial of a Number
### Problem Description:
The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. It’s a key concept in combinatorics.

### Example:
For `n = 5`, the factorial is `5! = 5 * 4 * 3 * 2 * 1 = 120`.

### Approach:
This can be calculated iteratively or recursively.

---

## 4. Trailing Zeros in Factorial
### Problem Description:
Trailing zeros in the factorial of a number are caused by the factors of 10 in the number. A factor of 10 comes from multiplying 2 and 5. This problem counts the number of trailing zeros in `n!`.

### Example:
For `n = 100`, the number of trailing zeros in `100!` is `24`.

### Approach:
Count how many times 5 appears as a factor in the numbers from 1 to `n` (since 2 will always be present).

---

## 5. GCD or HCF of Two Numbers
### Problem Description:
The Greatest Common Divisor (GCD) or Highest Common Factor (HCF) is the largest number that divides both `a` and `b` without leaving a remainder.

### Example:
For `a = 56` and `b = 98`, the GCD is `14`.

### Approach:
The GCD can be calculated using the Euclidean algorithm, which works by repeatedly replacing the larger number with the remainder of the division of the two numbers.

---

## 6. LCM of Two Numbers
### Problem Description:
The Least Common Multiple (LCM) is the smallest number that is a multiple of both `a` and `b`.

### Example:
For `a = 4` and `b = 5`, the LCM is `20`.

### Approach:
The relationship between GCD and LCM is given by:

\[ \text{LCM}(a,b) = \frac{|a \times b|}{\text{GCD}(a,b)} \]

---

## 7. Check for Prime
### Problem Description:
A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

### Example:
For `n = 7`, the number is prime. For `n = 10`, the number is not prime.

### Approach:
To check for primality, check if `n` is divisible by any number from `2` to \( \sqrt{n} \). If it is divisible by any, it is not prime.

---

## 8. Prime Factors
### Problem Description:
Prime factorization is the process of determining which prime numbers multiply together to make the original number.

### Example:
For `n = 28`, the prime factors are `2` and `7` (since \( 28 = 2 \times 2 \times 7 \)).

### Approach:
Divide the number by the smallest prime numbers and repeat until the number becomes 1.

---

## 9. All Divisors of a Number
### Problem Description:
Find all the divisors of a number `n`. A divisor of `n` is any number that divides `n` without leaving a remainder.

### Example:
For `n = 36`, the divisors are `1, 2, 3, 4, 6, 9, 12, 18, 36`.

### Approach:
Iterate through numbers from `1` to \( \sqrt{n} \) and check if they divide `n`. If they do, both `i` and `n/i` are divisors.

---

## 10. Sieve of Eratosthenes
### Problem Description:
The Sieve of Eratosthenes is an ancient algorithm used to find all primes smaller than a given number `n`. It efficiently marks the non-prime numbers.

### Example:
For `n = 30`, the primes are `2, 3, 5, 7, 11, 13, 17, 19, 23, 29`.

### Approach:
Start by marking multiples of each prime number starting from 2. Repeat for the next unmarked number.

---

## 11. Computing Power
### Problem Description:
Compute \( a^b \) (a raised to the power of b) efficiently.

### Example:
For `a = 2` and `b = 10`, the result is `1024`.

### Approach:
Use the exponentiation by squaring method to compute powers efficiently, reducing time complexity from \( O(b) \) to \( O(\log b) \).

---

## 12. Modular Arithmetic
### Problem Description:
Modular arithmetic involves computing the remainder of a division. It is widely used in number theory, cryptography, and algorithms.

### Example:
For `a = 10` and `b = 3`, \( a \% b = 1 \) (since 10 divided by 3 gives a remainder of 1).

### Approach:
You can compute \( a \% b \) using the modulus operator in most programming languages. It’s used frequently for efficient computations and in problems involving large numbers.

---

## 13. Iterative Power
### Problem Description:
Iteratively calculate the power of a number \( a^b \) without recursion.

### Example:
For `a = 3` and `b = 4`, the result is `81`.

### Approach:
The iterative approach involves multiplying `a` by itself `b` times.

---
