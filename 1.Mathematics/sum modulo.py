#Given two numbers a and b, find the sum of a and b. Since the sum can be very large, find the sum modulo 10^9+7.
import math
a=int(input("A number: "))
b=int(input("B number: "))
c=a+b
d=c%int(math.pow(10,9)+7)
print(d)