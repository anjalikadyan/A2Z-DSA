n=int(input("Enter the number of elements: "))
arr=[0]*n
for i in range(n):
    arr[i]=input("Enter the array element: ")
    arr[i]=int(arr[i])

print("Original array: ",arr)
def quickSort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
    
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
    tem=arr[i+1]
    arr[i+1]=arr[high]
    arr[high]=tem
    return i+1
quickSort(arr,0,len(arr)-1)
print("Sorted array: ",arr)
