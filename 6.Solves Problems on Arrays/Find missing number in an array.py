n=int(input("Enter a number: "))
nums=[0]*n
arr=[0]*(n+1)
for i in range(n):
    arr[nums[i]]+=1
for i in range(1,n+1):
    if arr[i]==0:
        print(i)
print("end")