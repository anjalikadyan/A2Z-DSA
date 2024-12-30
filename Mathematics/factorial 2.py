#Given an integer N. Find the number of digits that appear in its factorial.Factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.
a=int(input("A number: "))
sum=1
count=0
for i in range(1,a+1):
    sum*=i
while(sum!=0):
    sum=int(sum/10)
    count+=1
print(count)