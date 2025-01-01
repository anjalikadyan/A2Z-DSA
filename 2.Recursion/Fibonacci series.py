n=int(input("enter a number= "))
#this is a code for nth fibonacci number
def fib(n):
    if n==0:
        return [0]
    elif n==1:
        return [1]
    elif n==2:
        return [0,1]
    else:
        series=fib(n-1)
        series.append(series[-1]+series[-2])
        return series
ans=fib(n)
print(ans)
