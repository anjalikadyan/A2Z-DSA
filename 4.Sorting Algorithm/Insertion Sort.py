#The task is to complete the insertsort() function which is used to implement Insertion Sort.
n=int(input("Number :"))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Number in array :"))
for i in range(1,len(arr)):
    k=arr[i]
    j=i-1
    while (j>=0 and arr[j]>k):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=k
print(arr)
