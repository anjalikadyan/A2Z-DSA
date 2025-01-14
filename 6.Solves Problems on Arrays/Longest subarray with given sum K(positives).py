n=int(input("Enter a number: "))
k=int(input("Enter a number: "))
a=[0]*n
preSumMap = {}
Sum = 0
maxLen = 0
for i in range(n):
    Sum += a[i]
    if Sum == k:
        maxLen = max(maxLen, i + 1)
        rem = Sum - k
    if rem in preSumMap:
        length = i - preSumMap[rem]
        maxLen = max(maxLen, length)
    if Sum not in preSumMap:
        preSumMap[Sum] = i
print(maxLen)