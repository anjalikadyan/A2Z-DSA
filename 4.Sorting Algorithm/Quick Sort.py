n=int(input("Enter the number of elements: "))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Enter the arrayelement: "))
print("Original array: ",arr)
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<=pivot]
    right=[x for x in arr[:-1] if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
print(quick_sort(arr))
