n=int(input("Enter a number: "))
x=int(input("Enter a number: "))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Enter a number in array: "))
a=-1
b=-1
for i in range(len(arr)):
    if arr[i]<=x :
        a=max(arr[i],a)
    if arr[i]>=x:
        b=min(arr[i],b) if b!=-1 else arr[i]
print(a)
print(b)