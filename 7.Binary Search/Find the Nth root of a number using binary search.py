n=int(input("number1: "))
m=int(input("number2: "))
re=round(m**(1/n))
if re**n==m:
    print(re)
else:
    print(-1)