n=int(input("enter the size of arr: "))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("enter arr: "))
print(arr)
def is_sorted(arr,n):
    if n==0 or n==1:
        return True
    elif arr[0]>arr[1]:
        return False
    else:
        return is_sorted(arr[1:],n-1)
print(is_sorted(arr,n))