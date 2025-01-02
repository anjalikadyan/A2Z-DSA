#Given an array, arr[]. Sort the array using bubble sort algorithm.
n=int(input("Number :"))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Number in array :"))
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)