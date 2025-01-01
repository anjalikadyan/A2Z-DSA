from collections import Counter
n=int(input())
arr=[0]*n
for i in range(n):
    arr[i]=input("word:")
print(arr)
freq=Counter(arr)
res=list(map(lambda x:freq[x],arr))
print(res)
