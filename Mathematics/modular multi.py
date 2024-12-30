#Given two integers ‘a’ and ‘m’.The task is to find the smallest modular multiplicative inverse of ‘a’ under modulo ‘m’.if it does not exist then return -1.
a=int(input("number: "))
m=int(input("module: "))
for i in range(1,m):
    if((i*a)%m==1):
        print(i)