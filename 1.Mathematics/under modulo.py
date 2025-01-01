#You are given two numbers a and b. You need to find the multiplication of a and b under modulo M (M as 10^9+7).
import math
a=input("A number: ")
a=int(a)
b=int(input("B number: "))
c=a*b
d=int(c%int(math.pow(10,9)+7))
print(d)