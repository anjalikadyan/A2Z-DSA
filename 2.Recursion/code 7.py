n=int(input("Enter the number: "))
def fib(n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
            
ans=fib(n)
print(ans)