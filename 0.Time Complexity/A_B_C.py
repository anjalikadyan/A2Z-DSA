# Code 5
def fun(n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c

#Time Complexity: Big O(n).
#Space Complexity: Big O(1).