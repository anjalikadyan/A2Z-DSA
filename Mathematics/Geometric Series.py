#Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.
a=int(input("A number: "))
b=int(input("B number: "))
c=int(input("N number: "))
if c==1:
    print(a)
d=b/a
sum=1
for i in range(1,c):
    sum*=d
f=int(a*sum)
print(f)