import math
n=int(input("number: "))
re=int(math.floor(math.sqrt(n)))
de=int(math.sqrt(n))
if de*de==n:
    print(de)
else:
    print(re)