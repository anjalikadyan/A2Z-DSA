n=int(input("Enter a number: "))
target=int(input("Enter a number: "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input("Enter a number in array: "))
a=[-1,-1]
for i in range(len(nums)):
    if nums[i]==target and a[0]==-1:
        a[0]=i
    if nums[i]==target and i!=a[1]:
        a[1]=i
print(a)