#Given a positive integer value n. The task is to find how many numbers less than or equal to n have numbers of divisors exactly equal to 3.
import math
a=int(input("A number: "))
count=0
def primeit (a:int)->bool:
    if a<2:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i==0):
            return False
    return True
for i in range(2,int(math.sqrt(a))+1):
    if(primeit(i)):
        if i*i<=a:
            count+=1
print(count)