n=int(input("Enter a number: "))
#this is a code for calculate 2^n
def power(n):
    if n==0:
        return 1
    else:
        return 2*power(n-1)
print(power(n))