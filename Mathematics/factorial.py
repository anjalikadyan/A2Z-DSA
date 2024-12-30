#Given a positive integer N. The task is to find factorial of N.
a=int(input("Enter a number: "))
sum=1
for i in range(1,a+1):
    sum*=i
print("factorial of N numbers: ",sum)