#A prime number is a number which is only divisible by 1 and itself.Given number N check if it is prime or not.
a=int(input("A number: "))
count=1
for i in range(2,a*a+1):
    if(a%i==0):
        count+=1
if(count==2):
    print("tr")
else:
    print("no")