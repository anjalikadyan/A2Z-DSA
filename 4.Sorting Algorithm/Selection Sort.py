#Given an array arr, use selection sort to sort arr[] in increasing order.
n=int(input("Number :"))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Number in array :"))
for i in range(len(arr)-1):
    num=i
    for j in range(i+1,len(arr)):
        if arr[num]>arr[j]:
            num=j
    temp=arr[i]
    arr[i]=arr[num]
    arr[num]=temp
print(arr)
