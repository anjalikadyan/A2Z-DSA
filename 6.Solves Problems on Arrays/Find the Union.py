n=int(input("enter a number: "))
m=int(input("enter a number: "))
a=[0]*n
b=[0]*m
c=list(set(a+b))
c.sort()
print(c)