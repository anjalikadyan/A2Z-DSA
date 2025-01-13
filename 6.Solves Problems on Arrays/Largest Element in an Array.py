n=int(input("Enter a number: "))
arr=[0]*n
for i in range(n):
    arr[i]=int(input("Enter a number in array: "))
mx=arr[0]
for i in range(len(arr)):
    if mx<arr[i]:
        mx=arr[i]
print(mx)