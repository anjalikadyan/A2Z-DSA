# Example Problem: Factorial
# A classic example of recursion is the factorial function, which calculates the product of all integers from 1 to n.

def factorial(n: int) -> int:
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive call
# In this example, the function calls itself with smaller values of n until it reaches the base case (n == 0).