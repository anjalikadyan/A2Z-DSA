n=int(input("enter n="))
#this is a code for factorial of a number
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(n))