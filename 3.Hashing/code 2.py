from collections import Counter
n=int(input())
arr=[0]*n
for i in range(n):
    arr[i]=input("word:")
print(arr)
freq=Counter(arr)
res=list(map(lambda x:freq[x],arr))
sum=res[0]
for i in range(1,n):
    if sum<res[i]:
        sum=res[i]
print(sum)

