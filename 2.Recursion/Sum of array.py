n=int(input("Enter the size of arr: "))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Enter the number: "))
print(arr)

def sumth(arr,n):
    if n==0:
        return 0
    elif n==1:
        return arr[0]
    else:
        rem=sumth(arr[1:],n-1)
        sum=arr[0]+rem
        return sum
ans=sumth(arr,n)
print("sum of the array is: ",ans)